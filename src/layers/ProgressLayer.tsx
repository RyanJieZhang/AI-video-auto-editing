import {AbsoluteFill, useCurrentFrame} from 'remotion';
import type {ScenePlan} from '../data/editPlan';
import {DURATION_FRAMES} from '../data/editPlan';

export const ProgressLayer = ({scenes}: {scenes: ScenePlan[]}) => {
  const frame = useCurrentFrame();
  const width = `${Math.min(100, (frame / DURATION_FRAMES) * 100)}%`;
  const sceneIndex = scenes.findIndex((item) => frame >= item.from && frame < item.from + item.duration);

  return (
    <AbsoluteFill style={{pointerEvents: 'none'}}>
      <div
        style={{
          position: 'absolute',
          left: 78,
          right: 78,
          top: 52,
          height: 14,
          borderRadius: 999,
          background: '#dbe6f7',
          overflow: 'hidden',
        }}
      >
        <div style={{width, height: '100%', borderRadius: 999, background: '#155bd5'}} />
      </div>
      <div
        style={{
          position: 'absolute',
          right: 78,
          top: 82,
          fontSize: 24,
          fontWeight: 900,
          color: '#5b6578',
          fontFamily: 'ui-monospace, SFMono-Regular, Consolas, monospace',
        }}
      >
        scene {Math.max(1, sceneIndex + 1)} / {scenes.length}
      </div>
    </AbsoluteFill>
  );
};
