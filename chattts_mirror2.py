import os
import sys

# 使用国内镜像
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
print("Using HF mirror: https://hf-mirror.com")

# 清空旧目录
import shutil
old_path = r'C:\Users\Laptop\.openclaw\workspace\ChatTTS'
if os.path.exists(old_path):
    shutil.rmtree(old_path)
    print("Cleared old directory")

os.environ['CHATTTS_HOME'] = old_path

try:
    print("\nLoading ChatTTS...")
    import ChatTTS
    import torch
    
    chat = ChatTTS.Chat()
    
    print("\nDownloading models from mirror...")
    print("This may take 10-15 minutes...\n")
    
    success = chat.load(
        source='huggingface',
        force_redownload=True,
        compile=False
    )
    
    if success:
        print("\n[SUCCESS] Models loaded!")
        
        text = "Hello aur, this is Xiaozhua. ChatTTS is working!"
        print(f"\nGenerating: {text}")
        
        wavs = chat.infer([text])
        
        import torchaudio
        output = r'C:\Users\Laptop\.openclaw\workspace\chattts_success.wav'
        torchaudio.save(output, torch.tensor(wavs[0]).unsqueeze(0), 24000)
        print(f"[SUCCESS] Saved to: {output}")
    else:
        print("\n[ERROR] Model loading failed")
        
except Exception as e:
    print(f"\n[ERROR] {e}")
    import traceback
    traceback.print_exc()
