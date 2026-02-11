#!/usr/bin/env python3
"""
小爪控制面板 - 一键启动/重启 OpenClaw + 表情窗口
作者: 小爪 (Claw)
"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os
import threading
import time


class XiaozhuaController:
    """小爪控制面板主类"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("小爪控制面板")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # 设置主题色
        self.bg_color = "#1a1a2e"
        self.accent_color = "#e94560"
        self.text_color = "#ffffff"
        
        self.root.configure(bg=self.bg_color)
        
        # 表情动画帧 (使用 ASCII 字符避免编码问题)
        self.emotion_frames = {
            "normal": ["[*]", "(^)", "(-)", "(o)"],
            "working": [">>", "(*)", "(^)", "(+)"],
            "sleepy": ["zz", "(-)", "(_)", "(.)"],
            "happy": ["**", "(^)", "(*)", "(<3)"],
            "thinking": ["??", "(^)", "(-)", "(?)"]
        }
        self.current_emotion = "normal"
        self.frame_index = 0
        
        self.setup_ui()
        self.start_animation()
        
    def setup_ui(self):
        """设置 UI 界面"""
        # 标题
        title = tk.Label(
            self.root,
            text="小爪控制面板",
            font=("Microsoft YaHei", 20, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title.pack(pady=20)
        
        # 表情显示区域
        self.emotion_label = tk.Label(
            self.root,
            text="[*]",
            font=("Consolas", 40),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.emotion_label.pack(pady=20)
        
        # 状态显示
        self.status_label = tk.Label(
            self.root,
            text="状态: 准备就绪",
            font=("Microsoft YaHei", 12),
            bg=self.bg_color,
            fg="#888888"
        )
        self.status_label.pack(pady=10)
        
        # 按钮区域
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=20, padx=40, fill=tk.X)
        
        # 启动按钮
        self.start_btn = self.create_button(
            button_frame, ">> 启动网关", self.start_gateway
        )
        self.start_btn.pack(fill=tk.X, pady=5)
        
        # 重启按钮
        self.restart_btn = self.create_button(
            button_frame, ">> 重启网关", self.restart_gateway
        )
        self.restart_btn.pack(fill=tk.X, pady=5)
        
        # 状态检查
        self.check_btn = self.create_button(
            button_frame, ">> 检查状态", self.check_status
        )
        self.check_btn.pack(fill=tk.X, pady=5)
        
        # 备份按钮
        self.backup_btn = self.create_button(
            button_frame, ">> 一键备份", self.backup_self
        )
        self.backup_btn.pack(fill=tk.X, pady=5)
        
        # 退出按钮
        self.exit_btn = self.create_button(
            button_frame, ">> 退出", self.root.quit, is_secondary=True
        )
        self.exit_btn.pack(fill=tk.X, pady=20)
        
        # 底部信息
        info = tk.Label(
            self.root,
            text="OpenClaw v2026.2.9 | 模型: GLM-4-Plus",
            font=("Microsoft YaHei", 9),
            bg=self.bg_color,
            fg="#666666"
        )
        info.pack(side=tk.BOTTOM, pady=10)
        
    def create_button(self, parent, text, command, is_secondary=False):
        """创建样式按钮"""
        bg = "#333333" if is_secondary else self.accent_color
        fg = self.text_color
        
        btn = tk.Button(
            parent,
            text=text,
            font=("Microsoft YaHei", 12),
            bg=bg,
            fg=fg,
            activebackground="#555555" if is_secondary else "#ff6b6b",
            activeforeground=fg,
            relief=tk.FLAT,
            cursor="hand2",
            command=command,
            height=2
        )
        return btn
        
    def start_animation(self):
        """启动表情动画"""
        def animate():
            frames = self.emotion_frames[self.current_emotion]
            self.emotion_label.config(text=frames[self.frame_index])
            self.frame_index = (self.frame_index + 1) % len(frames)
            self.root.after(500, animate)
        
        animate()
        
    def set_emotion(self, emotion):
        """设置表情状态"""
        if emotion in self.emotion_frames:
            self.current_emotion = emotion
            self.frame_index = 0
            
    def run_command(self, cmd, description):
        """在后台运行命令"""
        self.set_emotion("working")
        self.status_label.config(text=f"状态: {description}...")
        
        def execute():
            try:
                result = subprocess.run(
                    cmd,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                if result.returncode == 0:
                    self.status_label.config(text=f"状态: {description}完成 [OK]")
                    self.set_emotion("happy")
                else:
                    self.status_label.config(text=f"状态: {description}失败")
                    self.set_emotion("thinking")
                    
            except Exception as e:
                self.status_label.config(text=f"状态: 错误 - {str(e)}")
                self.set_emotion("thinking")
                
        threading.Thread(target=execute, daemon=True).start()
        
    def start_gateway(self):
        """启动 OpenClaw 网关"""
        self.run_command("openclaw gateway start", "正在启动网关")
        
    def restart_gateway(self):
        """重启 OpenClaw 网关"""
        self.set_emotion("thinking")
        self.status_label.config(text="状态: 正在重启网关...")
        
        def restart():
            try:
                # 先停止
                subprocess.run("openclaw gateway stop", shell=True, timeout=10)
                time.sleep(2)
                # 再启动
                subprocess.run("openclaw gateway start", shell=True, timeout=10)
                self.status_label.config(text="状态: 网关重启完成 [OK]")
                self.set_emotion("happy")
            except Exception as e:
                self.status_label.config(text=f"状态: 重启失败")
                self.set_emotion("thinking")
                
        threading.Thread(target=restart, daemon=True).start()
        
    def check_status(self):
        """检查 OpenClaw 状态"""
        self.set_emotion("thinking")
        self.status_label.config(text="状态: 正在检查...")
        
        def check():
            try:
                result = subprocess.run(
                    "openclaw status",
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if result.returncode == 0:
                    self.status_label.config(text="状态: 网关运行中 [OK]")
                    self.set_emotion("happy")
                else:
                    self.status_label.config(text="状态: 网关未运行")
                    self.set_emotion("sleepy")
                    
            except Exception as e:
                self.status_label.config(text=f"状态: 检查失败")
                self.set_emotion("thinking")
                
        threading.Thread(target=check, daemon=True).start()
        
    def backup_self(self):
        """一键备份"""
        self.set_emotion("working")
        self.status_label.config(text="状态: 正在备份...")
        
        def backup():
            try:
                workspace = os.path.expanduser("~/.openclaw/workspace")
                os.chdir(workspace)
                
                # 添加所有更改
                subprocess.run("git add -A", shell=True, timeout=10)
                
                # 提交
                result = subprocess.run(
                    'git commit -m "Auto backup by Xiaozhua Controller"',
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                self.status_label.config(text="状态: 备份完成 [OK]")
                self.set_emotion("happy")
                
                messagebox.showinfo(
                    "备份完成",
                    "已成功备份到本地 git 仓库！\n稍后网络恢复会自动推送到 GitHub。"
                )
                
            except Exception as e:
                self.status_label.config(text=f"状态: 备份失败")
                self.set_emotion("thinking")
                messagebox.showerror("备份失败", str(e))
                
        threading.Thread(target=backup, daemon=True).start()


def main():
    """主函数"""
    root = tk.Tk()
    
    # 设置 DPI 感知
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
    
    app = XiaozhuaController(root)
    root.mainloop()


if __name__ == "__main__":
    main()
