#!/usr/bin/env bash

# 统一通过用户已有的 proxy shell function 执行外网命令。
# 用法：
#   ./scripts/proxy_exec.sh curl -I https://github.com
#   ./scripts/proxy_exec.sh git ls-remote https://github.com/user/repo.git

set -euo pipefail

if [[ $# -eq 0 ]]; then
  echo "用法: $0 <command> [args...]" >&2
  exit 1
fi

escaped_args=()
for arg in "$@"; do
  escaped_args+=("$(printf '%q' "$arg")")
done

command_string="${escaped_args[*]}"

exec bash -ic "proxy >/dev/null; ${command_string}"
