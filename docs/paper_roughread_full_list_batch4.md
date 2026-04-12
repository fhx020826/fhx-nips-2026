# 完整论文列表粗读卡片（Batch 4）

说明：
- 本批按完整列表顺序继续推进，覆盖第 `16` 到第 `25` 篇论文。
- 每篇均采用与 `NaVid` 最终版一致的详细粗读模板与写作口径。
- 每篇文档都可直接单独复制到飞书。
- 当前完整列表实际共有 `61` 篇。

## 本批论文

16. [Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/016_groundslow.md)
17. [NavForesee: A Unified Vision-Language World Model for Hierarchical Planning and Dual-Horizon Navigation Prediction 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/017_navforesee.md)
18. [SoraNav: Adaptive UAV Task-Centric Navigation via Zeroshot VLM Reasoning 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/018_soranav.md)
19. [LaViRA: Language-Vision-Robot Actions Translation for Zero-Shot Vision Language Navigation in Continuous Environments 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/019_lavira.md)
20. [JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/020_janusvln.md)
21. [VLN-Zero: Rapid Exploration and Cache-Enabled Neurosymbolic Vision-Language Planning for Zero-Shot Transfer in Robot Navigation 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/021_vlnzero.md)
22. [GC-VLN: Instruction as Graph Constraints for Training-free Vision-and-Language Navigation 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/022_gcvln.md)
23. [DAgger Diffusion Navigation: DAgger Boosted Diffusion Policy for Vision-Language Navigation 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/023_difnav.md)
24. [MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/024_monodream.md)
25. [VPN: Visual Prompt Navigation 粗读](/home/hxfeng/fhx-nips-2026/docs/paper_roughreads_full/025_vpn.md)

## 当前批次的快速判断

### 最值得优先精读
- `Ground Slow, Move Fast`
- `NavForesee`
- `JanusVLN`
- `MonoDream`
- `DAgger Diffusion Navigation`

### 更适合作为结构参考或方法接口参考
- `VLN-Zero`
- `GC-VLN`
- `LaViRA`
- `SoraNav`
- `VPN`

### 更值得优先侦察代码
- `Ground Slow, Move Fast`
- `JanusVLN`
- `VLN-Zero`
- `VPN`

### 需要特别注意的可比性问题
- `Ground Slow, Move Fast` 虽然资源生态已经相当完整，但依托 `InternNav / InternData-N1` 体系，默认不是最朴素的公平 baseline 设定。
- `NavForesee` 的主表结果很强，但当前未核到官方代码、模型或项目页，且训练依赖大规模规划样本与 `Gemini 2.5 Pro` 数据生成。
- `SoraNav` 是 UAV 子线，不与 `R2R-CE / RxR-CE` 直接横比；当前也未核到正式开源仓库。
- `LaViRA` 的 simulator 结果只在 `VLN-CE val-unseen 100-episode subset` 上评测，不能误当成完整 split 的标准主榜结果。
- `JanusVLN` 的资源生态完整，但其 `Base / Extra` 数据设置要显式区分，不能把使用额外数据的结果与纯基础设定混写。
- `VLN-Zero` 是标准 `R2R-CE / RxR-CE` benchmark 上的 zero-shot 系统，但它依赖“先探索再部署”的两阶段流程以及 `OPENAI_API_KEY` 驱动的大模型调用，和训练型 baseline 的比较必须加前提。
- `GC-VLN` 虽然有官方仓库和项目页，但 README 仍写明完整代码将后续发布，当前更适合作为结构参考，不应误记为成熟可复现开源。
- `DAgger Diffusion Navigation` 是 diffusion 进入 continuous VLN 的关键论文，但主实验是按 `Open Area / Narrow Space / Stairs` 做单场景类别评测，指标里还是 `SRL`，不是标准 `R2R-CE val-unseen` 主榜。
- `MonoDream` 的方法和结果都很有价值，而且明确不依赖外部 web 数据；但当前未核到官方代码仓与项目页，适合继续跟踪，不宜立刻进入代码侦察第一梯队。
- `VPN` 不是标准语言导航主线，而是把 `R2R / R2R-CE` 改造成 `R2R-VP / R2R-CE-VP` 的视觉提示导航 benchmark；因此结果只能在该变体任务内解读。
