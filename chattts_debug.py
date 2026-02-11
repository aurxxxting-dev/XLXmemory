import sys
sys.path.insert(0, r'C:\Users\Laptop\.openclaw\workspace')

try:
    print("正在导入 ChatTTS...")
    import ChatTTS
    print("✓ ChatTTS 导入成功")
    
    print("\n加载模型中...")
    chat = ChatTTS.Chat()
    chat.load(compile=False, source='huggingface')
    print("✓ 模型加载完成！")
    
    # 生成测试文本
    texts = ["你好aur，我是小爪。这是用 ChatTTS 生成的中文语音测试。"]
    
    print("\n生成语音中...")
    wavs = chat.infer(texts)
    
    # 保存
    import torch
    output_path = r'C:\Users\Laptop\.openclaw\workspace\chattts_test.wav'
    torch.save(wavs, output_path)
    print(f"✓ 语音已保存到: {output_path}")
    
except Exception as e:
    print(f"\n✗ 错误: {e}")
    import traceback
    traceback.print_exc()
