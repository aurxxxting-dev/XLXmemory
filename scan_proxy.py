import socket
import os

# 常见代理端口
proxy_ports = [7890, 7891, 10808, 10809, 1080, 8080, 3128, 9090, 8118]

print("正在扫描本地代理端口...\n")

working_proxy = None

for port in proxy_ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex(('127.0.0.1', port))
        sock.close()
        
        if result == 0:
            print(f"✓ 端口 {port} 开放")
            working_proxy = f"http://127.0.0.1:{port}"
        else:
            print(f"✗ 端口 {port} 未开放")
    except:
        print(f"✗ 端口 {port} 检查失败")

if working_proxy:
    print(f"\n发现可用代理: {working_proxy}")
    os.environ['HTTP_PROXY'] = working_proxy
    os.environ['HTTPS_PROXY'] = working_proxy
    print("\n已设置环境变量，现在可以下载了！")
else:
    print("\n没找到本地代理端口")
    print("可能VPN是全局模式，试试不用代理直接下载？")
