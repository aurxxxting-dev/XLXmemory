# 微信小程序激励视频广告接入指南

## 📁 文件说明

```
/pages/draw/
  ├── draw.js      # 页面逻辑（摇签 + 广告 + 解锁）
  ├── draw.wxml    # 页面结构
  └── draw.wxss    # 页面样式

/server/
  └── server.js    # 后端服务（调用 Gemini API）
```

---

## 🚀 接入步骤

### 第一步：开通流量主

1. 登录 [微信公众平台](https://mp.weixin.qq.com/)
2. 左侧菜单 → **流量主**
3. 点击 **开通**（需要小程序累计 1000 独立访客）
4. 创建广告位：
   - 广告位类型：**激励式广告**
   - 广告位名称：`解签解锁视频`
   - 复制广告位 ID（如 `adunit-xxxxxxxxx`）

### 第二步：修改代码

**1. 替换广告位 ID**

打开 `pages/draw/draw.js`，找到：
```javascript
const adUnitId = 'adunit-xxxxxxxxx'  // ← 改成你的广告位ID
```

**2. 修改后端接口地址**

找到：
```javascript
url: 'https://你的服务器.com/api/interpret'
```
改成你的实际服务器地址。

### 第三步：配置服务器（后端）

**方式 A：自有服务器**

```bash
# 1. 安装依赖
npm install express @google/genai

# 2. 设置 API Key
export GEMINI_API_KEY=你的Gemini_API_Key

# 3. 启动服务
node server.js
```

**方式 B：微信云开发（更简单）**

如果不想买服务器，可以用微信云开发：

```javascript
// cloudfunctions/interpret/index.js
const cloud = require('wx-server-sdk');
const { GoogleGenAI } = require('@google/genai');

cloud.init();

exports.main = async (event, context) => {
  const { sign } = event;
  
  const ai = new GoogleGenAI({ 
    apiKey: '你的API_Key'  // 云函数里安全
  });
  
  const response = await ai.models.generateContent({
    model: 'gemini-2.0-flash',
    contents: `解读签文：${sign}...`
  });
  
  return { interpretation: response.text };
};
```

### 第四步：测试

1. 开发者工具 → 真机调试
2. 摇一摇抽签
3. 点击"看视频解锁"
4. 看完广告 → 应该解锁 AI 解签

---

## 💡 关键逻辑

```
用户摇签
   ↓
显示签文 + "看视频解锁" 按钮
   ↓
用户点击 → 播放激励视频广告
   ↓
用户看完（15-30秒）
   ↓
触发 unlockContent()
   ↓
调用后端 API → Gemini 解签
   ↓
显示 AI 解签结果
```

---

## ⚠️ 重要提醒

### 1. 广告合规
- ✅ 用户主动点击才能播放
- ✅ 不能诱导点击（不能说"快点广告领红包"）
- ❌ 不能自动播放、不能强制看完

### 2. API Key 安全
- ❌ **千万不要把 Gemini API Key 写在前端代码里**
- ✅ 必须通过后端/云函数调用
- ✅ 后端限制调用频率，防止被刷

### 3. 用户体验
- 广告加载需要 1-3 秒，要有 loading 提示
- 如果广告加载失败，给备用方案（比如免费次数）
- 用户中途退出广告 = 不解锁，这是平台规则

---

## 🔧 常见问题

**Q: 广告一直加载失败？**
- 检查广告位 ID 是否正确
- 检查是否开通流量主
- 真机调试比模拟器稳定

**Q: 用户看完广告没解锁？**
- 检查 `onClose` 回调里的 `res.isEnded`
- 必须是 `true` 才算看完

**Q: 后端部署到哪里？**
- 推荐：阿里云/腾讯云轻量服务器（¥50/月左右）
- 或者：Vercel、Railway（免费额度）
- 最简单：微信云开发（按量付费）

---

## 📊 收益参考

假设每天有 1000 人使用：
- 30% 看广告 = 300 次观看
- 单次收益 ≈ ¥0.1
- **日收入 ≈ ¥30**
- **月收入 ≈ ¥900**

用户量越大，收益越高。

---

有问题随时问 🐾
