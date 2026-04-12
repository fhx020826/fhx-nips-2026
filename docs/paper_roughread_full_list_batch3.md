# 完整论文列表粗读卡片（Batch 3）

说明：
- 本批按完整列表顺序继续推进，覆盖第 `11` 到第 `15` 篇论文。
- 每篇均采用与 `NaVid` 最终版一致的详细粗读模板与写作口径。
- 每篇文档都可直接单独复制到飞书。
- 当前主执行总表已重构为 `75` 篇；其中原 batch 3 里的 `AirNav` 和 `IndoorUAV` 已因 scope 收紧被移出主线，不再作为后续粗读资产保留。

## 本批论文

12. [ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-Language Navigation in Continuous Environments 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/012_etpr1.md)
14. [CLASH: Collaborative Large-Small Hierarchical Framework for Continuous Vision-and-Language Navigation 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/014_clash.md)
15. [Efficient-VLN: A Training-Efficient Vision-Language Navigation Model 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/015_efficientvln.md)

## 当前批次的快速判断

### 最值得优先精读
- `ETP-R1`
- `CLASH`
- `Efficient-VLN`

### 更适合作为 benchmark / deployment 参考
- 本批原先包含的 `AirNav` 与 `IndoorUAV` 已不再属于当前主线范围，因此相关判断仅保留在历史记录中，不再继续维护。

### 更值得优先侦察代码
- `ETP-R1`
- `CLASH`

### 需要特别注意的可比性问题
- `ETP-R1` 虽然直接报告 `R2R-CE / RxR-CE`，但明确使用了 `Gemini` 增广数据、`Prevalent / RxR-Marky` 等额外数据，并依赖 depth，因此主结果必须带着“额外数据 + 非纯 RGB”前提看。
- `CLASH` 在 `R2R-CE` 上结果很强，但仿真使用 depth，真实部署使用 `LiDAR + SLAM`，且代码仓库 README 明确写明仍在逐步清理发布。
- `Efficient-VLN` 的项目页存在明显错链，最佳结果依赖 `ScaleVLN`，且当前未核到可信官方代码仓库，因此不能按“已完整开源”处理。
