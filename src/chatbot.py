import gradio as gr
from .api_handler import get_chat_response  # 导入流式响应函数

# 聊天功能处理函数
def chat_with_ai(user_input, history=None):
    if history is None:
        history = []
    
    # 先给个占位符，避免 UI 没反应
    history.append((user_input, "Thinking..."))

    for partial_response in get_chat_response(user_input):  # AI 逐步生成回复
        history[-1] = (user_input, partial_response)
        yield "", history  