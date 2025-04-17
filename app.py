import sys
import os
import gradio as gr
from src.ui import build_ui  # 从 ui.py 引入构建界面的方法

# 设置Gradio界面
def launch_app():
    """启动 Gradio 应用"""
    iface = build_ui()  # 构建 Gradio 界面
    iface.launch(share=False, server_name="127.0.0.1", server_port=7860, show_error=True)

if __name__ == "__main__":
    launch_app()