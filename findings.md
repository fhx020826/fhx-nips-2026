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
