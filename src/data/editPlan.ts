export const FPS = 30;
export const VIDEO_WIDTH = 1080;
export const VIDEO_HEIGHT = 1920;
export const DURATION_SECONDS = 60;
export const DURATION_FRAMES = FPS * DURATION_SECONDS;

export type SceneKind =
  | 'hook'
  | 'line'
  | 'chaos'
  | 'failures'
  | 'layers'
  | 'handoff'
  | 'boundary'
  | 'architecture'
  | 'loop'
  | 'closing';

export type ScenePlan = {
  id: string;
  kind: SceneKind;
  from: number;
  duration: number;
  title: string;
  subtitle: string;
  narration: string;
  accent: 'blue' | 'orange' | 'green';
  bullets?: string[];
};

const sec = (value: number) => Math.round(value * FPS);

export const scenes: ScenePlan[] = [
  {
    id: 's01',
    kind: 'hook',
    from: sec(0),
    duration: sec(5),
    title: '一个万能 prompt？',
    subtitle: '先停一下',
    narration: '如果你想让一个 prompt 自动剪完整条视频，我先劝你停一下。',
    accent: 'orange',
  },
  {
    id: 's02',
    kind: 'line',
    from: sec(5),
    duration: sec(5),
    title: '视频创作不是一道题',
    subtitle: '它是一条生产线',
    narration: '因为视频创作不是一道题，它是一条生产线。',
    accent: 'blue',
  },
  {
    id: 's03',
    kind: 'chaos',
    from: sec(10),
    duration: sec(6),
    title: '一个 prompt 同时做所有事',
    subtitle: '很快就会互相打架',
    narration: '一个 prompt 同时写脚本、找素材、配音乐、做动效、写代码，很快就会互相打架。',
    accent: 'orange',
    bullets: ['脚本', '素材', '音乐', '动效', '代码'],
  },
  {
    id: 's04',
    kind: 'failures',
    from: sec(16),
    duration: sec(6),
    title: '最常见的翻车点',
    subtitle: '问题不是一个，而是一串',
    narration: '最常见的问题是：素材没来源，时间线错位，音乐盖住人声，代码还到处硬编码。',
    accent: 'orange',
    bullets: ['素材没来源', '时间线错位', '音乐盖人声', '代码硬编码'],
  },
  {
    id: 's05',
    kind: 'layers',
    from: sec(22),
    duration: sec(7),
    title: '更稳的方法',
    subtitle: '拆成职责清晰的 Agent',
    narration: '更稳的方式，是把它拆成多个 Agent：规划、口播、素材、对齐、动效、音频、Remotion、QA 和发布。',
    accent: 'blue',
    bullets: ['规划', '口播', '素材', '对齐', '动效', '音频', 'Remotion', 'QA', '发布', '复盘'],
  },
  {
    id: 's06',
    kind: 'handoff',
    from: sec(29),
    duration: sec(7),
    title: '每层只交付一个文件',
    subtitle: '下一层接着用',
    narration: '每一层只做自己的事，并且交付一个文件给下一层。',
    accent: 'green',
    bullets: ['creative-brief.md', 'script.md', 'asset-list.md', 'timeline.md'],
  },
  {
    id: 's07',
    kind: 'boundary',
    from: sec(36),
    duration: sec(7),
    title: '职责边界要清楚',
    subtitle: '找素材，不等于剪时间线',
    narration: '比如素材层只负责找和验证素材，不负责最终剪辑；时间线层只负责怎么拼，不负责下载。',
    accent: 'blue',
    bullets: ['Asset Gathering', 'Asset Usage Planner'],
  },
  {
    id: 's08',
    kind: 'architecture',
    from: sec(43),
    duration: sec(7),
    title: '到 Remotion 才开始装配',
    subtitle: 'Composition / Scene / Sequence',
    narration: '到 Remotion 阶段，Agent 才把脚本、素材、字幕、音频和动效装配成 Composition、Scene 和 Sequence。',
    accent: 'blue',
    bullets: ['Composition', 'Scene', 'Sequence', 'CaptionLayer', 'AudioLayer'],
  },
  {
    id: 's09',
    kind: 'loop',
    from: sec(50),
    duration: sec(6),
    title: '最后不是结束',
    subtitle: 'QA 和 Prompt Lab 会复盘',
    narration: '最后 QA 找问题，Prompt Lab 复盘，把这次经验变成下一次的流程。',
    accent: 'green',
    bullets: ['QA', 'Prompt Lab', '下一次更稳'],
  },
  {
    id: 's10',
    kind: 'closing',
    from: sec(56),
    duration: sec(4),
    title: '别追求万能 prompt',
    subtitle: '追求一条能反复成功的视频生产线',
    narration: '所以，别追求万能 prompt。追求一条能反复成功的视频生产线。',
    accent: 'orange',
  },
];
