import os
import sys

# 设置代理（自动检测系统代理）
# 尝试常见的代理端口
proxy_ports = [7890, 1080, 8080, 33210, 33211]

proxy_set = False
for port in proxy_ports:
    # 测试代理是否可用
    test_url = f"http://127.0.0.1:{port}"
    os.environ['HTTP_PROXY'] = test_url
    os.environ['HTTPS_PROXY'] = test_url
    
    print(f"尝试代理: {test_url}")
    
    # 简单测试
    import urllib.request
    try:
        req = urllib.request.Request('https://www.google.com', method='HEAD')
        req.add_header('User-Agent', 'Mozilla/5.0')
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                print(f"✓ 代理 {port} 可用！")
                proxy_set = True
                break
    except:
        continue

if not proxy_set:
    print("自动检测代理失败，请手动设置代理地址")
    print("示例: http://127.0.0.1:7890")
    sys.exit(1)

print(f"\n使用代理: {os.environ['HTTPS_PROXY']}")
print("\n开始下载 ChatTTS 模型...\n")

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
    print(f"保存在: {downloaded_path}")
    
except Exception as e:
    print(f"\n✗ 下载失败: {e}")
    import traceback
    traceback.print_exc()
