# 🐾 小爪备份系统

## 手动备份
双击桌面 `🐾小爪备份.bat`：
- 自动检测所有变更
- 提交到本地 git
- 推送到 GitHub

## 备份内容
- ✅ memory/ 每日记忆日志
- ✅ *.md 配置文件（IDENTITY, SOUL, USER 等）
- ✅ .clawhub/ skill 配置
- ✅ skills/ 自定义技能
- ✅ pages/ 小程序代码
- ✅ server/ 后端服务

## 多身体同步
当在新设备部署时：
```bash
git clone https://github.com/aurxxxting-dev/XLXmemory.git
```
所有记忆和配置一键恢复！

## 自动备份（可选）
可设置 Windows 计划任务，每小时/每天自动备份。

## 智能家居预留接口
待接入：
- [ ] Home Assistant
- [ ] Node-RED
- [ ] MQTT Broker
- [ ] 智能网关管理

未来可扩展为多身体管理中枢 🐾
