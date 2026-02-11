import sys
sys.path.insert(0, r'C:\Users\Laptop\.openclaw\workspace')

print("正在导入 ChatTTS...")
import ChatTTS

print("加载模型中...")
chat = ChatTTS.Chat()
chat.load(compile=False, source='huggingface')  # 从 huggingface 下载

print("✓ 模型加载完成！")

# 生成测试文本
texts = ["你好aur，我是小爪。这是用 ChatTTS 生成的中文语音测试。"]

print("生成语音中...")
wavs = chat.infer(texts)

# 保存
import torch
output_path = r'C:\Users\Laptop\.openclaw\workspace\chattts_test.wav'
torch.save(wavs, output_path)
print(f"✓ 语音已保存到: {output_path}")
