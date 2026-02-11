import os
from huggingface_hub import snapshot_download
import sys

# 设置缓存目录
local_path = r'C:\Users\Laptop\.openclaw\workspace\ChatTTS'
os.makedirs(local_path, exist_ok=True)

print("开始从 Hugging Face 下载 ChatTTS 模型...")
print(f"目标目录: {local_path}")
print("这可能需要 5-10 分钟，取决于网速...\n")

try:
    # 下载整个仓库
    downloaded_path = snapshot_download(
        repo_id="2Noise/ChatTTS",
        cache_dir=os.path.join(local_path, "cache"),
        local_dir=local_path,
        local_dir_use_symlinks=False,
        resume_download=True
    )
    
    print(f"\n✓ 下载完成！")
    print(f"模型保存在: {downloaded_path}")
    
    # 列出下载的文件
    print("\n下载的文件列表:")
    for root, dirs, files in os.walk(downloaded_path):
        for file in files:
            file_path = os.path.join(root, file)
            size_mb = os.path.getsize(file_path) / (1024 * 1024)
            rel_path = os.path.relpath(file_path, downloaded_path)
            print(f"  {rel_path}: {size_mb:.2f} MB")
    
except Exception as e:
    print(f"\n✗ 下载失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
