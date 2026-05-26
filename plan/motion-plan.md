# Motion Plan

| Fragment | Scene/Beat | Purpose | Visual Design | Motion | Inputs | Remotion Notes |
| --- | --- | --- | --- | --- | --- | --- |
| HookWarningCard | S01/B1 | Stop-scroll hook | Large warning title, orange accent, dark text | Scale-in title, pulsing warning line | Script beat 1 | Use interpolate + spring |
| ProductionLineReveal | S02/B2 | Reframe the problem | Horizontal production stages flowing upward in vertical layout | Dots move from planning to export | Beat 2 | SVG-like CSS divs in Remotion |
| ChaosStack | S03/B3 | Show failure of one prompt | Cards labeled script/assets/music/code overlap | Cards jitter and collide, then freeze | Beat 3 | Use per-card frame offsets |
| FailureCards | S04/B4 | Make risks scannable | Four cards: no source, timeline drift, loud music, hardcoded code | Cards pop one by one | Beat 4 | Stable 2x2 grid |
| AgentLayerStack | S05/B5 | Present solution | 10-layer vertical stack with blue/orange numbering | Layer cards cascade in | Beat 5 | Reuse layer data |
| ArtifactHandoff | S06/B6 | Explain handoff | File cards move from one layer to next | Downward handoff animation | Beat 6 | Use Sequence per artifact |
| BoundaryComparison | S07/B7 | Clarify responsibilities | Left: asset gathering, Right: timeline planning | Divider line sweeps in | Beat 7 | High contrast columns |
| RemotionArchitecture | S08/B8 | Show implementation model | Composition contains Scenes, Scenes contain Sequences | Nested boxes draw in | Beat 8 | Code-like labels |
| QALoop | S09/B9 | Show continuous improvement | QA and Prompt Lab connected in loop | Loop arrow rotates subtly | Beat 9 | No CSS animation; frame-based transform |
| ClosingSlogan | S10/B10 | Memorable ending | Bold slogan and project name | Text reveal + progress bar completes | Beat 10 | End on stable frame |
