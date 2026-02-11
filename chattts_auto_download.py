import os
import sys

# 设置环境变量
os.environ['CHATTTS_HOME'] = r'C:\Users\Laptop\.openclaw\workspace\ChatTTS'
os.environ['HF_HOME'] = r'C:\Users\Laptop\.openclaw\workspace\ChatTTS\hf_cache'

sys.path.insert(0, r'C:\Users\Laptop\.openclaw\workspace')

try:
    print("正在导入 ChatTTS...")
    import ChatTTS
    
    print("创建 Chat 实例...")
    chat = ChatTTS.Chat()
    
    print("\n开始下载模型（从 Hugging Face）...")
    print("这可能需要几分钟，请耐心等待...\n")
    
    # 使用内置下载功能
    success = chat.load(
        source='huggingface',
        force_redownload=False,
        compile=False
    )
    
    if success:
        print("\n✓ 模型下载并加载成功！")
        
        # 测试生成语音
        text = "你好aur，我是小爪。ChatTTS模型下载成功了，现在可以生成中文语音了。"
        print(f"\n生成测试语音: {text}")
        
        import torch
        wavs = chat.infer([text])
        
        # 保存
        output_path = r'C:\Users\Laptop\.openclaw\workspace\chattts_success.wav'
        torch.save(wavs, output_path)
        print(f"✓ 语音已保存: {output_path}")
    else:
        print("\n✗ 模型加载失败")
        
except Exception as e:
    print(f"\n✗ 错误: {e}")
    import traceback
    traceback.print_exc()
