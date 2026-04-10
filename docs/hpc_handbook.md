# HPC 使用手册摘要

## 当前工作模式

- 本机：Windows
- 远端：Linux HPC 跳板机/集群环境
- 当前开发方式：通过远程登录在 HPC 上开发与运行

这意味着后续所有环境、路径、代理、SLURM、容器、端口映射等操作，都要默认按“远端 Linux 集群”理解，而不是本地 Windows 机器。

## 技术支持

### 网管邮箱

- `qyfan@ir.hit.edu.cn`
- `cfyang@ir.hit.edu.cn`
- `cxduan@ir.hit.edu.cn`
- `yifchen@ir.hit.edu.cn`

### 其他联系

- 申请实验室邮箱：`jwcao@ir.hit.edu.cn`
- HPC 申请老师：`xding@ir.hit.edu.cn`

如果遇到账户、权限、软件安装、Docker/Enroot、SLURM、磁盘额度、SSH 故障等问题，可联系网管或在赛尔大群求助。

## 新生申请 HPC

1. 先申请实验室邮箱。
2. 用实验室邮箱向相关老师和网管发送申请邮件，说明组别、姓名、年级和申请原因。
3. 生成 SSH key：

```bash
ssh-keygen -t rsa -b 4096 -C "<your email>@ir.hit.edu.cn"
```

4. 将公钥 `~/.ssh/id_rsa.pub` 发给网管。

## 登录方式

### 跳板机信息

- `hpc-login-01`
  - IP: `10.160.22.46`
  - Port: `2223`
- `hpc-login-02`
  - IP: `10.160.22.46`
  - Port: `2222`

### SSH config 示例

```sshconfig
Host hpc
  HostName 10.160.22.46
  Port 2223
  User <username>
  IdentityFile <private key path>
  ServerAliveInterval 240

Host hpc-02
  HostName 10.160.22.46
  Port 2222
  User <username>
  IdentityFile <private key path>
  ServerAliveInterval 240
```

### 常用登录命令

```bash
ssh hpc
ssh hpc-02
```

### 账号规则

- 默认用户名：`名缩写 + 姓`
- 默认密码：姓名全拼
- 登录后可用 `passwd` 修改密码

## 重要行为约束

1. 不要在跳板机上运行大负载程序。
2. 不要使用内网穿透工具。
3. 不要递归开放 `777` 权限。
4. 不要给家目录或 SSH 密钥上级目录过高权限。

## SLURM 快速参考

### 常用命令

- `sinfo`：查看集群状态
- `squeue`：查看作业队列
- `squeue --me`：只看自己的作业
- `sbatch`：提交脚本作业
- `srun`：提交交互式作业
- `scancel <job id>`：取消作业
- `sacct -X --format="JobID%6,State%10,JobName%15,Elapsed%10,AllocTRES%80"`：查看历史作业资源

### sinfo 常用格式

```bash
sinfo -N -o "%5N  %5t  %13C  %8O  %8e  %7m  %G"
```

### 节点状态含义

- `down`：下线
- `drain`：故障
- `drng`：故障但已有作业不受影响
- `alloc`：资源已全部分配
- `mix`：资源部分分配
- `idle`：空闲
- `comp`：清理中

### scir 插件

- `scir-watch -s`：查看 GPU 名称、费用、空闲卡和节点
- `scir-account`：查看计算点数
- `scir-account -d`：查看实时额度
- `scir-account transfer --points <POINTS> --target <TARGET> --month <MONTH>`：转点数

## 交互式申请节点

### 例 1：申请 4 卡 A100 80G 并进入 shell

```bash
srun --gres=gpu:a100-sxm4-80gb:4 --pty bash -i
```

### 例 2：指定节点

```bash
srun -w gpu06 --gres=gpu:a100-sxm4-80gb:4 --pty bash -i
```

### 注意

- 交互式申请结束后应尽快释放资源。
- 如果要在同一节点内开多个终端，优先用 `tmux`。
- 目前多数节点禁用 SSH，避免“先占资源不使用”。
- 开放 SSH 的节点：`gpu10` 到 `gpu14`。

## sbatch 脚本模板

```bash
#!/bin/bash
#SBATCH -J test
#SBATCH -o test.out
#SBATCH -e test.err
#SBATCH -p compute
#SBATCH -N 1
#SBATCH -t 1:00:00
#SBATCH -w gpu06
#SBATCH --gres=gpu:a100-sxm4-80gb:4

. $HOME/miniconda3/etc/profile.d/conda.sh
conda activate devel_cu102_1.7.1

python -V
```

提交：

```bash
sbatch run.sh
```

## 计算点数

- 提交作业会按 GPU 单价、GPU 数量、申请时长预扣点数。
- 作业提前结束会返还剩余点数。
- 博士:硕士月额度比例约为 `1:0.7`，每月重置。

## CUDA 与环境

### 查看 PyTorch 对应 CUDA 版本

```bash
python -c "import torch; print(torch.__version__); print(torch.version.cuda)"
```

### 加载公共 cudatoolkit

```bash
. /usr/share/modules/init/bash
module use --append /home/share/modules/modulefiles
module avail
module load cuda/11.8.0
nvcc -V
```

### conda 方式安装 CUDA

- 适合需要编译 `apex`、`deepspeed` 或 JIT 扩展时使用。
- 必要时设置：

```bash
export CUDA_HOME=<conda_env_path>
export CUDA_PATH=<conda_env_path>
```

### 动态库问题

如果需要 `lib64 -> lib` 链接：

```bash
ln -s lib lib64
```

## 磁盘额度

### 规则

- 软额度：6TB
- 硬额度：9TB
- 超过软额度后有 7 天宽限期
- 超过硬额度会直接禁止写入

### 查询命令

```bash
/usr/lpp/mmfs/bin/mmlsquota --block-size autofta
```

## 共享目录权限

要共享某个目录给别人：

1. 从家目录到目标目录路径上的每一级都要给其他用户 `x` 权限：

```bash
chmod 711 /path/to/each/dir
```

2. 最终目录一般给 `rx` 权限：

```bash
chmod 755 /path/to/final/dir
```

3. 更细粒度权限可用 `setfacl`。

## 公共模型目录

- 共享路径：`/home/share/models`

## 容器

### 推荐

- 优先使用 `enroot`
- 只有明确需要 Docker 导出/兼容时再考虑 rootless Docker

### Enroot 常用命令

导入镜像：

```bash
enroot import docker://<IMAGE NAME>
```

创建容器：

```bash
enroot create --name <CONTAINER NAME> <SQSH PATH>
```

启动并执行命令：

```bash
enroot start <CONTAINER NAME> <COMMAND>
```

挂载目录：

```bash
enroot start --mount <SRC>:<DST> <CONTAINER NAME> <COMMAND>
```

### Enroot + SLURM 示例

```bash
#!/usr/bin/bash

#SBATCH -J enroot
#SBATCH -o torch251.log
#SBATCH --gres=gpu:geforce_rtx_2080_ti:1
#SBATCH --container-writable
#SBATCH --container-mount-home
#SBATCH --container-mounts /home/share/models:/models:ro
#SBATCH --container-image torch251

python -c "import torch; print(torch.cuda.is_available())"
```

### Rootless Docker 关键点

首次设置：

```bash
dockerd-rootless-setuptool.sh install
```

如果失败，可手动设置：

```bash
mkdir -p /tmp/$(id -u)/docker/run
export XDG_RUNTIME_DIR=/tmp/$(id -u)/docker/run
export DOCKER_HOST=unix:///tmp/$(id -u)/docker/run/docker.sock
```

启动：

```bash
PATH=/usr/bin:/sbin:/usr/sbin:$PATH dockerd-rootless.sh
```

## 端口映射

### 正向映射

将远端端口映射到本地，例如 TensorBoard：

```bash
ssh -N -L 22222:localhost:6006 hpc
```

然后本地打开：

```text
http://localhost:22222
```

### 反向映射

让 HPC 使用本地代理，例如将本地 Clash `7890` 映射到远端 `55555`：

```bash
ssh -R 55555:localhost:7890 hpc
export all_proxy=http://localhost:55555
```

如果端口冲突，换一个更大的端口。

## GPU 监控

HPC 02 跳板机有 GPU 可视化监控，映射方式：

```bash
ssh -L 3000:localhost:3000 hpc-02
```

然后本地打开：

```text
http://localhost:3000/goto/wpCAJj1SR?orgId=1
```

## 远程桌面

### 启动 VNC

```bash
/opt/TurboVNC/bin/vncserver
```

### 查看桌面

```bash
/opt/TurboVNC/bin/vncserver -list
```

### 端口映射示例

假设 `gpu05` 上的桌面序号为 `:1`，即端口 `5901`：

```bash
ssh -L 55900:gpu05:5901 hpc
```

然后本地 VNC 连接：

```text
localhost:55900
```

## 常见问题

### Requested node configuration is not available

常见原因：

- GPU 型号名称写错
- `-` 和 `_` 混用
- 申请资源超出节点物理上限

排查命令：

```bash
scir-watch -s
sinfo -N -o "%5N  %5t  %13C  %8O  %8e  %7m  %G"
```

### OOM killed

说明内存申请不够。可通过增加 CPU / 内存申请量解决。

### huggingface 下载失败

通常是外网访问问题。可以：

1. 使用本地代理反向映射
2. 在 HPC 内使用 Clash 等代理

### SSH 突然无法登录

常见原因：

- SSH key 权限过大
- 上级目录权限过大

不要递归给家目录过高权限，必要时联系网管。

### SSH 一段时间后自动断开

在 `~/.ssh/config` 中添加：

```sshconfig
ServerAliveInterval 240
```

### 不想显示登录提示

```bash
touch $HOME/.hushlogin
```

### 修改默认 shell

```bash
scir-manage chsh
```

## 对本项目的直接建议

1. 重计算任务不要在跳板机执行，统一通过 `srun` / `sbatch` 进入计算节点。
2. 交互式实验优先：
   - 跳板机提交
   - 节点内 `tmux`
   - 环境激活后再运行
3. 后续如果需要大模型、容器化训练或复杂依赖，优先考虑 `enroot`。
4. 需要开放共享目录时，严格控制权限，不要图省事开大权限。
5. 需要长时间监控任务时，优先用端口映射或日志，而不是长期占着交互式会话。
