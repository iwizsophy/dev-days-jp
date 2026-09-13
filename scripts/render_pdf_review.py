"""Render every generated PDF page plus contact sheets for visual release review."""
from pathlib import Path
import argparse
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '.workshop-tools'))
import pymupdf
from PIL import Image, ImageDraw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--output-dir', type=Path, default=Path('tmp/pdfs/review'))
    args = parser.parse_args()
    target = args.output_dir / args.pdf.stem
    target.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(args.pdf)
    for i, page in enumerate(doc):
        page.get_pixmap(matrix=pymupdf.Matrix(1.3, 1.3)).save(target / f'page-{i+1:03}.png')
    for start in range(0, len(doc), 12):
        sheet = Image.new('RGB', (1200, 1760), '#d1d5db')
        draw = ImageDraw.Draw(sheet)
        for i in range(start, min(start + 12, len(doc))):
            im = Image.open(target / f'page-{i+1:03}.png'); im.thumbnail((390, 545))
            x, y = (i-start) % 3 * 400, (i-start) // 3 * 440
            im.thumbnail((300, 415))
            sheet.paste(im, (x, y + 22)); draw.text((x + 4, y + 4), str(i+1), fill='black')
        sheet.save(target / f'contact-{start//12:02}.jpg')
    print(f'Rendered {len(doc)} pages to {target}')


if __name__ == '__main__': main()
