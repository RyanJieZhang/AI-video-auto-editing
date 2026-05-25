# AI-video-auto-editing

[中文](README.zh-CN.md) | [English](README.en.md)

一个基于 Codex Skills + Remotion 的 AI 视频自动剪辑工作流项目。

这个仓库的目标不是只写一个万能 prompt，而是把视频创作拆成可复用、可调试、可逐步优化的生产系统：从创意规划、口播脚本、素材收集、素材对齐、动效规划、音频设计，到 Remotion 装配、QA、导出和发布包装。

## 项目定位

本项目适合用来搭建一套“从 0 到 1”的视频创作流程：

- 输入一个视频需求或原始素材
- 由 Codex 按层级拆解任务
- 每一层生成明确产物
- 将产物逐步交给下一层
- 最后进入 Remotion 实现、预览、导出和发布包装
- 每次制作结束后复盘 prompt 和 skills，让下一次更稳定、更快

核心思想：

```text
规划 -> 脚本 -> 素材 -> 对齐 -> 动效 -> 音频 -> Remotion 装配 -> QA/导出 -> 复盘优化
```

## 8 层视频创作系统

项目使用分层协作，而不是让一个 prompt 负责所有事情。

| 层级 | 模块 | 负责内容 | 对应 Skill |
| --- | --- | --- | --- |
| 1 | Workflow Router / Index | 判断当前阶段，决定调用哪个 skill | `video-workflow-router` |
| 2 | Creative & Planning | 明确主题、受众、hook、章节、视觉方向 | 项目 workflow 模板 |
| 3 | Voiceover Editor | 口播转写、口语化改写、spoken beats | `voiceover-editor` |
| 4 | Asset Factory | 搜集、生成、下载、转码、验证素材 | `asset-gathering` |
| 5 | Asset Usage & Alignment | 素材去重、时间线分配、语义对齐 | `asset-usage-planner` |
| 6 | Motion / HyperFrames | 高级动效、hook frame、转场、数据卡 | `motion-fragments` |
| 7 | Audio Direction | BGM、SFX、ducking、人声优先、音频策略 | `audio-director` |
| 8 | Remotion Assembly / QA / Export | Composition、Scene、Sequence、字幕、导出 | `remotion-assembler`、`remotion-gotchas-index`、`platform-packaging` |

额外还有一个用于持续优化的 skill：

| 模块 | 负责内容 | 对应 Skill |
| --- | --- | --- |
| Prompt Lab | 反复测试 prompt、复盘失败点、优化 workflow 和 skills | `video-prompt-lab` |

## 仓库结构

```text
.
├── AGENTS.md
├── README.md
├── assets/
├── exports/
├── plan/
├── prompts/
│   ├── layer-rerun-prompts.md
│   ├── master-codex-video-production.md
│   └── retrospective-prompt.md
├── skills/
│   ├── asset-gathering/
│   ├── asset-usage-planner/
│   ├── audio-director/
│   ├── motion-fragments/
│   ├── platform-packaging/
│   ├── remotion-assembler/
│   ├── remotion-gotchas-index/
│   ├── video-prompt-lab/
│   ├── video-workflow-router/
│   └── voiceover-editor/
└── workflow/
    ├── layer-output-templates.md
    ├── prompt-iteration-log.md
    └── video-creation-system.md
```

### 关键目录说明

- `AGENTS.md`：项目级 Codex 执行规则。Codex 进入本项目后应优先遵循这里的路由规则。
- `workflow/`：完整视频创作系统说明、每层产物模板、prompt 迭代日志。
- `prompts/`：可直接复制给 Codex 的主流程 prompt、单层重跑 prompt、复盘 prompt。
- `skills/`：本项目沉淀出来的自定义 Codex Skills。
- `plan/`：创意简报、脚本、素材清单、时间线、动效计划、音频计划等中间产物。
- `assets/`：视频、图片、音乐、音效、截图、生成素材等。
- `exports/`：最终导出视频、封面、发布文案、QA 检查结果。

## 自定义 Skills

本仓库内置 10 个自定义 Codex Skills。

### `video-workflow-router`

负责判断当前任务属于哪一层，并决定下一步调用哪个 skill。

适用场景：

- 新视频任务开始时
- 不确定当前应该改脚本、素材、时间线还是 Remotion 代码时
- 多轮修改后需要重新定位进度时

### `voiceover-editor`

负责把创意或草稿改成适合口播的视频脚本。

负责：

- 口语化改写
- 拆分 spoken beats
- 估算每个 beat 的时长
- 标注 A-roll / B-roll 需求
- 标注需要素材支持的画面点

不负责：

- 下载素材
- 最终剪辑
- Remotion 编码

### `asset-gathering`

负责素材获取和素材 manifest。

负责：

- 搜索素材
- 生成素材
- 下载素材
- 转码素材
- 验证素材可用性
- 记录来源、版权、用途、状态

输出通常是：

```text
plan/asset-list.md
assets/
```

### `asset-usage-planner`

负责决定素材如何拼接进视频。

负责：

- 将素材分配给脚本 beat
- 规划 A-roll / B-roll
- 避免重复素材
- 构建 scene-level 时间线
- 发现素材缺口

输出通常是：

```text
plan/timeline.md
```

### `motion-fragments`

负责高级动效和重点视觉片段。

负责：

- hook frame
- 数据卡
- kinetic captions
- 过渡动画
- website demo focus
- meme-style 背景
- 封面或标题帧设计

输出通常是：

```text
plan/motion-plan.md
```

### `audio-director`

负责音乐和音效策略。

负责：

- BGM 风格
- 音乐节奏
- ducking
- 人声优先级
- SFX 出现位置
- loop point
- 淡入淡出

输出通常是：

```text
plan/audio-plan.md
```

### `remotion-assembler`

负责把前面所有计划实现为 Remotion 代码。

核心结构：

- `Composition`
- `Scene`
- `Sequence`
- `editPlan`
- `CaptionLayer`
- `AudioLayer`

使用时应同时参考 Remotion 官方 best practices skill。

### `remotion-gotchas-index`

负责 Remotion 调试。

适用场景：

- 预览空白
- 素材路径错误
- 字幕错位
- 音频不同步
- render 报错
- frame math 错误
- staticFile 路径问题

原则：窄修复，不大改。

### `platform-packaging`

负责发布包装。

负责：

- 标题
- 描述
- timestamps
- hashtags
- 缩略图 / 封面建议
- 导出设置
- QA notes

输出通常是：

```text
exports/packaging.md
```

### `video-prompt-lab`

负责持续优化整套系统。

负责：

- 测试主 prompt
- 记录失败点
- 优化 workflow
- 修订 skills
- 将第一次成功全流程沉淀为 Baseline v1

输出通常是：

```text
workflow/prompt-iteration-log.md
```

## 如何开始一次视频创作

最推荐的方式是先给 Codex 一个明确需求，而不是只扔素材。

可以使用这个模板：

```text
我要做一个视频：

主题：
平台：
目标时长：
画幅：
语言：
风格：
受众：
已有素材：
必须保留：
必须删掉：
想要的效果：
参考视频/链接：
```

如果你已经有原始视频、图片、音乐或文案，可以一起放入 `assets/`，然后在需求里说明它们的用途。

## 推荐执行流程

### 1. 使用主流程 prompt

打开：

```text
prompts/master-codex-video-production.md
```

复制里面的 prompt，填入你的具体视频需求，然后发给 Codex。

Codex 应该按以下顺序执行：

1. 调用 `video-workflow-router`
2. 生成 `plan/creative-brief.md`
3. 调用 `voiceover-editor`
4. 生成 `plan/script.md`
5. 调用 `asset-gathering`
6. 生成 `plan/asset-list.md`
7. 调用 `asset-usage-planner`
8. 生成 `plan/timeline.md`
9. 调用 `motion-fragments`
10. 生成 `plan/motion-plan.md`
11. 调用 `audio-director`
12. 生成 `plan/audio-plan.md`
13. 调用 `remotion-assembler`
14. 进入 Remotion 实现
15. 调用 `remotion-gotchas-index` 做 QA
16. 调用 `platform-packaging`
17. 生成导出和发布资料

### 2. 单层重跑

如果某一层不满意，不要从头来。

打开：

```text
prompts/layer-rerun-prompts.md
```

选择对应层级的 prompt。

例如只重写口播：

```text
Use voiceover-editor to rewrite plan/script.md for stronger spoken pacing.
Preserve the core message, split beats clearly, estimate timing, and mark visual needs.
Do not download assets or edit Remotion code.
```

例如只重新规划素材拼接：

```text
Use asset-usage-planner to map the current assets to script beats.
Produce plan/timeline.md with scenes, timing, asset IDs, visual roles, on-screen text, and gaps.
Do not download new assets.
```

### 3. 制作后复盘

每次完整制作或失败尝试后，使用：

```text
prompts/retrospective-prompt.md
```

让 Codex 更新：

```text
workflow/prompt-iteration-log.md
```

复盘重点：

- 哪个 skill 选错了
- 哪一层输出太虚
- 素材来源是否清楚
- 音乐和 SFX 是否记录完整
- Remotion 结构是否清晰
- 哪句 prompt 应该修改
- 哪个 skill 应该补规则

## 安装 / 复制 Skills

仓库里的 `skills/` 是项目副本。若要让 Codex 在本机自动加载这些 skills，需要把它们复制到 Codex 的 skills 目录。

Windows PowerShell 示例：

```powershell
$repoSkills = "E:\OneDrive - The University of Sydney (Students)\文档\AI视频自动剪辑\skills"
$codexSkills = "$env:USERPROFILE\.codex\skills"
Copy-Item "$repoSkills\*" $codexSkills -Recurse -Force
```

复制后重启 Codex。

## GitHub CLI

本项目已推送到 GitHub：

```text
https://github.com/RyanJieZhang/AI-video-auto-editing
```

如果需要在本机继续管理仓库，推荐安装 GitHub CLI：

```powershell
winget install --id GitHub.cli
```

登录：

```powershell
gh auth login
```

检查：

```powershell
gh auth status
```

常用 Git 命令：

```powershell
git status
git add .
git commit -m "Update workflow"
git push
```

## Remotion 工作方式

本仓库目前主要保存 workflow、prompts 和 skills。真正开始视频制作后，Remotion 项目会在当前仓库中进一步生成。

推荐结构：

```text
src/
├── Root.tsx
├── compositions/
├── scenes/
├── components/
├── data/
│   └── editPlan.ts
└── layers/
    ├── CaptionLayer.tsx
    └── AudioLayer.tsx
```

Remotion 实现原则：

- `Composition` 负责入口、尺寸、FPS、总时长
- `Scene` 负责语义段落
- `Sequence` 负责时间摆放
- `editPlan` 负责把脚本、素材、时间线结构化
- `CaptionLayer` 负责字幕
- `AudioLayer` 负责 BGM、SFX、人声策略

## 当前状态

- [x] 创建 8 层视频创作工作流
- [x] 创建 10 个自定义 Codex Skills
- [x] 创建主流程 prompt
- [x] 创建单层重跑 prompt
- [x] 创建复盘 prompt
- [x] 创建 prompt iteration log
- [x] 上传到 GitHub
- [ ] 跑通第一次完整视频制作
- [ ] 标记 Baseline v1
- [ ] 继续根据真实制作结果优化 skills

## 下一步建议

1. 选择一个具体视频主题。
2. 使用 `prompts/master-codex-video-production.md` 发起第一次完整制作。
3. 跑到 Remotion 预览或导出。
4. 使用 `prompts/retrospective-prompt.md` 复盘。
5. 更新 prompts、workflow 或 skills。
6. 第一次成功后，将该版本标记为 Baseline v1。

## License

目前未指定 license。正式公开复用前，建议补充一个许可证，例如 MIT、Apache-2.0 或私有使用说明。
