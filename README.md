# AI-video-auto-editing

Language / 语言：

- [中文 README](README.zh-CN.md)
- [English README](README.en.md)
- [Agent 工作流程图](workflow/agent-workflow-diagram.md)
- [Interactive Demo](demo/index.html)

AI-video-auto-editing is a Codex Skills + Remotion workflow project for building a repeatable AI-assisted video production system.

AI-video-auto-editing 是一个基于 Codex Skills + Remotion 的 AI 视频自动剪辑工作流项目，用来把视频创作拆成可复用、可调试、可迭代优化的生产流程。

## Quick Overview

The project organizes video production into layered responsibilities:

```text
Planning -> Script -> Assets -> Alignment -> Motion -> Audio -> Remotion Assembly -> QA/Export -> Retrospective
```

It includes:

- 10 custom Codex Skills
- Reusable full-production prompts
- Layer-specific rerun prompts
- A prompt retrospective loop
- A Remotion-oriented assembly plan
- Workflow documents for repeatable video creation
- A visual Agent workflow diagram for first-time readers
- A lightweight interactive demo page

## Repository

```text
.
├── AGENTS.md
├── README.md
├── README.zh-CN.md
├── README.en.md
├── assets/
├── exports/
├── plan/
├── prompts/
├── skills/
└── workflow/
```

For full documentation, choose a language above.
