import sys
import os
import gradio as gr

# 将项目根目录添加到 sys.path 中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.api_handler import get_chat_response  # 导入流式响应函数

# 聊天功能处理函数
def chat_with_ai(user_input, state=None):
    if state is None:
        state = []

    print(f"State type: {type(state)}")  # 调试信息

    # 添加用户输入到对话历史
    state.append((user_input, "Thinking..."))

    # 调用 get_chat_response，逐步生成回复
    for partial_response in get_chat_response(user_input, state):
        state[-1] = (user_input, partial_response)  # 更新最后一条记录的回复
        yield "", state

    # 最终返回完整的对话历史
    yield "", state
