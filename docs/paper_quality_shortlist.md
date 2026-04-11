# Continuous VLN / VLN-CE 高质量论文优先级表（飞书可直接粘贴）

说明：

- 这是内部维护的高质量优先级表，不等同于“最全列表”。
- 排序依据是当前的综合启发式判断，不是客观排名。
- 核心硬指标：
  - 与 `R2R-CE / RxR-CE / VLN-CE` 的直接相关性
  - benchmark 可比性
  - 首发时间新颖性
  - 赛道影响力与后续继承价值
  - 结果强度
  - 生态完整度（代码 / 项目页 / 数据 / challenge 关联）
  - 方法完整度与可借鉴性
- 排名越靠前，越值得优先精读、优先复现、优先作为方法灵感来源。

## 第一部分：Top 25 排名

| 排名 | 论文 | 首发日期 | 当前形态 | 优先用途 | 为什么优先 |
|---:|---|---|---|---|---|
| 1 | ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments | 2023-04-06 | arXiv / 后续期刊线索已存在但本表不展开 | baseline / codebase / topo planning | continuous VLN topo 路线代表作，问题定义清晰，工程实现扎实，直接影响后续方法设计 |
| 2 | Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation | 2025-12-09 | arXiv | 高层架构参考 | 双系统结构直接命中“高层语义-低层控制接口缺口”这个核心问题 |
| 3 | StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling | 2025-07-07 | arXiv | history / streaming / deployment | history compression 与在线推理直接相关，而且足够新 |
| 4 | DAgger Diffusion Navigation: DAgger Boosted Diffusion Policy for Vision-Language Navigation | 2025-08-13 | arXiv | 低层动作专家 / diffusion baseline | diffusion 在 continuous VLN 的 direct-hit 关键工作，和低层连续控制最贴近 |
| 5 | Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments | 2024-12-13 | arXiv | zero-shot / progress / subgoal | constraint + sub-instruction + progress 结构非常值得精读 |
| 6 | CLASH: Collaborative Large-Small Hierarchical Framework for Continuous Vision-and-Language Navigation | 2025-12-11 | arXiv | current SOTA / hierarchical collaboration | 代表最新大模型+小模型协作路线，现实参考价值很强 |
| 7 | NavForesee: A Unified Vision-Language World Model for Hierarchical Planning and Dual-Horizon Navigation Prediction | 2025-12-01 | arXiv | world model / hierarchical planning | 高层规划与局部预测统一建模，方法闭环完整 |
| 8 | ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-and-Language Navigation in Continuous Environments | 2025-12-24 | arXiv | topo follow-up / RFT | topo 路线强化版本，适合判断 topo 是否仍是强主线 |
| 9 | NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation | 2024-02-24 | arXiv | history backbone / planner | video-based history 是非常关键的上层感知与规划参考 |
| 10 | DREAMWALKER: Mental Planning for Continuous Vision-and-Language Navigation | 2023-08-14 | ICCV 2023 + arXiv | planning / world model | 早期但很强的 planning / world-model 路线代表作 |
| 11 | Open-Nav: Exploring Zero-Shot Vision-and-Language Navigation in Continuous Environment with Open-Source LLMs | 2024-09-27 | arXiv | zero-shot reasoning scaffold | open-source LLM + progress estimation + CoT，适合借高层推理结构 |
| 12 | Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments | 2020-04-06 | ECCV 2020 + arXiv | task origin / benchmark understanding | continuous VLN 起点，必须优先掌握 |
| 13 | Cross-modal Map Learning for Vision and Language Navigation | 2022-03-10 | CVPR 2022 + arXiv | map baseline / explicit representation | 显式空间表示和 waypoint 设计的早期 solid work |
| 14 | 1st Place Solutions for RxR-Habitat Vision-and-Language Navigation Competition (CVPR 2022) | 2022-06-23 | arXiv / challenge report | competition baseline / engineering | challenge 冠军方案，对工程细节与训练 recipe 很重要 |
| 15 | Dynamic Topology Awareness: Breaking the Granularity Rigidity in Vision-Language Navigation | 2026-01-29 | arXiv | topo granularity | 非常新，且直接针对 topo 粒度刚性问题 |
| 16 | Let's Reward Step-by-Step: Step-Aware Contrastive Alignment for Vision-Language Navigation in Continuous Environments | 2026-03-10 | arXiv | reward shaping / credit assignment | 对长程训练中的 credit assignment 很关键 |
| 17 | NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments | 2025-06-30 | arXiv | world model / memory | self-evolving world model 很新，值得重点观察真实性能收益 |
| 18 | GC-VLN: Instruction as Graph Constraints for Training-free Vision-and-Language Navigation | 2025-09-12 | CoRL 2025 + arXiv | training-free / graph constraints | 在 continuous VLN 上把图约束做成 training-free 框架，结构性很强 |
| 19 | SpatialNav: Leveraging Spatial Scene Graphs for Zero-Shot Vision-and-Language Navigation | 2026-01-11 | arXiv | scene graph / zero-shot | 2026 新工作，scene-graph 路线值得重点保留 |
| 20 | VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning | 2025-06-20 | arXiv | RFT / LVLM | RFT 用在 continuous VLN 上，方向值得持续跟踪 |
| 21 | Safe-VLN: Collision Avoidance for Vision-and-Language Navigation of Autonomous Robots Operating in Continuous Environments | 2023-11-06 | arXiv | obstacle avoidance / recovery | 明确把碰撞与恢复当主问题，非常契合 continuous VLN 痛点 |
| 22 | GridMM: Grid Memory Map for Vision-and-Language Navigation | 2023-07-24 | arXiv | memory / map | memory-map 路线代表作，适合借 history 结构 |
| 23 | Sim-2-Sim Transfer for Vision-and-Language Navigation in Continuous Environments | 2022-04-20 | ECCV 2022 + arXiv | transfer / benchmark cognition | 解释离散到连续性能鸿沟的重要工作 |
| 24 | Cog-GA: A Large Language Models-based Generative Agent for Vision-Language Navigation in Continuous Environments | 2024-09-04 | arXiv | LLM agent / waypoint planning | 高层 agent 化 continuous VLN 的代表之一 |
| 25 | Mind the Error! Detection and Localization of Instruction Errors in Vision-and-Language Navigation | 2024-03-15 | IROS 2024 + arXiv | robustness / benchmark extension | instruction error robustness 是很值得保留的支线问题 |

## 第二部分：建议的精读 / 复现优先级

### A. 第一优先：最值得先做 baseline reconnaissance

1. ETPNav
2. DAgger Diffusion Navigation
3. StreamVLN
4. Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments
5. 1st Place Solutions for RxR-Habitat Vision-and-Language Navigation Competition (CVPR 2022)

### B. 第二优先：最值得做高层结构参考

1. Ground Slow, Move Fast
2. NavForesee
3. NaVid
4. DREAMWALKER
5. Open-Nav

### C. 第三优先：最值得补 topo / memory / robustness

1. Dynamic Topology Awareness
2. ETP-R1
3. GC-VLN
4. Safe-VLN
5. GridMM
6. Mind the Error!

## 第三部分：当前不放进第一优先复现队列，但仍应持续跟踪

1. EmergeNav
2. HiMemVLN
3. SeqWalker
4. IndoorUAV
5. MonoDream
6. HA-VLN
7. Ground-level Viewpoint Vision-and-Language Navigation in Continuous Environments
8. TRAVEL
9. Human-Aware Vision-and-Language Navigation: Bridging Simulation to Reality with Dynamic Human Interactions
10. Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation

## 第四部分：本轮明确从 shortlist 降级到内部候补池的条目

1. RoomTour3D
原因：更适合作为数据和 pretraining 资源补充，不再放在 strict continuous-VLN 核心优先级表中。

2. monoVLN
原因：单目设定很重要，但当前对主 benchmark 主线的直接牵引力弱于 topo / streaming / zero-shot / world-model 主线。

3. NaviLLM
原因：属于更广义 embodied navigation foundation model，不再放进 strict continuous-VLN 高优先级表。
