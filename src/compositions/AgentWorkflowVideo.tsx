import {AbsoluteFill, Sequence} from 'remotion';
import {scenes} from '../data/editPlan';
import {SceneRenderer} from '../scenes/SceneRenderer';
import {CaptionLayer} from '../layers/CaptionLayer';
import {ProgressLayer} from '../layers/ProgressLayer';

export const AgentWorkflowVideo = () => {
  return (
    <AbsoluteFill style={{backgroundColor: '#f7fbff'}}>
      {scenes.map((scene, index) => (
        <Sequence key={scene.id} from={scene.from} durationInFrames={scene.duration}>
          <SceneRenderer scene={scene} index={index} total={scenes.length} />
        </Sequence>
      ))}
      <CaptionLayer scenes={scenes} />
      <ProgressLayer scenes={scenes} />
    </AbsoluteFill>
  );
};
