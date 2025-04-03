import sys
import os
import gradio as gr
from src.chatbot import chat_with_ai  # 导入聊天逻辑函数

# 设置Gradio界面
def launch_app():
    with gr.Blocks() as iface:
        chatbot = gr.Chatbot(label="Chat History")  # 聊天机器人显示区域
        input_box = gr.Textbox(label="Enter your message", lines=2, placeholder="Type your message...")
        state = gr.State([])  # ✅ 让 history 在会话中保持状态

        # 设置点击按钮时触发的事件
        send_button = gr.Button("Send")
        send_button.click(chat_with_ai, inputs=[input_box, state], outputs=[input_box, chatbot])

    iface.launch()

if __name__ == "__main__":
    launch_app()