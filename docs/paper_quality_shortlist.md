# Continuous VLN / VLN-CE 高质量论文短名单

## 用途

这是项目内部使用的“高质量论文优先级表”，不等同于对外交付的最全列表。

用途：

- 决定优先精读哪些论文
- 决定优先复现哪些 codebase / baseline
- 决定哪些工作更可能为后续方法设计提供直接启发

## 评分说明

分数是内部启发式评分，不是客观事实。用于排序，不用于对外声称。

### 评分维度

每篇论文满分 35：

- 任务直接相关性：0-5
- benchmark 可比性：0-5
- 时间新颖性：0-5
- 影响力与后续继承价值：0-5
- 结果强度：0-5
- 生态与复现性：0-5
- 方法 solid 程度：0-5

### 等级

- `A+`：31-35
- `A`：27-30
- `B+`：23-26

## 排名表

| 排名 | 等级 | 总分 | 论文 | 主要 benchmark / 设定 | 优先用途 | 为什么优先 |
|---:|---|---:|---|---|---|---|
| 1 | A+ | 34 | ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments | R2R-CE / RxR-CE | baseline / codebase / topo planning | continuous VLN topo 路线代表作，问题定义清楚、工程细节扎实、可直接影响后续方法设计 |
| 2 | A+ | 34 | Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation | VLN benchmarks with continuous relevance | high-level architecture | 双系统结构非常贴近“高层理解-低层控制接口缺口”这个核心问题 |
| 3 | A+ | 33 | StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling | VLN-CE benchmarks | history / deployment / streaming | history compression 和在线推理都直接相关，且足够新 |
| 4 | A+ | 33 | DAgger Diffusion Navigation: DAgger Boosted Diffusion Policy for Vision-Language Navigation | VLN-CE benchmarks | low-level action expert / diffusion baseline | 是 diffusion direct-hit 关键工作，和你后续低层动作建模最贴近 |
| 5 | A+ | 33 | Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments | R2R-CE / RxR-CE | zero-shot / progress / subgoal | constraint + sub-instruction + progress 结构非常值得精读 |
| 6 | A+ | 32 | CLASH: Collaborative Large-Small Hierarchical Framework for Continuous Vision-and-Language Navigation | VLN-CE leaderboard | current SOTA / hierarchical collaboration | 代表最新大模型+小模型协作路线，具备很强现实参考价值 |
| 7 | A | 30 | NavForesee: A Unified Vision-Language World Model for Hierarchical Planning and Dual-Horizon Navigation Prediction | R2R-CE / RxR-CE | world model / hierarchical planning | 高层规划与局部预测统一建模，方法完整度高 |
| 8 | A | 30 | ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-Language Navigation in Continuous Environments | VLN-CE | topo follow-up / RFT | topo 路线后续强化版本，能帮助判断 topo 是否仍是强主线 |
| 9 | A | 30 | NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation | VLN-CE | history backbone / planner | video-based history 是非常关键的上层感知与规划参考 |
| 10 | A | 29 | DREAMWALKER: Mental Planning for Continuous Vision-Language Navigation | VLN-CE | planning / world model | early but strong 的 planning 路线代表作 |
| 11 | A | 29 | Open-Nav: Exploring Zero-Shot Vision-and-Language Navigation in Continuous Environment with Open-Source LLMs | VLN-CE / real-world | zero-shot reasoning scaffold | open-source LLM + progress estimation + CoT，适合借高层推理结构 |
| 12 | A | 29 | Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments | VLN-CE / R2R-CE / RxR-CE | task origin / benchmark understanding | continuous VLN 起点，必须优先掌握 |
| 13 | A | 28 | Cross-modal Map Learning for Vision and Language Navigation | VLN-CE | map baseline / explicit representation | 显式空间表示和 waypoint 设计的早期 solid work |
| 14 | A | 28 | 1st Place Solutions for RxR-Habitat Vision-and-Language Navigation Competition | RxR-Habitat / VLN-CE | competition baseline / engineering | challenge 冠军方案，对工程与训练 recipe 很重要 |
| 15 | A | 28 | Dynamic Topology Awareness: Breaking the Granularity Rigidity in Vision-Language Navigation | R2R-CE / RxR-CE | topo granularity | 非常新，且直接针对 topo 粒度刚性问题 |
| 16 | A | 28 | Let's Reward Step-by-Step: Step-Aware Contrastive Alignment for Vision-Language Navigation in Continuous Environments | VLN-CE | reward shaping / credit assignment | 对长程训练 credit assignment 很关键 |
| 17 | A | 28 | NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments | VLN-CE | world model / memory | self-evolving world model 很新，值得观察是否真有效 |
| 18 | B+ | 26 | Safe-VLN: Collision Avoidance for Vision-and-Language Navigation of Autonomous Robots Operating in Continuous Environments | R2R-CE | obstacle avoidance / recovery | 把碰撞与恢复明确当成主问题，非常契合你的判断 |
| 19 | B+ | 26 | GridMM: Grid Memory Map for Vision-and-Language Navigation | R2R-CE | memory / map | memory-map 路线代表，适合借 history 结构 |
| 20 | B+ | 26 | VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning | VLN-CE | RFT / LVLM | RFT 用在 continuous VLN 上，方向值得关注 |
| 21 | B+ | 25 | SpatialNav: Leveraging Spatial Scene Graphs for Zero-Shot Vision-and-Language Navigation | R2R-CE / RxR-CE | scene graph / zero-shot | 2026 新工作，scene-graph 路线值得保留 |
| 22 | B+ | 25 | monoVLN: Bridging the Observation Gap between Monocular and Panoramic Vision and Language Navigation | R2R-CE / RxR-CE | monocular gap | 单目观测缺口问题对真实部署有价值 |
| 23 | B+ | 24 | RoomTour3D: Geometry-Aware Video-Instruction Tuning for Embodied Navigation | RoomTour3D | data / pretraining | 数据与 video-instruction 资源可能对后续训练帮助很大 |
| 24 | B+ | 24 | HA-VLN: A Benchmark for Human-Aware Navigation in Discrete–Continuous Environments with Dynamic Multi-Human Interactions | HA-VLN | dynamic humans benchmark | 如果后续考虑真实障碍和动态体，这条线很重要 |
| 25 | B+ | 23 | HiMemVLN: Enhancing Reliability of Open-Source Zero-Shot Vision-and-Language Navigation with Hierarchical Memory System | simulated + real-world VLN | memory / zero-shot reliability | 最新 memory/reliability 路线，值得快速扫读 |

## 复现建议分组

### 第一优先：最值得做 baseline / code reconnaissance

1. ETPNav
2. DAgger Diffusion Navigation
3. StreamVLN
4. Constraint-Aware Zero-Shot VLN-CE
5. DualVLN

### 第二优先：最值得做高层结构参考

1. NaVid
2. Open-Nav
3. NavForesee
4. DREAMWALKER
5. SpatialNav

### 第三优先：最值得补训练范式和 benchmark 认知

1. VLN-R1
2. Step-Aware Contrastive Alignment
3. RxR-Habitat Competition Winner
4. HA-VLN
5. RoomTour3D

## 说明

1. 这是当前阶段的内部排序，不是最终定论。
2. 如果后续发现代码不可用、结果不可比、生态差，排序应动态调整。
