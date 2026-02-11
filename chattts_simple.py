import os
import sys

# 添加路径
sys.path.insert(0, r'C:\Users\Laptop\.openclaw\workspace')
os.environ['CHATTTS_HOME'] = r'C:\Users\Laptop\.openclaw\workspace\ChatTTS'

try:
    print("导入 ChatTTS...")
    import ChatTTS
    
    print("创建实例...")
    chat = ChatTTS.Chat()
    
    print("加载模型...")
    chat.load_models(source='local', local_path=r'C:\Users\Laptop\.openclaw\workspace\ChatTTS')
    
    print("✓ 模型加载成功！")
    
    # 生成语音
    text = "你好aur，我是小爪。这是用ChatTTS生成的中文语音测试。"
    print(f"生成: {text}")
    
    wavs = chat.infer([text])
    
    # 保存
    import torch
    output = r'C:\Users\Laptop\.openclaw\workspace\chattts_result.wav'
    torch.save(wavs, output)
    print(f"✓ 已保存: {output}")
    
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
