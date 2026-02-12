# HEARTBEAT.md - 定期检查任务

## 每小时检查项
- [ ] 检查网关状态: openclaw gateway status
- [ ] 检查模型配置: openclaw config get agents.defaults.model
- [ ] 如有异常，发送提醒

## 如果模型报错 "Unknown model"
1. 检查 openclaw.json 配置
2. 重启网关: openclaw gateway restart
3. 通知用户

## GLM 出问题应急方法

### 快速切换到 Kimi
```bash
# 1. 修改配置
openclaw config patch agents.defaults.model.primary="kimi-coding/kimi-k2-thinking"

# 2. 重启网关
openclaw gateway restart
```

### 或者手动编辑配置
编辑 `~/.openclaw/openclaw.json`:
```json
"model": {
  "primary": "kimi-coding/kimi-k2-thinking"
}
```
然后重启网关。

### 一键切换脚本（已保存到桌面）
双击桌面 `切换小爪模型.bat` 快速切换

## 备用模型配置
当前已配置:
- Primary: zhipu/glm-4-flash (GLM)
- 备用: kimi-coding/kimi-k2-thinking (Kimi)
- 备用: kimi-coding/k2p5 (Kimi K2.5)
