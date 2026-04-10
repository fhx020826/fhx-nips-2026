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
   - Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments
   - monoVLN
   - MonoDream
   - ETP-R1
   - Efficient-VLN
   - Mind the Error!

### 当前阻塞

1. 论文总表目前仍以“总览池”为主，尚未展开为逐篇固定模板粗读。
2. 2025–2026 候选池还未系统扫全。

### 当前判断

1. 现在优先级最高的是把“代理 + conda + 仓库首个提交”彻底打通。
2. 基础设施已打通，当前应切换到“论文总表扩充 + 优先级排序 + 粗读模板化”。

### 下一步

1. 把 `docs/paper_inventory.md` 扩展到更完整的 2023–2026 候选池。
2. 对新增高优先级论文补齐固定粗读模板。
3. 按“直接命中 / 强相关 / 可迁移”三层进一步细化。
