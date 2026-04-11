# 发现记录

## 2026-04-10

### 代理相关

- `clash` 和 `proxy` 不是独立可执行文件，而是 `~/.bashrc` 中定义的 shell function。
- Clash 当前配置端口：
  - HTTP: `18990`
  - SOCKS: `18991`
  - Mixed: `18993`
- 在 Codex 的非交互 shell 中，必须显式用交互式 bash 才能调用这些函数：

```bash
bash -ic 'proxy >/dev/null; <command>'
```

- 通过该方式，`curl -I https://github.com` 已验证可成功访问外网。
- 为减少后续误用，已在项目内新增 `scripts/proxy_exec.sh` 作为统一代理命令入口。

### GitHub 远程

- 本地仓库已关联远程 `fhx020826/fhx-nips-2026`。
- `git ls-remote` 在代理下可执行，但空仓库当前没有 refs 输出。
- 当前首个本地提交已经成功推送到远程，后续可以持续增量同步。

### conda

- `conda` 位于 `/home/hxfeng/anaconda3/bin/conda`。
- 未走代理时创建环境会超时。
- 当前环境 `fhx-nips-2026` 已可被 `conda run -n fhx-nips-2026` 正常调用，Python 版本为 `3.10.20`。

### HPC 环境

- 当前开发上下文是“Windows 本机 + Linux HPC 跳板机/集群远程开发”。
- 跳板机适合登录、管理、提交作业，不适合跑重负载程序。
- 已在项目内整理摘要手册：`docs/hpc_handbook.md`。

### 论文调研

- 已创建论文总表：`docs/paper_inventory.md`。
- 根据用户最新要求，论文总表已切换为“全部重新检索”模式。
- 当前已重新检索并登记的 direct-hit 论文包括：
  - `Beyond the Nav-Graph`
  - `Cross-modal Map Learning for Vision and Language Navigation`
  - `Iterative Vision-and-Language Navigation in Continuous Environments`
  - `DREAMWALKER`
  - `GridMM`
  - `Safe-VLN`
  - `Cog-GA`
  - `Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments`
  - `NavMorph`
  - `monoVLN`
  - `MonoDream`
  - `Efficient-VLN`
  - `ETP-R1`
  - `EmergeNav`
  - `Dynamic Topology Awareness`
  - `Let's Reward Step-by-Step`
- 当前新增趋势开始更清楚地分成两类：
  - topo / graph granularity / dynamic topology
  - step-aware reward / dense alignment / long-horizon credit assignment
- 用户指出的 `DualVLN` 漏项已补回，说明后续必须继续以 Awesome-VLN 为主线系统补表，不能只靠关键词零散搜索。
- 本轮又补回一批此前遗漏但重要的条目：
  - `Open-Nav`
  - `StreamVLN`
  - `DAgger Diffusion Navigation`
  - `RoomTour3D`
  - `Towards Learning a Generalist Model for Embodied Navigation`
- 目前飞书全量列表已经超过 100 篇，达到阶段性目标。
- 当前下一阶段重点应转向：
  - 日期与去重校验
  - 内部高质量 shortlist 的硬指标打分
- 现已拆分出两份对外/对内文档：
  - broad 全景列表：保留任务全貌
  - strict 严格列表：只保留 continuous VLN / VLN-CE 问题空间中的论文
- 本轮进一步确认 strict 列表的保留规则应当是：
  - `continuous VLN / VLN-CE` 必须是论文主任务身份
  - continuous benchmark / challenge / dataset 扩展可以保留
  - 纯离散 VLN 上游方法、survey、泛 embodied navigation 工作应从 strict 列表移出
- `arXiv API` 连续批量查询容易触发 `429`，更稳妥的方式是：
  - 先抽取 arXiv 编号
  - 再逐篇抓取 `abs` 页面中的 `v1` 提交日期
- 当前 strict 飞书终版已经完成逐日精排，核心集规模为 39 篇。
- 经过边界清洗后，用户需要的“飞书可直接粘贴终版”与“内部高质量 shortlist”已经真正分离：
  - `docs/paper_list_feishu_strict.md` 负责最严格的任务相关核心集
  - `docs/paper_quality_shortlist.md` 负责高质量 Top 25 优先级排序

## 2026-04-11

### 第一批粗读卡片

- 已开始把 Top 25 从“列表层”推进到“论文卡片层”，第一批文档为：
  - `docs/paper_roughread_top25_batch1.md`
- 当前最先落地卡片的 5 篇是：
  - `ETPNav`
  - `RxR-Habitat 2022` 冠军报告
  - `CA-Nav`
  - `DifNav`
  - `StreamVLN`

### baseline / codebase 相关新发现

- `ETPNav` 目前仍是最稳的 continuous VLN baseline / codebase 入口：
  - `R2R-CE` 与 `RxR-CE` 都有显式训练/评测入口
  - pretraining / finetuning / checkpoint 都已放出
  - 但环境老，且依赖 waypoint predictor 和额外预训练数据
- `RxR-Habitat 2022` 冠军方案更适合视作 `ETPNav` 的前身工程 recipe，而不是单独的长期代码底座：
  - 已核实官方 starter 在 `VLN-CE` 的 `rxr-habitat-challenge` 分支
  - 未检索到该技术报告独立维护的官方实现仓库
- `CA-Nav` 的强项不在“轻量 baseline”，而在：
  - progress / constraint / sub-instruction bridge
  - zero-shot 连续导航
  - real-world deployment 证明
  但它额外依赖 BLIP2、Grounded-SAM、LLM replies，工程链条更长
- `DifNav` 是 diffusion 进入 continuous VLN 的关键 direct-hit 论文，但当前公开生态仍不完整：
  - 评测代码和 checkpoint 已放出
  - 在线数据增强、训练数据与完整训练代码尚未放出
  - README 当前只清晰暴露 `R2R-CE` 入口，`RxR-CE` 公开成熟度仍需继续核实
- `StreamVLN` 是 history / streaming / deployment 路线的重要新主线，但 benchmark 可比性必须单独标注：
  - 使用了额外导航数据、DAgger 数据和通用多模态数据
  - 不应直接与只用标准 VLN-CE 数据的 baseline 做无标注对比

### 方法学相关新发现

- 当前高价值论文已经开始明显分成三类：
  - 稳定 baseline / 工程底座：`ETPNav`
  - 高层结构接口参考：`CA-Nav`、`Ground Slow, Move Fast`、`NavForesee`
  - 历史压缩 / 在线推理 / 长程闭环：`StreamVLN`
- 因此后续文档组织也应该分两层：
  - 论文卡片层：记录论文方法与实验边界
  - reconnaissance 层：只记录“仓库能否作为本项目起点”
