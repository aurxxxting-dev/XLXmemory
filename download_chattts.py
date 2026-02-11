import os
from huggingface_hub import hf_hub_download
import sys

# 创建目录
save_dir = r"C:\Users\Laptop\.openclaw\workspace\ChatTTS\asset"
os.makedirs(save_dir, exist_ok=True)

# 模型文件列表
models = [
    "asset/GPT.pt",
    "asset/VQ.pt", 
    "asset/DVAE.pt",
    "asset/Decoder.pt",
    "asset/spk_stat.pt"
]

print("开始下载 ChatTTS 模型...")
for model_path in models:
    try:
        print(f"下载 {model_path} ...")
        downloaded = hf_hub_download(
            repo_id="2noise/ChatTTS",
            filename=model_path,
            local_dir=r"C:\Users\Laptop\.openclaw\workspace\ChatTTS",
            local_dir_use_symlinks=False
        )
        print(f"✓ 完成: {downloaded}")
    except Exception as e:
        print(f"✗ 失败: {model_path} - {e}")
        sys.exit(1)

print("\n✓ 所有模型下载完成！")
