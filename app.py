import sys
import os
import gradio as gr
from src.chatbot import chat_with_ai  # 导入聊天逻辑函数
from src.api_handler import set_current_model  # 导入模型设置函数

# 设置Gradio界面
def launch_app():
    with gr.Blocks() as iface:
        chatbot = gr.Chatbot(label="Chat History")  # 聊天机器人显示区域
        input_box = gr.Textbox(label="Enter your message", lines=2, placeholder="Type your message...")
        state = gr.State([])  # ✅ 让 history 在会话中保持状态

        # 添加模型切换功能
        model_selector = gr.Dropdown(
            choices=["DeepSeek-R1", "qwen-plus"],  # 模型选项
            value="qwen-plus",  # 默认值
            label="Select Model",
        )
        model_selector.change(set_current_model, inputs=model_selector, outputs=[])

        # 设置点击按钮时触发的事件
        send_button = gr.Button("Send")
        send_button.click(chat_with_ai, inputs=[input_box, state], outputs=[input_box, chatbot])

    iface.launch(share=False, server_name="127.0.0.1", server_port=7860, show_error=True)

if __name__ == "__main__":
    launch_app()