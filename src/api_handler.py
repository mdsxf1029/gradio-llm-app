import sys
import os
from config import client

# 将项目根目录添加到 sys.path 中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def get_chat_response(user_input):
    chat_completion = client.chat.completions.create(
        model="DeepSeek-R1",  # 替换为你的模型名称
        messages=[{
            "role": "user",
            "content": user_input,
        }],
        stream=True
    )

    # 流式输出结果
    response = ""
    for chunk in chat_completion:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content
            yield response  # 每次更新时返回拼接的部分