# src/ui.py

import gradio as gr
from src.chatbot import chat_with_ai  # 导入聊天逻辑函数
from src.globals import current_model
from src.api_handler import set_current_model  # 导入设置模型函数

# 构建美化后的 Gradio 用户界面
def build_ui():
    """构建 Gradio 前端界面，添加美化效果和交互功能"""
    
    # 设置页面样式
    custom_css = """
    #chatbot {
        background-color: #f0f0f5;
        padding: 10px;
        border-radius: 8px;
        font-family: 'Arial', sans-serif;
    }
    .gradio-container {
        background-color: #f7f8fc;
    }
    .gr-button {
        background-color: #4CAF50;
        color: white;
    }
    .gr-button:hover {
        background-color: #45a049;
    }
    .gr-dropdown {
        font-size: 16px;
    }
    .gr-textbox {
        font-size: 14px;
        border-radius: 10px;
    }
    """
    
    with gr.Blocks(css=custom_css) as iface:
        # 页面欢迎信息
        gr.Markdown("<h1 style='text-align: center; color: #4CAF50;'>🤖 Welcome to LLM Chatbot!</h1>")
        gr.Markdown("<h3 style='text-align: center; color: #FFC0CB;'>Select a model and start chatting!")

        # 模型选择下拉框
        model_selector = gr.Dropdown(
            choices=["DeepSeek-R1", "qwen-plus"],  # 模型选项
            value="DeepSeek-R1",  # 默认值
            label="Select Model",
            elem_id="model_selector"
        )

        # 显示聊天记录
        chatbot = gr.Chatbot(label="Chat History", elem_id="chatbot", height=400)

        # 用户输入框
        input_box = gr.Textbox(label="Enter your message", lines=2, placeholder="Type your message...", elem_id="input_box")

        # 状态保持
        state = gr.State([])
        with gr.Row():  # 使用 Row 来将按钮放在一行
            # 发送按钮
            send_button = gr.Button("Send", elem_id="send_button",variant="primary")
            # 清空聊天记录按钮
            clear_button = gr.Button("Clear Chat", elem_id="clear_button", variant="secondary")

        # 选择模型后更新当前模型
        model_selector.change(set_current_model, inputs=model_selector, outputs=[])

        # 清空聊天记录函数
        def clear_chat():
            return "", []  # 清空聊天记录

        # 点击清空按钮清除聊天记录
        clear_button.click(clear_chat, inputs=[], outputs=[chatbot, state])
        
        # 点击按钮发送消息并更新聊天记录
        send_button.click(chat_with_ai, inputs=[input_box, state], outputs=[input_box, chatbot])

        # 启动界面
        iface.launch(share=False, server_name="127.0.0.1", server_port=7860, show_error=True)

    return iface
