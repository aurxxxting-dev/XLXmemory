# 记忆文件自动备份脚本 (PowerShell)
$workspace = "$env:USERPROFILE\.openclaw\workspace"
Set-Location $workspace

# 添加所有变更
git add -A

# 检查是否有变更需要提交
$status = git status --porcelain
if (-not $status) {
    Write-Host "$(Get-Date): 无变更，跳过备份"
    exit 0
}

# 提交并推送
$dateStr = Get-Date -Format "yyyy-MM-dd HH:mm"
git commit -m "自动备份记忆文件 $dateStr"
git push origin master

Write-Host "$(Get-Date): 备份完成"
