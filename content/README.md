> **このコピーの教材セット：** App シナリオと各章の CLI 代替手順を使用します。CLI 独立コースと Mona Mayhem は参考資料です。 [日本語の教材セット](../README.ja.md) を参照してください。以下は参照元のイベント資料です。参照元への変更送信は行いません。

# 📚 Content

This folder contains the **official content** for **Dev Days**, including presentation slides and hands-on labs. See [📚 Core Content](#-core-content).

The current round of Dev Days focuses on the **GitHub Copilot app**, the only desktop experience for agent-driven development built natively on GitHub. Alternatively, if your audience wants to focus on development tools in the Terminal, you may focus on the GitHub Copilot CLI.

Dev Days events are flexible, so organizers should feel empowered to adjust the format based on the needs of their audience.

> 🔎 **Highlight**
> All workshop content is available at **[github.github.com/dev-days](https://github.github.com/dev-days/)**. This is the best link to share with attendees — it displays every available workshop option for Dev Days events so participants can navigate directly to the lab for your event.

## 🗓️ Sample Agenda (Session + Workshop)

This suggested event agenda includes one **Session** and one **Workshop** (approximately 2-3 hours total).

| Order | Session            | Type         | Estimated Time | Description                                                                           |
| ----: | ------------------ | ------------ | -------------- | ------------------------------------------------------------------------------------- |
|    01 | **GitHub Copilot app**   | Session      | 30–45 min      | The provided slide deck is an overview of the GitHub Copilot app.                |
|    02 | **Hands-on Lab**       | Hands-on Lab | 60–90 min (App), 120 min (Tailspin CLI), 60 min (Mona Mayhem) | Select one lab and reserve its full duration. |

Allow another 15 minutes for setup or switching tools, plus breaks and questions. Tailspin CLI needs a 3-hour event slot with a 30-minute talk and 30 minutes for setup and closing. If time runs short, prioritize one feature, its verification, and a reviewable diff; move extensions and additional agent workflows to follow-up work.

## 🔍 Prerequisites

Dev Days events are open to developers of all experience levels. Different events may cover different topics that are more relevant for a subset of developers.
> Checked against GitHub Docs on 2026-09-08: the [Copilot app](https://docs.github.com/en/copilot/concepts/agents/github-copilot-app) and [Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli) are available with all Copilot plans. Some external lessons still list older paid-plan requirements. Free access does not guarantee enough AI credits to finish every exercise. Check usage before and during the event. Organization users must confirm the App and CLI policies separately; access to one does not establish access to the other.


**For organizers**:

- Clearly define the topics you plan to cover on your registration page.

- Include any additional prerequisites relevant to your event. Make sure to inform attendees whether they need to bring their own laptops or if devices will be provided at the venue (common for events hosted at universities).

**For attendees**:

- **An active GitHub Copilot plan**, sufficient available usage, and a successful test prompt using the tool selected for the event — [Sign up here](https://aka.ms/get-github-copilot-devdays).

- Download the [GitHub Copilot app](https://gh.io/dev-days/app) if your event includes the GitHub Copilot app session or workshop.

- Install the [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli) if your event includes the GitHub Copilot CLI session or workshop.

- Laptop — Required for events that include a hands-on workshop.

| Workshop | Prepare before attending |
| --- | --- |
| Copilot app | Git, Node.js 22.13+, the App, and your own Tailspin Toys template repository. See [App prerequisites](https://github-samples.github.io/copilot-workshops/app/0-prerequisites/). |
| Tailspin Toys CLI | Your own Tailspin Toys template repository and a working Codespace or local dev container; install and authenticate CLI there. See [CLI prerequisites](https://github-samples.github.io/copilot-workshops/cli/0-prerequisites/). Check Codespaces availability and remaining usage if using it. |
| Mona Mayhem CLI | Git, Node.js, CLI, and your own copy of Mona Mayhem. Check the runtime required by the selected repository revision; npm installation of CLI needs Node.js 22+. See [Mona Mayhem prerequisites](https://github.com/copilot-dev-days/mona-mayhem#prerequisites). |

For this Japanese copy, use the [Japanese preparation and CLI fallback guide](../website/ja/handson-guide.html). The [Japanese workshop texts](../website/ja/workshops/index.html) cover all three current courses, including prompts. Slides, videos, and archived labs remain in their original languages. Rehearse the fallback before the event: UI changes can prevent participants from following screenshots. Continue planning, implementation, and testing in CLI on the same worktree; demonstrate App-only experiences separately. Record the lab commit, App/CLI versions, verified commands, and known UI differences during rehearsal.

## 📚 Core Content

For this round of Dev Days, you have two options for your event focus:
1. **[Recommended] GitHub Copilot app**, the only desktop experience for agent-driven development built natively on GitHub. 
2. **GitHub Copilot CLI**, Alternatively, if your audience wants to focus on development tools in the Terminal, you may focus on the GitHub Copilot CLI.

### ⭐ [Recommended] Option 1: GitHub Copilot app

The **GitHub Copilot app** is the only desktop experience for agent-driven development built natively on GitHub. 

| Name | Type | Time | Description / Concepts Taught | Level | Train the trainer |
| ---- | ---- | ---- | ----------------------------- | ----- | ------ |
| [⬇️**GitHub Copilot app**](https://github.com/github/dev-days/releases/download/2026-07-30/copilot-app-english.pptx) | Session/Talk | ~30 min | The GitHub Copilot app is the only desktop experience for agent-driven development built natively on GitHub. | Beginner | [English](https://www.youtube.com/live/SsFU0w3KrI4?si=M2yntYxNFM-U_LwP), [Spanish](https://www.youtube.com/live/PTBDlAa0_aM?si=i2jekaHzrVzZDx6T), [Portuguese](https://www.youtube.com/watch?v=O5ALS9rvTg8), [Korean](https://www.youtube.com/live/4ea0lmGXJiA?si=rrffYuhMdNlOuQFd), [Mandarin Chinese](https://www.bilibili.com/video/BV1T93v6VEca)
| [**GitHub Copilot app Workshop**](https://github.github.com/dev-days/) | Hands-on Lab | ~1 - 1.5 hr | Scenario: Your team is adopting AI agents to work through a growing backlog. The Copilot app gives you one place to direct that work — picking up issues, running agents, reviewing changes, and merging pull requests. This lesson gets you installed, connected, and comfortable starting a conversation about your project. | Beginner |

> The GitHub Copilot app presentation and workshop are available in multiple languages: 
> Spanish ([⬇️presentation](https://github.com/github/dev-days/releases/download/2026-07-30/copilot-app-spanish.pptx), [workshop](https://github-samples.github.io/copilot-workshops/es-es/app/)), Portuguese ([⬇️presentation](https://github.com/github/dev-days/releases/download/2026-07-30/copilot-app-portuguese.pptx), [workshop](https://github-samples.github.io/copilot-workshops/pt-br/app/)), simplified Chinese ([⬇️presentation](https://github.com/github/dev-days/releases/download/2026-07-30/copilot-app-chinese.pptx), [workshop](https://github-samples.github.io/copilot-workshops/zh-cn/app/)),  Korean ([⬇️presentation](https://github.com/github/dev-days/releases/download/2026-07-30/copilot-app-korean.pptx), [workshop](https://github-samples.github.io/copilot-workshops/ko-kr/app/)).

### ⌨️ Option 2: GitHub Copilot CLI

Copilot CLI is more than a chat interface. It’s an autonomous coding agent that can plan complex tasks, execute multistep workflows, edit files, run tests, and iterate until the job is done. 
> There are two workshop topic options for the GitHub Copilot CLI. Choose the one that best suits your audience.

| Name          | Type         | Time      | Description / Concepts Taught | Level         |
| ------------- | ------------ | --------- | ----------------------------- | ------------- |
| [⬇️**GitHub Copilot CLI**](https://github.com/github/dev-days/releases/download/2026-07-30/copilot-CLI.pptx) | Session/Talk | ~30 min | GitHub Copilot CLI in the terminal and command-line workflows. | Beginner |
| [**GitHub Copilot CLI: Tailspin Toys Workshop**](https://github.github.com/dev-days/) | Hands-on Lab | ~2 hr | Master GitHub Copilot in the terminal with Tailspin Toys. Covers custom instructions, Copilot CLI setup, MCP servers, custom agents, and agent skills for AI-assisted delivery. | Intermediate |
| [**GitHub Copilot CLI: Mona Mayhem Workshop**](https://copilot-dev-days.github.io/mona-mayhem/?track=cli) | Hands-on Lab | ~1 hr | Build a retro arcade contribution-battle game while learning context engineering, planning, implementation, and review in Copilot CLI. | Intermediate |

## 🧠 How to use this content

* Use **sessions** to introduce concepts and workflows
* Use **hands-on labs** for guided, practical learning
* Prefer **one hands-on lab per event** to ensure enough execution time
