# 完整论文列表粗读卡片（Batch 1）

说明：
- 本批按完整列表的时间顺序推进，覆盖前 `5` 篇论文。
- 每篇均采用与 `P^3Nav` 相同的最终粗读模板与写作口径。
- 每篇文档都可直接单独复制到飞书。
- 当前完整列表实际共有 `61` 篇。

## 本批论文

1. [P^3Nav: End-to-End Perception, Prediction and Planning for Vision-and-Language Navigation 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/001_p3nav.md)
2. [EmergeNav: Structured Embodied Inference for Zero-Shot Vision-and-Language Navigation in Continuous Environments 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/002_emergenav.md)
3. [HiMemVLN: Enhancing Reliability of Open-Source Zero-Shot Vision-and-Language Navigation with Hierarchical Memory System 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/003_himemvln.md)
4. [Let’s Reward Step-by-Step: Step-Aware Contrastive Alignment for Vision-Language Navigation in Continuous Environments 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/004_stepaware.md)
5. [Enhancing Vision-Language Navigation with Multimodal Event Knowledge from Real-World Indoor Tour Videos 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/005_eventkg.md)

## 当前批次的快速判断

### 最值得优先精读
- `P^3Nav`
- `HiMemVLN`
- `Let’s Reward Step-by-Step`

### 更适合作为结构参考
- `EmergeNav`
- `Enhancing Vision-Language Navigation with Multimodal Event Knowledge from Real-World Indoor Tour Videos`

### 更值得优先侦察代码
- `HiMemVLN`
- `Let’s Reward Step-by-Step`

### 需要特别注意的可比性问题
- `EmergeNav` 与 `HiMemVLN` 的主实验都更接近 zero-shot `100-episode protocol`，不是标准 full benchmark leaderboard 设定。
- `Let’s Reward Step-by-Step` 与主 benchmark 直接对齐，但训练中使用了 divergence correction 的 simulator teacher signal。
- `Enhancing Vision-Language Navigation with Multimodal Event Knowledge from Real-World Indoor Tour Videos` 依赖大规模外部视频知识图和 GPT-4 / LLaVA 自动构图，比较时必须单独标注外部知识来源。
