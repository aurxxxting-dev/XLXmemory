import os

# 设置代理
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10080'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10080'

print(f"使用代理: {os.environ['HTTPS_PROXY']}")
print("\n开始下载 ChatTTS 模型...")
print("这可能需要 10-15 分钟，取决于网速...\n")

from huggingface_hub import snapshot_download

local_path = r'C:\Users\Laptop\.openclaw\workspace\ChatTTS'
os.makedirs(local_path, exist_ok=True)

try:
    downloaded_path = snapshot_download(
        repo_id="2Noise/ChatTTS",
        cache_dir=os.path.join(local_path, "cache"),
        local_dir=local_path,
        local_dir_use_symlinks=False,
        resume_download=True
    )
    
    print(f"\n✓ 下载完成！")
    print(f"模型保存在: {downloaded_path}")
    
except Exception as e:
    print(f"\n✗ 下载失败: {e}")
    import traceback
    traceback.print_exc()
