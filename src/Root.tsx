import {Composition} from 'remotion';
import {AgentWorkflowVideo} from './compositions/AgentWorkflowVideo';
import {DURATION_FRAMES, FPS, VIDEO_HEIGHT, VIDEO_WIDTH} from './data/editPlan';

export const RemotionRoot = () => {
  return (
    <Composition
      id="AgentWorkflowVideo"
      component={AgentWorkflowVideo}
      durationInFrames={DURATION_FRAMES}
      fps={FPS}
      width={VIDEO_WIDTH}
      height={VIDEO_HEIGHT}
    />
  );
};
