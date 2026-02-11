import os
import sys

# 设置模型路径
os.environ['CHATTTS_HOME'] = r'C:\Users\Laptop\.openclaw\workspace\ChatTTS'
os.chdir(r'C:\Users\Laptop\.openclaw\workspace')

sys.path.insert(0, r'C:\Users\Laptop\.openclaw\workspace')

try:
    print("正在导入 ChatTTS...")
    import ChatTTS
    import torch
    import torchaudio
    
    print("创建 Chat 实例...")
    chat = ChatTTS.Chat()
    
    print("\n加载本地模型...")
    success = chat.load(
        source='custom',
        custom_path=r'C:\Users\Laptop\.openclaw\workspace\ChatTTS',
        compile=False
    )
    
    if not success:
        print("✗ 模型加载失败")
        sys.exit(1)
    
    print("✓ 模型加载成功！\n")
    
    # 生成中文天气预报
    text = "你好aur，我是小爪。这是用ChatTTS本地生成的中文语音。成都今天天气晴朗，气温5到14度，非常适合出门活动。记得根据温差增减衣物哦。祝你今天愉快！"
    
    print(f"生成语音: {text[:50]}...")
    wavs = chat.infer([text])
    
    # 保存为 wav
    output_path = r'C:\Users\Laptop\.openclaw\workspace\chattts_weather_final.wav'
    torchaudio.save(output_path, torch.tensor(wavs[0]).unsqueeze(0), 24000)
    
    print(f"\n✓ 语音生成成功！")
    print(f"保存位置: {output_path}")
    
except Exception as e:
    print(f"\n✗ 错误: {e}")
    import traceback
    traceback.print_exc()
