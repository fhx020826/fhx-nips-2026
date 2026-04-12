# 完整论文列表粗读卡片（Batch 3）

说明：
- 本批按完整列表顺序继续推进，覆盖第 `11` 到第 `15` 篇论文。
- 每篇均采用与 `NaVid` 最终版一致的详细粗读模板与写作口径。
- 每篇文档都可直接单独复制到飞书。
- 当前完整列表实际共有 `61` 篇。

## 本批论文

11. [AirNav: A Large-Scale Real-World UAV Vision-and-Language Navigation Dataset with Natural and Diverse Instructions 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/011_airnav.md)
12. [ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-Language Navigation in Continuous Environments 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/012_etpr1.md)
13. [IndoorUAV: Benchmarking Vision-Language UAV Navigation in Continuous Indoor Environments 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/013_indooruav.md)
14. [CLASH: Collaborative Large-Small Hierarchical Framework for Continuous Vision-and-Language Navigation 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/014_clash.md)
15. [Efficient-VLN: A Training-Efficient Vision-Language Navigation Model 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/015_efficientvln.md)

## 当前批次的快速判断

### 最值得优先精读
- `ETP-R1`
- `CLASH`
- `Efficient-VLN`

### 更适合作为 benchmark / deployment 参考
- `AirNav`
- `IndoorUAV`

### 更值得优先侦察代码
- `ETP-R1`
- `CLASH`
- `AirNav`

### 需要特别注意的可比性问题
- `AirNav` 属于真实城市 UAV VLN benchmark，不与 `R2R-CE / RxR-CE` 主榜直接可比；当前官方仓库 README 还明确写明主要公开训练集，`val/test` 释放状态需持续跟踪。
- `ETP-R1` 虽然直接报告 `R2R-CE / RxR-CE`，但明确使用了 `Gemini` 增广数据、`Prevalent / RxR-Marky` 等额外数据，并依赖 depth，因此主结果必须带着“额外数据 + 非纯 RGB”前提看。
- `IndoorUAV` 是室内 UAV 子线 benchmark，方法上依赖 `GPT-4o` 进行 instruction decomposition，并结合 `pi0` 低层 VLA policy，不是 Habitat ground-agent 的直接 baseline。
- `CLASH` 在 `R2R-CE` 上结果很强，但仿真使用 depth，真实部署使用 `LiDAR + SLAM`，且代码仓库 README 明确写明仍在逐步清理发布。
- `Efficient-VLN` 的项目页存在明显错链，最佳结果依赖 `ScaleVLN`，且当前未核到可信官方代码仓库，因此不能按“已完整开源”处理。
