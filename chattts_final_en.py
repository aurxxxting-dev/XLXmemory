import os
import sys

# 设置模型路径
os.environ['CHATTTS_HOME'] = r'C:\Users\Laptop\.openclaw\workspace\ChatTTS'
os.chdir(r'C:\Users\Laptop\.openclaw\workspace')

sys.path.insert(0, r'C:\Users\Laptop\.openclaw\workspace')

try:
    print("Loading ChatTTS...")
    import ChatTTS
    import torch
    import torchaudio
    
    print("Creating Chat instance...")
    chat = ChatTTS.Chat()
    
    print("Loading local models...")
    success = chat.load(
        source='custom',
        custom_path=r'C:\Users\Laptop\.openclaw\workspace\ChatTTS',
        compile=False
    )
    
    if not success:
        print("Model loading failed")
        sys.exit(1)
    
    print("Model loaded successfully!")
    
    # Generate weather forecast
    text = "Hello aur, this is Xiaozhua. Chengdu today is sunny with temperature 5 to 14 degrees. Have a nice day!"
    
    print(f"Generating speech...")
    wavs = chat.infer([text])
    
    # Save as wav
    output_path = r'C:\Users\Laptop\.openclaw\workspace\chattts_weather_final.wav'
    torchaudio.save(output_path, torch.tensor(wavs[0]).unsqueeze(0), 24000)
    
    print(f"Success! Saved to: {output_path}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
