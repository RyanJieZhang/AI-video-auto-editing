import type {CSSProperties} from 'react';
import {Easing, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import type {ScenePlan} from '../data/editPlan';

type Props = {
  scene: ScenePlan;
  index: number;
  total: number;
};

const palette = {
  blue: '#155bd5',
  orange: '#ff6a00',
  green: '#1f8a5b',
};

const baseText: CSSProperties = {
  fontFamily:
    'Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif',
  letterSpacing: 0,
};

export const SceneRenderer = ({scene, index, total}: Props) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const accent = palette[scene.accent];
  const enter = interpolate(frame, [0, fps * 0.8], [40, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });
  const opacity = interpolate(frame, [0, fps * 0.5], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        ...baseText,
        width: '100%',
        height: '100%',
        padding: 78,
        color: '#172033',
        background:
          scene.accent === 'orange'
            ? 'linear-gradient(180deg, #fff7ef 0%, #f7fbff 72%)'
            : 'linear-gradient(180deg, #f7fbff 0%, #eef4ff 72%)',
        position: 'relative',
        overflow: 'hidden',
      }}
    >
      <div
        style={{
          position: 'absolute',
          right: -180,
          top: -160,
          width: 520,
          height: 520,
          borderRadius: 999,
          background: `${accent}22`,
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: -160,
          bottom: 120,
          width: 360,
          height: 360,
          borderRadius: 999,
          background: '#155bd512',
        }}
      />

      <div
        style={{
          transform: `translateY(${enter}px)`,
          opacity,
          position: 'relative',
          zIndex: 2,
        }}
      >
        <div style={{fontSize: 34, fontWeight: 800, color: accent}}>
          {String(index + 1).padStart(2, '0')} / {String(total).padStart(2, '0')}
        </div>
        <h1
          style={{
            margin: '26px 0 0',
            fontSize: scene.kind === 'closing' ? 88 : 76,
            lineHeight: 1.08,
            fontWeight: 900,
            maxWidth: 890,
          }}
        >
          {scene.title}
        </h1>
        <p
          style={{
            margin: '24px 0 0',
            fontSize: 38,
            lineHeight: 1.3,
            color: '#46546a',
            fontWeight: 700,
            maxWidth: 860,
          }}
        >
          {scene.subtitle}
        </p>
      </div>

      <Visual scene={scene} frame={frame} accent={accent} />
    </div>
  );
};

const Visual = ({scene, frame, accent}: {scene: ScenePlan; frame: number; accent: string}) => {
  if (scene.kind === 'chaos') {
    return <ChaosCards items={scene.bullets ?? []} frame={frame} accent={accent} />;
  }
  if (scene.kind === 'failures') {
    return <FailureGrid items={scene.bullets ?? []} frame={frame} accent={accent} />;
  }
  if (scene.kind === 'layers') {
    return <LayerStack items={scene.bullets ?? []} frame={frame} accent={accent} />;
  }
  if (scene.kind === 'handoff') {
    return <FileHandoff items={scene.bullets ?? []} frame={frame} accent={accent} />;
  }
  if (scene.kind === 'boundary') {
    return <BoundaryCards items={scene.bullets ?? []} accent={accent} />;
  }
  if (scene.kind === 'architecture') {
    return <Architecture items={scene.bullets ?? []} accent={accent} />;
  }
  if (scene.kind === 'loop') {
    return <LoopCards items={scene.bullets ?? []} accent={accent} />;
  }
  return <HeroShape accent={accent} />;
};

const HeroShape = ({accent}: {accent: string}) => (
  <div
    style={{
      position: 'absolute',
      left: 78,
      right: 78,
      bottom: 300,
      height: 280,
      borderRadius: 28,
      background: '#ffffff',
      border: '4px solid #dbe6f7',
      boxShadow: '0 28px 80px rgba(23,32,51,0.16)',
      display: 'grid',
      placeItems: 'center',
      color: accent,
      fontSize: 54,
      fontWeight: 900,
    }}
  >
    VIDEO PRODUCTION LINE
  </div>
);

const ChaosCards = ({items, frame, accent}: {items: string[]; frame: number; accent: string}) => (
  <div style={{position: 'absolute', left: 90, right: 90, bottom: 280, height: 430}}>
    {items.map((item, i) => {
      const y = interpolate(frame, [i * 5, i * 5 + 18], [180, i * 62], {
        extrapolateLeft: 'clamp',
        extrapolateRight: 'clamp',
      });
      const rotate = (i - 2) * 5;
      return (
        <div
          key={item}
          style={{
            position: 'absolute',
            left: 60 + i * 44,
            top: y,
            width: 620,
            height: 86,
            borderRadius: 20,
            border: `4px solid ${accent}`,
            background: '#fff',
            transform: `rotate(${rotate}deg)`,
            display: 'grid',
            placeItems: 'center',
            fontSize: 38,
            fontWeight: 900,
            boxShadow: '0 20px 48px rgba(23,32,51,0.14)',
          }}
        >
          {item}
        </div>
      );
    })}
  </div>
);

const FailureGrid = ({items, frame, accent}: {items: string[]; frame: number; accent: string}) => (
  <div
    style={{
      position: 'absolute',
      left: 78,
      right: 78,
      bottom: 260,
      display: 'grid',
      gridTemplateColumns: '1fr 1fr',
      gap: 22,
    }}
  >
    {items.map((item, i) => {
      const scale = interpolate(frame, [i * 8, i * 8 + 12], [0.86, 1], {
        extrapolateLeft: 'clamp',
        extrapolateRight: 'clamp',
      });
      return (
        <div
          key={item}
          style={{
            height: 150,
            borderRadius: 24,
            background: '#fff',
            border: '3px solid #dbe6f7',
            boxShadow: '0 18px 42px rgba(23,32,51,0.12)',
            display: 'grid',
            placeItems: 'center',
            color: i === 0 ? accent : '#172033',
            fontSize: 34,
            fontWeight: 900,
            transform: `scale(${scale})`,
          }}
        >
          {item}
        </div>
      );
    })}
  </div>
);

const LayerStack = ({items, frame, accent}: {items: string[]; frame: number; accent: string}) => (
  <div style={{position: 'absolute', left: 78, right: 78, bottom: 180}}>
    {items.map((item, i) => {
      const x = interpolate(frame, [i * 3, i * 3 + 12], [80, 0], {
        extrapolateLeft: 'clamp',
        extrapolateRight: 'clamp',
      });
      return (
        <div
          key={item}
          style={{
            height: 64,
            marginBottom: 10,
            borderRadius: 18,
            background: '#fff',
            border: '3px solid #dbe6f7',
            display: 'flex',
            alignItems: 'center',
            gap: 18,
            padding: '0 22px',
            transform: `translateX(${x}px)`,
          }}
        >
          <b style={{color: accent, fontSize: 28}}>{i + 1}</b>
          <span style={{fontSize: 28, fontWeight: 800}}>{item}</span>
        </div>
      );
    })}
  </div>
);

const FileHandoff = ({items, frame, accent}: {items: string[]; frame: number; accent: string}) => (
  <div style={{position: 'absolute', left: 78, right: 78, bottom: 260}}>
    {items.map((item, i) => {
      const y = interpolate(frame, [i * 10, i * 10 + 18], [40, 0], {
        extrapolateLeft: 'clamp',
        extrapolateRight: 'clamp',
      });
      return (
        <div
          key={item}
          style={{
            height: 86,
            marginBottom: 18,
            borderRadius: 18,
            background: '#fff',
            borderLeft: `12px solid ${accent}`,
            boxShadow: '0 16px 36px rgba(23,32,51,0.12)',
            padding: '22px 26px',
            fontSize: 30,
            fontWeight: 900,
            transform: `translateY(${y}px)`,
          }}
        >
          {item}
        </div>
      );
    })}
  </div>
);

const BoundaryCards = ({items, accent}: {items: string[]; accent: string}) => (
  <div
    style={{
      position: 'absolute',
      left: 78,
      right: 78,
      bottom: 300,
      display: 'grid',
      gridTemplateColumns: '1fr 1fr',
      gap: 24,
    }}
  >
    {items.map((item, i) => (
      <div
        key={item}
        style={{
          height: 280,
          borderRadius: 28,
          padding: 32,
          background: '#fff',
          border: `4px solid ${i === 0 ? accent : '#dbe6f7'}`,
          boxShadow: '0 20px 48px rgba(23,32,51,0.14)',
        }}
      >
        <div style={{fontSize: 32, fontWeight: 900, color: i === 0 ? accent : '#172033'}}>
          {item}
        </div>
        <div style={{marginTop: 36, fontSize: 28, color: '#5b6578', lineHeight: 1.35}}>
          {i === 0 ? '找 / 生成 / 验证 / 记录来源' : '分配 / 对齐 / 去重 / 建时间线'}
        </div>
      </div>
    ))}
  </div>
);

const Architecture = ({items, accent}: {items: string[]; accent: string}) => (
  <div style={{position: 'absolute', left: 78, right: 78, bottom: 230}}>
    {items.map((item, i) => (
      <div
        key={item}
        style={{
          marginLeft: i * 42,
          marginBottom: 14,
          width: 850 - i * 56,
          height: 74,
          borderRadius: 16,
          background: i === 0 ? accent : '#fff',
          color: i === 0 ? '#fff' : '#172033',
          border: '3px solid #dbe6f7',
          display: 'grid',
          placeItems: 'center',
          fontSize: 30,
          fontWeight: 900,
          fontFamily: 'ui-monospace, SFMono-Regular, Consolas, monospace',
        }}
      >
        {item}
      </div>
    ))}
  </div>
);

const LoopCards = ({items, accent}: {items: string[]; accent: string}) => (
  <div style={{position: 'absolute', left: 98, right: 98, bottom: 320, height: 320}}>
    {items.map((item, i) => (
      <div
        key={item}
        style={{
          position: 'absolute',
          left: i === 1 ? 290 : i === 2 ? 540 : 40,
          top: i === 1 ? 130 : 20,
          width: 330,
          height: 130,
          borderRadius: 24,
          background: i === 1 ? accent : '#fff',
          color: i === 1 ? '#fff' : '#172033',
          border: '3px solid #dbe6f7',
          display: 'grid',
          placeItems: 'center',
          fontSize: 30,
          fontWeight: 900,
          boxShadow: '0 18px 42px rgba(23,32,51,0.12)',
        }}
      >
        {item}
      </div>
    ))}
  </div>
);
