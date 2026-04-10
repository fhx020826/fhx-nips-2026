# Continuous VLN / VLN-CE 高质量论文短名单

## 用途

这个文件不直接作为最终交付给用户的“全量论文列表”，而是项目内部使用的质量分层与优先级记录。

目标：

- 在“全量相关论文 > 100 篇”的基础上
- 额外筛出约 25 篇高质量论文
- 用于后续优先粗读、方法归纳、codebase 侦察和 idea 提炼

## 高质量判断标准

满足越多越优先：

1. 任务直接相关，尤其是 `R2R-CE / RxR-CE / VLN-CE`
2. 当时 SOTA / leaderboard 靠前 / challenge 冠军
3. 顶会顶刊录用，或至少是高可信度的 solid work
4. 被后续工作频繁继承、引用或对比
5. 生态好：项目页 / 代码 / 可复现性 / 社区讨论较好
6. 新且重要：2025–2026 即使引用低，也可因新颖和任务相关性被高优先级保留

## 硬性打分模板

后续每篇论文按以下维度给内部评分，便于模式化筛选：

| 维度 | 分值 | 说明 |
|---|---:|---|
| 任务直接相关性 | 0-5 | 是否直接解决 continuous VLN / VLN-CE |
| benchmark 可比性 | 0-5 | 是否在 R2R-CE / RxR-CE / VLN-CE 或强相关设定上验证 |
| 时间新颖性 | 0-5 | 越新且越重要，分越高 |
| 影响力 | 0-5 | 引用量、社区讨论度、后续继承情况 |
| 结果强度 | 0-5 | 是否 SOTA / challenge 冠军 / leaderboard 靠前 |
| 生态与复现性 | 0-5 | 代码、项目页、数据、实现完整度 |
| 方法 solid 程度 | 0-5 | 不是简单拼接，问题定义清晰、结构完整 |

### 质量等级建议

- `A+`: 30 分以上
- `A`: 26–29 分
- `B+`: 22–25 分
- `B`: 18–21 分
- `C`: 17 分及以下，仅保留作补充背景

## 来源优先级

1. arXiv / 官方论文页
2. 顶会/顶刊正式页面
3. Awesome-VLN README
4. Google Scholar 风格检索结果
5. 项目页 / 代码仓库

如果来源之间冲突，以更原始、更官方的来源为准。

## 当前初始短名单（会继续更新）

| 优先级 | 论文 | 年份 | 原因 |
|---|---|---:|---|
| A | Beyond the Nav-Graph | 2020 | continuous VLN 任务起点 |
| A | Cross-modal Map Learning for Vision and Language Navigation | 2022 | 早期 solid baseline，显式空间表示 |
| A | 1st Place Solutions for RxR-Habitat Vision-and-Language Navigation Competition | 2022 | challenge 冠军方案 |
| A | DREAMWALKER | 2023 | planning 路线代表作 |
| A | ETPNav | 2023/2024 | topo planning 路线代表作 |
| A | Safe-VLN | 2023 | 明确处理 collision avoidance |
| A | NaVid | 2024 | video history 路线关键工作 |
| A | Constraint-Aware Zero-Shot VLN-CE | 2024 | zero-shot + sub-instruction + constraints |
| A | Open-Nav | 2024 | open-source LLM zero-shot continuous VLN |
| A | StreamVLN | 2025 | streaming / slow-fast history 关键工作 |
| A | DAgger Diffusion Navigation | 2025 | diffusion direct-hit 关键工作 |
| A | DualVLN / Ground Slow, Move Fast | 2025 | 双系统结构关键工作 |
| A | NavForesee | 2025 | unified world model + hierarchical planning |
| A | CLASH | 2025 | 最新 leaderboard / SOTA 倾向 |
| A | ETP-R1 | 2025 | topo 路线强化后续工作 |
| B | GridMM | 2023 | memory-map 代表工作 |
| B | Lookahead Exploration with Neural Radiance Representation | 2024 | future observation / exploration 路线 |
| B | Cog-GA | 2024 | LLM agent 路线代表 |
| B | NavMorph | 2025 | self-evolving world model |
| B | SpatialNav | 2026 | scene-graph zero-shot 路线 |
| B | Dynamic Topology Awareness | 2026 | dynamic topo granularity |
| B | Step-Aware Contrastive Alignment | 2026 | reward / credit assignment 路线 |
| B | monoVLN | 2025 | monocular 观测缺口方向 |
| B | RoomTour3D | 2024 | 数据与预训练资源关键补充 |
| B | HA-VLN | 2025 | 动态人类 benchmark 扩展 |

## 说明

1. 这里的等级只是当前阶段性判断，不是最终结论。
2. 后续会在补齐 >100 篇全量列表后，重新校准这个 shortlist。
