# 当前进展

## 2026-04-10

### 本轮新增

1. 新建隔离工作区 `/home/hxfeng/fhx-nips-2026`。
2. 初始化本地 Git 仓库，并关联远程：
   - `https://github.com/fhx020826/fhx-nips-2026.git`
3. 建立基础目录结构：
   - `docs/`
   - `src/`
   - `scripts/`
   - `configs/`
   - `data/`
   - `artifacts/`
   - `tmp/`
4. 明确代理真实用法：
   - `clash` / `proxy` 来自 `~/.bashrc` 的 shell function
   - 后续外网命令应通过 `bash -ic 'proxy >/dev/null; <command>'` 执行
5. 已验证：
   - Clash 当前正在运行
   - `curl` 可通过代理访问 GitHub
   - `conda run -n fhx-nips-2026 python --version` 返回 `Python 3.10.20`
6. 新增统一代理脚本：
   - `scripts/proxy_exec.sh`
7. 新增 HPC 使用摘要文档：
   - `docs/hpc_handbook.md`
8. 明确当前开发模式：
   - 本机 Windows
   - 远端 Linux HPC 跳板机/集群
   - 重负载任务后续统一走 SLURM/计算节点
9. 新建论文总表：
   - `docs/paper_inventory.md`
10. 已将第一批新增候选落表，包含：
   - Beyond the Nav-Graph
   - Cross-modal Map Learning for Vision and Language Navigation
   - Iterative Vision-and-Language Navigation in Continuous Environments
   - DREAMWALKER
   - GridMM
   - Safe-VLN
   - Cog-GA
   - Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments
   - NavMorph
   - monoVLN
   - MonoDream
   - Efficient-VLN
   - ETP-R1
   - EmergeNav
   - Dynamic Topology Awareness
   - Step-Aware Contrastive Alignment
   - GC-VLN
11. 已按你的新要求改成“全部重新检索”模式，不再在论文总表里使用“继承上下文”来源。
12. 新增飞书可直接粘贴的平铺列表：
   - `docs/paper_list_feishu.md`
13. 当前已核实并进入平铺列表的论文数为 27 篇，仍远未达到目标规模。
14. 已补回前一轮遗漏的关键工作：
   - DualVLN
   - ETPNav
   - NaVid
   - VPN
   - HA-VLN
   - Human-Aware VLN
   - NavTrust
15. 继续补回 direct-hit / 强相关关键漏项：
   - Open-Nav
   - StreamVLN
   - DAgger Diffusion Navigation
   - RoomTour3D
   - NaviLLM
16. 当前飞书列表已扩至 102 条，已覆盖：
   - 任务起点
   - 桥接/迁移
   - 竞赛冠军方案
   - topo / graph / memory / lookahead
   - zero-shot / open-source LLM / large-small hierarchy
   - diffusion / streaming / benchmark 扩展
   - benchmark 血缘线（R2R / RxR / Habitat）
   - VLN 方法演进链（离散上游但直接影响 continuous VLN-CE）
17. 按你的最新要求，交付结构正式分成两层：
   - 对外：最全论文列表（最终目标 >100 篇）
   - 对内：高质量 shortlist（目标约 25 篇）
18. 新增内部质量短名单文件：
   - `docs/paper_quality_shortlist.md`
19. 新增严格终版飞书列表：
   - `docs/paper_list_feishu_strict.md`
20. 内部 shortlist 已改为正式排序版，包含分数、用途与优先级建议。
21. 本轮对 strict 列表做了边界清洗：
   - 删除纯离散 VLN 上游方法
   - 删除纯 survey
   - 删除泛 embodied navigation 但不以 continuous VLN 为主任务的条目
22. 重新定义 strict 列表保留范围：
   - direct continuous VLN 方法
   - continuous VLN 的 zero-shot / memory / topology / streaming / robustness 工作
   - continuous VLN 的 benchmark / challenge / dataset 扩展
23. 新增日期核验脚本：
   - `scripts/collect_arxiv_dates.py`
   - `scripts/fetch_arxiv_abs_dates.py`
24. 已逐篇核对 strict 核心集的 `arXiv v1` 首发日期，并完成逐日倒序重排。
25. strict 飞书终版现收敛为 39 篇核心论文：
   - 从 2026-03-16 的 `EmergeNav / HiMemVLN`
   - 到 2020-04-06 的 `Beyond the Nav-Graph`
26. `docs/paper_quality_shortlist.md` 已重写为飞书可直接粘贴的 Top 25 高质量优先级表。

## 2026-04-11

### 本轮新增

1. 新建第一批 Top 25 统一粗读卡片文档：
   - `docs/paper_roughread_top25_batch1.md`
2. 第一批已落地粗读与生态核查的条目共 5 篇：
   - `ETPNav`
   - `1st Place Solutions for RxR-Habitat Vision-and-Language Navigation Competition (CVPR 2022)`
   - `Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments`
   - `DAgger Diffusion Navigation`
   - `StreamVLN`
3. 已对上述条目逐项补充：
   - 论文页
   - 代码仓
   - 项目页
   - benchmark 身份
   - 可比性判断
   - 额外数据 / 额外监督 / 额外传感器依赖
   - 是否适合作为 baseline / codebase reconnaissance 对象
4. 当前已形成第一轮明确工程判断：
   - `ETPNav` 仍是最稳的 continuous VLN baseline / codebase 入口
   - `RxR-Habitat 2022` 冠军报告更适合作为 `ETPNav` 前身 recipe 参考
   - `CA-Nav` 更适合作为 progress / constraint / sub-instruction 结构参考
   - `DifNav` 值得重点跟踪，但公开训练闭环尚不完整
   - `StreamVLN` 是 history / streaming / deployment 路线高价值新主线，但不应和标准 benchmark baseline 直接等价比较

### 当前阻塞

1. 论文总表目前仍以“总览池”为主，尚未展开为逐篇固定模板粗读。
2. 2025–2026 候选池还未系统扫全。
3. 部分 2025 论文当前只完成了 paper 级别链接核实，项目页/代码页/正式录用信息还未补齐。
4. broad 总表仍有继续补齐和细分标签的空间，但 strict 核心集已经基本稳定。
5. 当前飞书 broad 列表已扩到 100+，已达到“全景图谱”阶段目标。
6. 接下来重点不再是继续堆数量，而是：
   - 日期精排
   - 去重复核
   - 内部高质量 25 篇打分校准
7. strict 列表已完成逐日精排，但部分 2025–2026 新论文的项目页 / 代码页 / 录用信息仍需后续逐篇补齐到粗读模板。
8. 第一批粗读卡片已经建立，但还只覆盖 Top 25 中的 5 篇，尚未形成完整 Top 25 卡片层。
9. baseline / codebase reconnaissance 目前仍停留在 paper-card 层，尚未单独抽成“仓库可跑性与依赖风险”文档。

### 当前判断

1. 现在优先级最高的是把“代理 + conda + 仓库首个提交”彻底打通。
2. 基础设施已打通，当前已进入“strict 核心集精排完成，接下来做粗读模板化”的阶段。
3. 当前已正式进入“Top 25 论文卡片化 + baseline/codebase reconnaissance 前置核查”阶段。

### 下一步

1. 对 strict 核心集 39 篇按统一粗读模板逐篇展开。
2. 对 Top 25 shortlist 继续补硬指标：
   - 代码
   - 项目页
   - benchmark 可比性
   - 额外数据 / 额外监督 / 额外传感器
3. 继续维护 broad 全景池，但不再把它和 strict 飞书终版混在一起。
4. 完成远程 push，确保本地与远程一致。
5. 第二批优先补：
   - `Ground Slow, Move Fast`
   - `NavForesee`
   - `NaVid`
   - `DREAMWALKER`
   - `Open-Nav`
6. 在第二批粗读之后，单独整理一页 `baseline / codebase reconnaissance` 文档，聚焦：
   - 仓库是否可跑
   - 依赖栈是否过旧
   - 数据 / 权重是否可得
   - 最小可验证起点应选谁
