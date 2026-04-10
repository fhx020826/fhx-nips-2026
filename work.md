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

### 当前阻塞

1. GitHub 仓库远程探针可连通，但仓库当前没有返回 refs，推测为空仓库或默认分支尚未产生首个提交。
2. 仍需验证通过代理执行 `git push` 是否稳定。

### 当前判断

1. 现在优先级最高的是把“代理 + conda + 仓库首个提交”彻底打通。
2. 基础设施已基本成型，可以在首次推送成功后进入论文总表搭建。

### 下一步

1. 完成项目治理文件与代理脚本的首次 Git 提交。
2. 通过代理测试远程 `push`。
3. 开始 continuous VLN / VLN-CE 论文总表搭建。
