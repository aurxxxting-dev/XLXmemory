import sys
import os
import traceback

# 设置模型路径
os.environ['CHATTTS_HOME'] = r'C:\Users\Laptop\.openclaw\workspace\ChatTTS'

try:
    print("正在加载 ChatTTS...")
    import torch
    import torchaudio
    
    # 直接加载模型
    from ChatTTS.core import Chat
    
    print("初始化 ChatTTS...")
    chat = Chat()
    chat.load_models(
        source='local',
        local_path=r'C:\Users\Laptop\.openclaw\workspace\ChatTTS'
    )
    
    print("✓ 模型加载完成！")
    
    # 生成中文语音
    text = "你好aur，我是小爪。这是用ChatTTS本地生成的中文语音，希望这次效果让你满意。成都今天天气晴朗，气温5到14度，适合出门活动。"
    
    print(f"\n生成语音: {text[:30]}...")
    
    # 生成音频
    wavs = chat.infer([text], do_text_normalization=True)
    
    # 保存
    output_path = r'C:\Users\Laptop\.openclaw\workspace\chattts_weather.wav'
    torchaudio.save(output_path, torch.tensor(wavs[0]).unsqueeze(0), 24000)
    
    print(f"✓ 语音已保存: {output_path}")
    
except Exception as e:
    print(f"\n✗ 错误: {e}")
    traceback.print_exc()
