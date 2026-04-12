# 当前进展

## 2026-04-12

### 本轮真实状态

1. 项目工作区已固定在：
   - `/home/hxfeng/fhx-nips-2026`
2. Git 远程已正确关联：
   - `origin = https://github.com/fhx020826/fhx-nips-2026.git`
3. 论文执行顺序已经固定为：
   - `docs/paper_list_feishu_strict.md`
4. 内部高质量列表已经固定为：
   - `docs/paper_quality_shortlist.md`
5. 单论文详细粗读卡片已经采用单文件落盘形式，目录为：
   - `docs/paper_roughreads_full/`

### 已完成的关键资产

1. 已完成前 `10` 篇单论文详细粗读：
   - `001_p3nav.md`
   - `002_emergenav.md`
   - `003_himemvln.md`
   - `004_stepaware.md`
   - `005_eventkg.md`
   - `006_oneagent.md`
   - `007_dynatopo.md`
   - `008_spatialvln.md`
   - `009_spatialnav.md`
   - `010_seqwalker.md`
2. 已完成第 `11` 到第 `15` 篇单论文详细粗读：
   - `011_airnav.md`
   - `012_etpr1.md`
   - `013_indooruav.md`
   - `014_clash.md`
   - `015_efficientvln.md`
3. 已完成三批索引文档：
   - `docs/paper_roughread_full_list_batch1.md`
   - `docs/paper_roughread_full_list_batch2.md`
   - `docs/paper_roughread_full_list_batch3.md`
4. 已将“每批粗读都要同步核查 shortlist”的规则写入：
   - `user.md`
5. 已对 shortlist 中与前 `10` 篇相关的条目完成复核，并修正以下描述：
   - `One Agent to Guide Them All`：补充 `RGB-D` 与 `RxR-CE sampled subset`
   - `Dynamic Topology Awareness`：补充官方代码已核实
   - `Spatial-VLN`：明确其更适合作为空间推理 / 部署参考
   - `SpatialNav`：明确其建立在 `pre-exploration + sampled subset` 上
   - `SeqWalker`：明确其属于 `SH IR2R-CE` 扩展设定
6. 已完成 batch 3 对应 shortlist 复核，并修正以下判断：
   - `CLASH`：由“仅 arXiv”修正为“`arXiv + 官方代码（逐步清理发布）`”
   - `ETP-R1`：由“仅 arXiv”修正为“`arXiv + 官方代码 + 数据/ckpt`”
   - `Efficient-VLN`：确认项目页存在错链，当前未核到可信官方代码，但仍纳入内部高质量 shortlist
   - `AirNav`：明确其属于 UAV benchmark 扩展线，且当前公开生态以训练集与权重为主
   - `IndoorUAV`：明确其更适合作为室内 UAV benchmark / hierarchical bridge 参考，而非 Habitat 主线 baseline
7. 已强化仓库规范文档：
   - `coding.md`
8. 已把临时调研目录纳入忽略列表：
   - `tmp_papers/`
   - `tmp_repos/`
9. 已清理两项历史未跟踪临时产物：
   - `configs/paper_metadata/001_p3nav.json`
   - `scripts/render_roughread_card.py`

### 当前确认的流程约束

1. 之后每次批量粗读都必须同步做外网事实核查。
2. GitHub 仓库、README、项目页和模型页也必须算入外网核查范围。
3. 外网命令统一走代理，优先形式为：
   - `bash -ic 'proxy >/dev/null; <command>'`
4. 每批都要同步判断：
   - 是否应纳入内部高质量论文列表
   - 已在 shortlist 中的条目是否需要修正
5. 对 `sampled subset`、`pre-exploration`、额外传感器、扩展 benchmark 等设定必须显式标注。
6. 当前已进一步固定：`Efficient-VLN` 这类“项目页存在但资源链接异常”的论文，不得误记为“官方代码已公开”。

### 当前阻塞

1. 当前 shell 中 `conda` 命令不可用。
2. 因此，如果下一步要执行 Python 开发、运行脚本或正式实现代码，需要先解决 conda 初始化问题。
3. 仓库内仍存在一些历史临时调研缓存和旧文档，尚未进入清理动作，但已经需要持续评估。

### 当前判断

1. 当前项目仍处于“粗读资产建设 + shortlist 校正 + baseline 前置侦察”阶段。
2. 当前 `011` 到 `015` 批次中，最值得后续优先精读或代码侦察的是：
   - `ETP-R1`
   - `CLASH`
   - `Efficient-VLN`
3. 现在最重要的不是扩展更多杂项脚本，而是继续稳步完成 `61` 篇论文的高质量粗读。
4. 当前最值得后续继续关注的方向仍然是：
   - explicit world representation
   - topo granularity / graph planning
   - hierarchical planning / progress / recovery
   - streaming history
   - diffusion low-level expert
   - training-efficient history compression

### 下一步

1. 继续生成第 `16` 到第 `20` 篇详细粗读卡片。
2. 每完成一批，同步复核 `docs/paper_quality_shortlist.md`。
3. 对当前 shortlist 中高优先级条目逐步进入 codebase reconnaissance，优先顺序先看：
   - `ETP-R1`
   - `CLASH`
   - `JanusVLN`
   - `StreamVLN`
4. 在进入任何 Python 运行任务前，先解决 conda 环境可用性问题。
5. 后续视需要继续整理：
   - `baseline / codebase reconnaissance` 专门文档
   - shortlist 中高优先级条目的代码可跑性核查
