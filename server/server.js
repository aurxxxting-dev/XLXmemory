// server.js
// 后端服务 - 调用 Gemini API 解签

const express = require('express');
const { GoogleGenAI } = require('@google/genai');

const app = express();
app.use(express.json());

// 你的 Gemini API Key（只在服务端保存）
const GEMINI_API_KEY = process.env.GEMINI_API_KEY || '你的API_KEY';
const ai = new GoogleGenAI({ apiKey: GEMINI_API_KEY });

// 解签接口
app.post('/api/interpret', async (req, res) => {
  try {
    const { sign, userId } = req.body;
    
    if (!sign) {
      return res.status(400).json({ error: '缺少签文参数' });
    }

    // 构造提示词
    const prompt = `你是一位精通易经、八字的解签大师。

用户抽到了：${sign}

请从以下几个方面详细解读这个签文：
1. 签文整体寓意
2. 事业运势
3. 爱情/人际关系
4. 财运
5. 今日建议

语气要温和、积极，即使抽到凶签也要给出建设性的建议。
用中文回答，控制在300字左右。`;

    // 调用 Gemini
    const response = await ai.models.generateContent({
      model: 'gemini-2.0-flash',
      contents: prompt,
    });

    const interpretation = response.text;

    res.json({
      success: true,
      sign: sign,
      interpretation: interpretation,
      // 可以在这里记录用户看了广告的数据，用于分析
      userId: userId || 'anonymous'
    });

  } catch (error) {
    console.error('解签失败:', error);
    res.status(500).json({
      error: '解签服务暂时不可用',
      message: error.message
    });
  }
});

// 健康检查
app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`解签服务运行在端口 ${PORT}`);
});

/*
部署说明：
1. 安装依赖: npm install express @google/genai
2. 设置环境变量: export GEMINI_API_KEY=你的API_KEY
3. 运行: node server.js
4. 微信小程序请求地址改成你的服务器地址

注意：
- 这个服务需要部署到公网服务器（阿里云、腾讯云等）
- 域名需要备案才能在微信小程序中使用
- 或者使用云开发（wx.cloud.callFunction）
*/
