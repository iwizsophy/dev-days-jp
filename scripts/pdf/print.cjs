// Render only the generated, self-contained HTML. No network resources are loaded.
const { chromium } = require('playwright');
const { pathToFileURL } = require('node:url');
const fs = require('node:fs');

(async () => {
  const [input, output, executable] = process.argv.slice(2);
  if (!input || !output) throw new Error('Usage: node print.cjs INPUT OUTPUT [CHROMIUM]');
  const browser = await chromium.launch({ headless: true, ...(executable ? { executablePath: executable } : {}) });
  try {
    const page = await browser.newPage();
    await page.route(/^https?:/, route => route.abort());
    await page.goto(pathToFileURL(input).href, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    const errors = await page.evaluate(() => {
      const failures = [...document.images].filter(i => !i.complete || !i.naturalWidth).map(i => i.alt);
      for (const a of document.querySelectorAll('a[href^="#"]')) {
        if (!document.getElementById(decodeURIComponent(a.hash.slice(1)))) failures.push(`Broken anchor: ${a.hash}`);
      }
      for (const pre of document.querySelectorAll('pre')) {
        if (pre.scrollWidth > pre.clientWidth + 2) failures.push('Code block horizontal overflow');
      }
      return failures;
    });
    if (errors.length) throw new Error(errors.join('\n'));
    await page.pdf({ path: output, format: 'A4', printBackground: true,
      preferCSSPageSize: true, tagged: true, outline: true, displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: '<div style="font-family:Arial;font-size:9px;width:100%;text-align:center;color:#607080">Dev Days / Copilot App &nbsp; · &nbsp; <span class="pageNumber"></span> / <span class="totalPages"></span></div>' });
    fs.writeFileSync(output + '.render.json', JSON.stringify({ images: await page.locator('img').count(), headings: await page.locator('h1').allTextContents() }, null, 2));
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode = 1; });
