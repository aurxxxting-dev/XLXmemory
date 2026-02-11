#!/usr/bin/env python3
"""
小爪快速控制脚本 - 命令行版
用法: python xiaozhua_cli.py [start|restart|stop|status|backup]
"""

import subprocess
import sys
import os
from datetime import datetime


def print_banner():
    """打印欢迎横幅"""
    print("==========================================")
    print("          小爪快速控制面板")
    print("==========================================")
    print()


def run_cmd(cmd):
    """运行命令并处理编码"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=30
        )
        return result
    except Exception as e:
        print(f"[ERROR] 命令执行失败: {e}")
        return None


def start_gateway():
    """启动网关"""
    print(">>> 正在启动 OpenClaw 网关...")
    result = run_cmd("openclaw gateway start")
    if result and result.returncode == 0:
        print("[OK] 网关启动成功！")
        print("[INFO] 日志: openclaw logs --follow")
    else:
        print(f"[ERROR] 启动失败")


def stop_gateway():
    """停止网关"""
    print(">>> 正在停止 OpenClaw 网关...")
    result = run_cmd("openclaw gateway stop")
    if result and result.returncode == 0:
        print("[OK] 网关已停止")
    else:
        print(f"[ERROR] 停止失败")


def restart_gateway():
    """重启网关"""
    print(">>> 正在重启 OpenClaw 网关...")
    run_cmd("openclaw gateway stop")
    import time
    time.sleep(2)
    result = run_cmd("openclaw gateway start")
    if result and result.returncode == 0:
        print("[OK] 网关重启成功！")
    else:
        print(f"[ERROR] 重启失败")


def check_status():
    """检查状态"""
    print(">>> 正在检查 OpenClaw 状态...")
    result = run_cmd("openclaw status")
    if result:
        print(result.stdout)
        if result.stderr:
            print(f"[WARN] {result.stderr}")


def backup_self():
    """一键备份"""
    print(">>> 正在备份小爪...")
    
    workspace = os.path.expanduser("~/.openclaw/workspace")
    os.chdir(workspace)
    
    # 添加所有更改
    run_cmd("git add -A")
    
    # 提交
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    result = run_cmd(f'git commit -m "Auto backup: {timestamp}"')
    
    if result and result.returncode == 0:
        print(f"[OK] 备份完成！时间: {timestamp}")
        print("[INFO] 网络恢复后会自动推送到 GitHub")
    else:
        if result and "nothing to commit" in result.stderr.lower():
            print("[INFO] 没有需要备份的更改")
        else:
            print(f"[WARN] 可能已备份或无更改")


def show_help():
    """显示帮助"""
    print("""
用法: python xiaozhua_cli.py [命令]

命令:
    start    - 启动 OpenClaw 网关
    stop     - 停止 OpenClaw 网关
    restart  - 重启 OpenClaw 网关
    status   - 检查网关状态
    backup   - 一键备份到 git
    help     - 显示此帮助

示例:
    python xiaozhua_cli.py start
    python xiaozhua_cli.py backup

文件:
    xiaozhua_controller.py - GUI 版本 (双击运行)
    xiaozhua_cli.py        - 命令行版本
""")


def main():
    """主函数"""
    print_banner()
    
    if len(sys.argv) < 2:
        print("[?] 请提供命令参数")
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    commands = {
        "start": start_gateway,
        "stop": stop_gateway,
        "restart": restart_gateway,
        "status": check_status,
        "backup": backup_self,
        "help": show_help,
        "-h": show_help,
        "--help": show_help,
    }
    
    if command in commands:
        commands[command]()
    else:
        print(f"[ERROR] 未知命令: {command}")
        show_help()


if __name__ == "__main__":
    main()
