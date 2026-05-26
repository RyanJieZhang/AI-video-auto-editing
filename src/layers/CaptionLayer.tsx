import {AbsoluteFill, useCurrentFrame} from 'remotion';
import type {ScenePlan} from '../data/editPlan';

export const CaptionLayer = ({scenes}: {scenes: ScenePlan[]}) => {
  const frame = useCurrentFrame();
  const scene = scenes.find((item) => frame >= item.from && frame < item.from + item.duration);

  if (!scene) {
    return null;
  }

  return (
    <AbsoluteFill
      style={{
        justifyContent: 'flex-end',
        alignItems: 'center',
        padding: '0 78px 128px',
        pointerEvents: 'none',
      }}
    >
      <div
        style={{
          width: '100%',
          minHeight: 132,
          borderRadius: 28,
          background: 'rgba(23, 32, 51, 0.88)',
          color: '#fff',
          padding: '26px 30px',
          fontSize: 34,
          lineHeight: 1.35,
          fontWeight: 800,
          fontFamily:
            'Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif',
          letterSpacing: 0,
        }}
      >
        {scene.narration}
      </div>
    </AbsoluteFill>
  );
};
