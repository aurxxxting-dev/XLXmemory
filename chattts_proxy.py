import os
import sys

# 设置代理
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10080'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10080'
print(f"Using proxy: {os.environ['HTTPS_PROXY']}")

# 清空旧目录
import shutil
old_path = r'C:\Users\Laptop\.openclaw\workspace\ChatTTS'
if os.path.exists(old_path):
    shutil.rmtree(old_path)
    print(f"Cleared old directory")

os.environ['CHATTTS_HOME'] = old_path
os.environ['HF_HOME'] = os.path.join(old_path, 'cache')

try:
    print("\nLoading ChatTTS...")
    import ChatTTS
    import torch
    
    chat = ChatTTS.Chat()
    
    print("\nDownloading models from HuggingFace...")
    print("This may take 10-15 minutes...\n")
    
    success = chat.load(
        source='huggingface',
        force_redownload=True,
        compile=False
    )
    
    if success:
        print("\n✓ Models loaded successfully!")
        
        text = "你好aur，我是小爪。ChatTTS运行成功了！"
        print(f"\nGenerating: {text}")
        
        wavs = chat.infer([text])
        
        import torchaudio
        output = r'C:\Users\Laptop\.openclaw\workspace\chattts_success.wav'
        torchaudio.save(output, torch.tensor(wavs[0]).unsqueeze(0), 24000)
        print(f"✓ Saved to: {output}")
    else:
        print("\n✗ Model loading failed")
        
except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
