# 完整论文列表粗读卡片（Batch 2）

说明：
- 本批按完整列表顺序继续推进，覆盖第 `6` 到第 `10` 篇论文。
- 每篇均采用与 `P^3Nav` 相同的最终粗读模板与写作口径。
- 每篇文档都可直接单独复制到飞书。
- 当前完整列表实际共有 `61` 篇。

## 本批论文

6. [One Agent to Guide Them All: Empowering MLLMs for Vision-and-Language Navigation via Explicit World Representation 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/006_oneagent.md)
7. [Dynamic Topology Awareness: Breaking the Granularity Rigidity in Vision-Language Navigation 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/007_dynatopo.md)
8. [Spatial-VLN: Zero-Shot Vision-and-Language Navigation With Explicit Spatial Perception and Exploration 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/008_spatialvln.md)
9. [SpatialNav: Leveraging Spatial Scene Graphs for Zero-Shot Vision-and-Language Navigation 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/009_spatialnav.md)
10. [SeqWalker: Sequential-Horizon Vision-and-Language Navigation with Hierarchical Planning 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/010_seqwalker.md)

## 当前批次的快速判断

### 最值得优先精读
- `One Agent to Guide Them All`
- `Dynamic Topology Awareness`
- `SeqWalker`

### 更适合作为结构参考
- `Spatial-VLN`
- `SpatialNav`

### 更值得优先侦察代码
- `Dynamic Topology Awareness`
- `SeqWalker`

### 需要特别注意的可比性问题
- `One Agent to Guide Them All` 在 `RxR-CE` 上使用的是 `260` 条 sampled subset，而且核心依赖 `RGB-D`、位姿与显式 metric mapping。
- `Spatial-VLN` 的主价值在 zero-shot spatial reasoning 和 real-world deployment，challenge subset 与真实场景表格不能直接当标准主 benchmark leaderboard 使用。
- `SpatialNav` 明确允许 pre-exploration，并且连续环境结果仅基于 `100/200` 条 sampled subset，因此不能直接与标准 online `R2R-CE / RxR-CE` 横比。
- `SeqWalker` 的主任务是 `SH IR2R-CE`，它不是标准 `R2R-CE / RxR-CE` 主榜方法，而是长程、多阶段 continuous VLN 的扩展 benchmark 与层级规划方法。
