import os
import urllib.request
import ssl

# 创建目录
save_dir = r"C:\Users\Laptop\.openclaw\workspace\ChatTTS\asset"
os.makedirs(save_dir, exist_ok=True)

# 使用国内镜像
base_url = "https://hf-mirror.com/2noise/ChatTTS/resolve/main/asset"

models = {
    "GPT.pt": "1.2GB",
    "VQ.pt": "100MB", 
    "DVAE.pt": "200MB",
    "Decoder.pt": "400MB"
}

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

print("开始下载 ChatTTS 模型（使用国内镜像）...\n")

for model, size in models.items():
    save_path = os.path.join(save_dir, model)
    if os.path.exists(save_path):
        print(f"✓ {model} 已存在，跳过")
        continue
    
    url = f"{base_url}/{model}"
    print(f"下载 {model} ({size})...")
    print(f"URL: {url}")
    
    try:
        urllib.request.urlretrieve(url, save_path)
        print(f"✓ {model} 下载完成\n")
    except Exception as e:
        print(f"✗ {model} 下载失败: {e}\n")

print("下载结束！")
