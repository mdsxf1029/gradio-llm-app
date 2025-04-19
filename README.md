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

2. **创建虚拟环境：**
在项目目录下，使用 `venv` 创建一个虚拟环境。

```bash
python -m venv venv
```

3. **激活虚拟环境：**
在 Windows 上，使用以下命令来激活虚拟环境：

```bash
.\venv\Scripts\activate
```

4. **安装依赖：**

```bash
pip install -r requirements.txt
```

5. **配置 API key：**
在 `config.py` 文件中，设置你所使用模型的 API key。示例：

```python
api_key = "your_api_key_here",   # 替换为你的API密钥
base_url = "your_base_url_here"
```

6. **启动项目：**

```bash
python app.py
```

7. 打开浏览器访问 http://127.0.0.1:7860 ，即可开始对话。