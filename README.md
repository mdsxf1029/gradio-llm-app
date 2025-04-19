# Gradio LLM 聊天界面应用

本项目基于 [Gradio](https://www.gradio.app/) 实现了一个支持多模型切换和多轮对话的聊天界面应用。用户可以与不同的大语言模型进行自然语言交流，并在同一对话窗口内进行连续多轮问答。

## 📁 项目结构

```
├── app.py                # 项目主入口，初始化程序运行
├── ui.py                 # 定义 Gradio UI 和交互逻辑
├── src/                  # 模块功能代码
│   ├── api_handler.py    # 模拟 API 调用，实现模型切换
│   ├── chatbot.py        # 聊天逻辑与多轮对话处理
│   ├── globals.py        # 存放全局变量
├── requirements.txt      # 项目依赖文件
├── config.py             # 存放 API key
├── .gitignore            # Git 忽略文件配置
├── README.md             # 项目说明文件（本文件）
```

## 🚀 运行方式

1. **克隆项目：**

```bash
git clone https://github.com/mdsxf1029/gradio-llm-app.git
cd gradio-llm-app
```

2. **安装依赖：**

```bash
pip install -r requirements.txt
```

3. **启动项目：**

```bash
python app.py
```

4. 打开浏览器访问 http://127.0.0.1:7860，即可开始对话。