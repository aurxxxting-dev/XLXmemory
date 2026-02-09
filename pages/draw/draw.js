// pages/draw/draw.js
// 抽签页面 - 包含激励视频广告

Page({
  data: {
    // 抽签结果
    drawResult: null,
    // 是否已解锁详细解签
    isUnlocked: false,
    // 广告是否加载中
    adLoading: false
  },

  // 激励视频广告实例
  rewardedVideoAd: null,

  onLoad() {
    // 初始化激励视频广告
    this.initRewardedAd()
  },

  // ========== 1. 初始化广告 ==========
  initRewardedAd() {
    // 替换为你的广告位 ID（在微信公众平台 - 流量主里申请）
    const adUnitId = 'adunit-xxxxxxxxx'
    
    // 创建激励视频广告实例
    this.rewardedVideoAd = wx.createRewardedVideoAd({
      adUnitId: adUnitId
    })

    // 监听广告加载成功
    this.rewardedVideoAd.onLoad(() => {
      console.log('广告加载成功')
      this.setData({ adLoading: false })
    })

    // 监听广告加载失败
    this.rewardedVideoAd.onError((err) => {
      console.error('广告加载失败', err)
      wx.showToast({ title: '广告加载失败', icon: 'none' })
      this.setData({ adLoading: false })
    })

    // 监听广告关闭（用户看完或中途退出）
    this.rewardedVideoAd.onClose((res) => {
      // isEnded: true = 看完, false = 中途退出
      if (res && res.isEnded) {
        // 用户看完了，解锁内容！
        this.unlockContent()
      } else {
        // 用户中途退出，没看完不算数
        wx.showToast({ title: '需要看完才能解锁哦', icon: 'none' })
      }
    })
  },

  // ========== 2. 摇一摇抽签 ==========
  onShake() {
    // 摇手机触发（这里用按钮模拟）
    wx.vibrateShort() // 震动反馈
    
    // 模拟抽签结果
    const results = ['大吉', '中吉', '小吉', '凶', '大凶']
    const result = results[Math.floor(Math.random() * results.length)]
    
    this.setData({
      drawResult: result,
      isUnlocked: false // 重新抽签后重置解锁状态
    })
  },

  // ========== 3. 点击"看视频解锁" ==========
  onUnlockClick() {
    // 检查广告实例
    if (!this.rewardedVideoAd) {
      wx.showToast({ title: '广告未准备好', icon: 'none' })
      return
    }

    this.setData({ adLoading: true })

    // 显示激励视频广告
    this.rewardedVideoAd.show()
      .then(() => {
        console.log('广告显示成功')
      })
      .catch(() => {
        // 如果显示失败，尝试重新加载再显示
        this.rewardedVideoAd.load()
          .then(() => this.rewardedVideoAd.show())
          .catch(err => {
            console.error('广告显示失败', err)
            wx.showToast({ title: '广告加载失败，请重试', icon: 'none' })
            this.setData({ adLoading: false })
          })
      })
  },

  // ========== 4. 解锁内容（看完广告后调用）==========
  unlockContent() {
    this.setData({ isUnlocked: true })
    
    // 这里调用你的 Gemini API 解签
    this.getAIInterpretation()
    
    wx.showToast({ title: '解锁成功！', icon: 'success' })
  },

  // ========== 5. 调用 Gemini API 解签 ==========
  async getAIInterpretation() {
    const { drawResult } = this.data
    
    wx.showLoading({ title: 'AI解签中...' })

    try {
      // 调用你的后端 API（不要直接在前端调 Gemini，会暴露 API Key）
      const res = await wx.request({
        url: 'https://你的服务器.com/api/interpret', // 你的后端接口
        method: 'POST',
        data: {
          sign: drawResult,
          userId: wx.getStorageSync('userId') || ''
        }
      })

      if (res.data && res.data.interpretation) {
        this.setData({
          aiResult: res.data.interpretation
        })
      }
    } catch (err) {
      console.error('解签失败', err)
      wx.showToast({ title: '解签失败，请重试', icon: 'none' })
    } finally {
      wx.hideLoading()
    }
  }
})
