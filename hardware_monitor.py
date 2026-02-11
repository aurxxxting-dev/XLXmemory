#!/usr/bin/env python3
"""
小爪硬件温度监控
读取 Open Hardware Monitor 的传感器数据
"""

import subprocess
import sys

OHM_PATH = r"C:\Program Files\OpenHardwareMonitor\OpenHardwareMonitor.exe"


def check_ohm_running():
    """检查 OHM 是否运行"""
    result = subprocess.run(
        "tasklist | findstr OpenHardwareMonitor",
        shell=True,
        capture_output=True,
        text=True
    )
    return "OpenHardwareMonitor" in result.stdout


def start_ohm():
    """启动 OHM"""
    print(">>> 启动 Open Hardware Monitor...")
    subprocess.Popen(
        [OHM_PATH],
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    print(">>> 已启动，等待几秒初始化...")
    import time
    time.sleep(3)


def get_temperatures():
    """通过 WMIC 读取温度"""
    try:
        # 读取 OHM 的 WMI 数据
        result = subprocess.run(
            'wmic /namespace:\\\\root\\\\OpenHardwareMonitor PATH Sensor WHERE "SensorType=\'Temperature\'" GET Name,Value,Max',
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=10
        )
        return result.stdout
    except Exception as e:
        return f"读取失败: {e}"


def main():
    print("==========================================")
    print("          小爪硬件温度监控")
    print("==========================================")
    print()
    
    # 检查并启动 OHM
    if not check_ohm_running():
        start_ohm()
    else:
        print(">>> Open Hardware Monitor 已在运行")
    
    print()
    print(">>> 读取温度数据...")
    print()
    
    data = get_temperatures()
    print(data)
    
    print()
    print(">>> 提示: OHM 正在后台运行，随时可以读取温度")
    print(">>> 软件位置: C:\\Program Files\\OpenHardwareMonitor\\")


if __name__ == "__main__":
    main()
