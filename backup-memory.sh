#!/bin/bash
# 记忆文件自动备份脚本

cd "$HOME/.openclaw/workspace" || exit 1

# 添加所有变更
git add -A

# 检查是否有变更需要提交
if git diff --cached --quiet; then
    echo "$(date): 无变更，跳过备份"
    exit 0
fi

# 提交并推送
git commit -m "自动备份记忆文件 $(date '+%Y-%m-%d %H:%M')"
git push origin master

echo "$(date): 备份完成"
