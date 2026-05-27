# Packaging

## Render

- File: `exports/why-not-one-prompt-demo.mp4`
- Preview frame: `exports/preview-frame.png`
- Duration: 60 seconds
- Size: 720 x 1280
- FPS: 24
- Codec: H.264
- Pixel format: yuv420p
- Audio: none in MVP

## Additional Exports

- `exports/张府皇家航空宣传片2_已修改.mp4`: edited source demo with airport text changed.
- `exports/zhangfu-airline-v002-vertical.mp4`: improved 720x1280 vertical airline promo draft with "降落長沙" title, captions, framed source footage, background blur, and preserved source audio.

## Title Options

1. 为什么不要用一个万能 prompt 自动剪视频
2. AI 自动剪视频，别再迷信万能 prompt
3. 真正稳定的 AI 剪视频流程：不是一个 prompt，而是一条生产线
4. 我把自动剪视频拆成 10 个 Agent，终于不乱了

## Description

很多人想用一个万能 prompt 完成脚本、素材、音乐、剪辑、动效和代码，但视频创作其实是一条生产线。这个 demo 展示了一套更稳定的分层 Agent 工作流：规划、口播、素材、对齐、动效、音频、Remotion、QA、发布和复盘。

## Timestamps

- 0:00 万能 prompt 的问题
- 0:05 视频创作是一条生产线
- 0:10 一次做太多会互相打架
- 0:16 常见翻车点
- 0:22 分层 Agent 解法
- 0:29 每层交付一个文件
- 0:36 素材和时间线职责分离
- 0:43 Remotion 装配结构
- 0:50 QA 和 Prompt Lab 复盘
- 0:56 结论

## Thumbnail / Cover

推荐封面文案：

```text
别再用万能 prompt 剪视频
```

副标题：

```text
自动剪辑应该是一条 Agent 生产线
```

视觉建议：

- 左侧：混乱的 prompt 卡片
- 右侧：10 层 Agent 流程
- 主色：蓝色系统感 + 橙色警告感

## Hashtags / Tags

- AI视频
- 自动剪辑
- Codex
- Remotion
- AI Agent
- 工作流
- 小红书创作
- B站创作

## QA Notes

- MVP 使用生成图形，无外部版权素材。
- MVP 暂无真实配音和 BGM。
- 文字适合竖屏阅读，但后续可以进一步压缩字幕长度。
- 720p 版本适合快速演示；正式发布建议用 Remotion 渲染 1080x1920。
- 航空 v002 已经适配竖屏，但仍需要 BGM/SFX 和更干净的机场文字镜头才能进入 final。
- 每次导出后运行 `scripts/quality_gate.py`；平均分低于 8/10 时继续迭代，不标记 final。
