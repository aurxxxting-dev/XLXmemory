import os
import sys

os.environ['CHATTTS_HOME'] = r'C:\Users\Laptop\.openclaw\workspace\ChatTTS'
os.chdir(r'C:\Users\Laptop\.openclaw\workspace')

try:
    print("Loading ChatTTS...")
    import ChatTTS
    import torch
    
    chat = ChatTTS.Chat()
    
    print("\nTrying to load with local files...")
    # 尝试加载本地模型，不强制检查完整性
    chat.load(
        source='local',
        custom_path=r'C:\Users\Laptop\.openclaw\workspace\ChatTTS',
        compile=False,
        force_redownload=False
    )
    
    print("Model loaded!")
    
    # 生成测试
    text = "你好aur，我是小爪。ChatTTS终于运行成功了！"
    print(f"\nGenerating: {text}")
    
    wavs = chat.infer([text])
    
    # 保存
    import torchaudio
    output = r'C:\Users\Laptop\.openclaw\workspace\chattts_success.wav'
    torchaudio.save(output, torch.tensor(wavs[0]).unsqueeze(0), 24000)
    print(f"Saved to: {output}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
