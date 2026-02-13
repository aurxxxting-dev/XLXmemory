# 记忆文件自动备份脚本 (PowerShell)
$workspace = "$env:USERPROFILE\.openclaw\workspace"
Set-Location $workspace

# 先检查网络/VPN是否连通
Write-Host "$(Get-Date): 检查网络连接..."
try {
    # 尝试访问 GitHub API，超时5秒
    $null = Invoke-RestMethod -Uri "https://api.github.com" -TimeoutSec 5
    Write-Host "$(Get-Date): ✅ 网络连接正常"
} catch {
    Write-Host "$(Get-Date): ❌ 网络不通或VPN未连接，备份中止"
    Write-Host "$(Get-Date): 错误信息: $_"
    exit 1
}

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

try {
    git push origin master
    Write-Host "$(Get-Date): ✅ 备份完成并成功推送到云端"
} catch {
    Write-Host "$(Get-Date): ❌ 推送失败: $_"
    exit 1
}
