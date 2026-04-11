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

### 当前阻塞

1. 论文总表目前仍以“总览池”为主，尚未展开为逐篇固定模板粗读。
2. 2025–2026 候选池还未系统扫全。
3. 部分 2025 论文当前只完成了 paper 级别链接核实，项目页/代码页/正式录用信息还未补齐。
4. 本轮最新本地提交还未成功 push，原因是代理链路发生 `gnutls_handshake` / 连接类瞬时错误。
5. 当前飞书列表已扩到 102 条，已达到“>100”目标。
6. 接下来重点不再是数量，而是：
   - 日期精排
   - 去重复核
   - 内部高质量 25 篇打分校准
7. 当前 broad 列表和 strict 列表已分开，但 strict 列表的日期仍是月粒度，不是逐日精排。

### 当前判断

1. 现在优先级最高的是把“代理 + conda + 仓库首个提交”彻底打通。
2. 基础设施已打通，当前应切换到“论文总表扩充 + 优先级排序 + 粗读模板化”。

### 下一步

1. 把 `docs/paper_inventory.md` 扩展到更完整的 2023–2026 候选池。
2. 对新增高优先级论文补齐固定粗读模板。
3. 扩展 `docs/paper_list_feishu.md` 到更接近 100 篇。
4. 完成远程 push，确保本地与远程一致。
