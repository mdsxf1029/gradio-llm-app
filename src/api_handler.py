import sys
import os

# 将项目根目录添加到 sys.path 中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from config import openai_client, qwen_client
from src.globals import current_model

def set_current_model(model_name):
    global current_model
    if model_name not in ["DeepSeek-R1", "qwen-plus"]:
        raise ValueError("Invalid model name. Choose 'DeepSeek-R1' or 'qwen-plus'.")
    current_model = model_name

def get_chat_response(user_input, state):
    # 根据用户选择调用相应的 API
    global current_model

    if current_model == "DeepSeek-R1":
        chat_completion = openai_client.chat.completions.create(
            model="DeepSeek-R1",  # 替换为你的模型名称
            messages=[{"role": "user", "content": user_input}],
            stream=True
        )
    elif current_model == "qwen-plus":
        chat_completion = qwen_client.chat.completions.create(
            model="qwen-plus",  # 替换为你的模型名称
            messages=[{"role": "user", "content": user_input}],
            stream=True
        )
    else:
        raise ValueError("No valid model selected.")

    response = ""
    for chunk in chat_completion:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content
            yield response  # 每次更新时返回拼接的部分