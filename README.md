# 项目名称

简要描述你的项目（例如：python学习源码）。

## 📦 依赖

本项目使用 Python 标准库 + 以下第三方库（如有）：

- `requests`：用于网络请求（示例）
- `rich`：美化终端输出

> 💡 如果只用标准库，可删除以上内容。

## 🚀 快速开始

### 环境要求
- Python 3.7 或更高版本
- Windows / macOS / Linux

### 安装依赖（Windows）

1. 克隆本项目：
   ```bash
   git clone https://github.com/hao1234good1234/python-demo
   cd your-project

2. windows一键安装脚本，运行安装脚本（自动创建虚拟环境 + 安装依赖）：
   install.bat

   如果是在单个依赖后面安装：
   pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple/

3. macOS / Linux安装依赖
   # 创建虚拟环境
   python -m venv venv

   # 激活
   source venv/bin/activate

   # 安装依赖（使用清华源）
   pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

4. 运行项目
   # Windows
    venv\Scripts\activate && python main.py

   # macOS / Linux
    source venv/bin/activate && python main.py
5. 📁 项目结构（模版）
    your-project/
    ├── main.py              # 主程序入口
    ├── core/                # 核心模块（可选）
    ├── requirements.txt     # 依赖清单
    ├── install.bat          # Windows 安装脚本
    └── README.md            # 本文件