"""
模块与包（Modules and Packages）
"""

# **模块 = 一个 `.py` 文件**  
# **包 = 一个包含 `__init__.py` 的文件夹（里面可以有很多模块）**  


# ✅ **好处：**

# - 代码复用（`validators.py` 可被多个项目用）
# - 团队协作（每人负责一个模块）
# - 易于测试和维护

# 二、模块（Module）：一个 `.py` 文件就是一个模块
# 示例：创建 `math_utils.py`
# def add(a, b):
#     return a + b
# def multiply(a, b):
#     return a * b
# PI = 3.14159
# 在其他文件中使用：
#main.py
# import math_utils
# print(math_utils.add(3, 9))
# print(math_utils.multiply(3, 2))
# print(math_utils.PI)

# 🔸 导入方式（4 种常用）
# | 写法                         | 说明                     | 适用场景                                  |
# | ---------------------------- | ------------------------ | ----------------------------------------- |
# | `import math_utils`          | 导入整个模块             | 推荐！命名空间清晰                        |
# | `from math_utils import add` | 只导入 `add` 函数        | 减少打字，但小心命名冲突                  |
# | `from math_utils import *`   | 导入所有（**不推荐！**） | 会污染命名空间，难以追踪来源              |
# | `import math_utils as mu`    | 起别名                   | 模块名太长时用（如 `import numpy as np`） |
# ✅ **最佳实践：优先用 `import module` 或 `from module import specific_func`**

# 🗂️ 三、包（Package）：带 `__init__.py` 的文件夹
# 创建一个包：`mytools/`
# mytools/
# ├── __init__.py   ← 关键！标识这是一个包
# ├── file_ops.py
# └── validators.py
# 🔸 `__init__.py` 可以是空文件，也可以包含初始化代码
# 使用包中的模块：
# 方式1：直接导入模块
# from mytools import file_ops
# file_ops.save_json(...)

# 方式2：导入具体的函数
# from mytools.validators import is_valid_email

# 🌟 四、`__init__.py` 的妙用（不只是空文件！）
# 1. **控制 `from package import *` 的行为**
# mytools/__init__.py
# from .file_ops import save_json, load_json
# from .validators import is_valid_email
# 定义 __all__，指定哪些能被 import *
# __all__ = ["save_json", "load_json", "is_valid_email"]
# 现在用户可以：
# from mytools import *  # 只导入 __all__ 中的内容

# 2. **简化导入路径（提供“快捷方式”）**
# mytools/__init__.py
# from .file_ops import save_json
# from .validators import is_valid_email

# 用户可以直接：
# from mytools import save_json, is_valid_email
# 而不用写：from mytools.file_ops import save_json
# ✅ 这是专业库（如 `requests`, `flask`）的常见做法！


# 🧪 五、实战项目：重构你的“通讯录”
# 项目结构
# contact_app/
# ├── main.py
# └── core/
#     ├── __init__.py
#     ├── storage.py      # 负责 JSON 读写
#     └── contacts.py     # 负责业务逻辑

# 步骤 1：`core/storage.py`

# core/storage.py
# import json
# from pathlib import Path

# DATA_FILE = Path("contacts.json")

# def load_contacts():
#     if not DATA_FILE.exists():
#         return {}
#     with open(DATA_FILE, "r", encoding="utf-8") as f:
#         return json.load(f)

# def save_contacts(data):
#     with open(DATA_FILE, "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)

# 步骤 2：`core/contacts.py`
# core/contacts.py
# from .storage import load_contacts, save_contacts

# def add_contact(name, phone):
#     contacts = load_contacts()
#     contacts[name] = phone
#     save_contacts(contacts)

# def get_all_contacts():
#     return load_contacts()

# 步骤 3：`core/__init__.py`
# core/__init__.py
# from .contacts import add_contact, get_all_contacts

# __all__ = ["add_contact", "get_all_contacts"]

# 步骤 4：`main.py`
# main.py
# from core import add_contact, get_all_contacts

# add_contact("王五", "13900001111")
# for name, phone in get_all_contacts().items():
#     print(f"{name}: {phone}")

# ✅ **现在你的代码：**

# - 结构清晰
# - 易于扩展（加新功能只需改对应模块）
# - 可被其他项目复用（`from contact_app.core import ...`）

# 🔍 六、相对导入 vs 绝对导入
# 绝对导入（推荐！）
# from core.storage import load_contacts
# from myproject.utils import helper

# - 从项目根目录开始
# - 清晰、不易出错

# 相对导入（包内部使用）
# 在 core/contacts.py 中
# from .storage import load_contacts  # ← 当前包下的 storage 模块
# from ..utils import helper         # ← 上一级包的 utils 模块

# 用 `.` 表示当前包，`..` 表示上一级
# **只能在包内使用**，不能在主脚本中用

# ⚠️ 如果运行 `python core/contacts.py`，相对导入会报错！  
# 正确运行方式：`python -m contact_app.main`

# 🛠️ 七、如何运行带包的项目？
# ❌ 错误方式：
# python main.py          # 如果 main.py 用了相对导入，会失败

# ✅ 正确方式（从项目根目录运行）：
# 假设你在 contact_app/ 目录外
# python -m contact_app.main

# 或者确保当前目录在 `sys.path` 中（开发时常用）。

# 📌 八、标准库 vs 第三方包 vs 自定义包
# | 类型         | 示例                              | 说明                  |
# | ------------ | --------------------------------- | --------------------- |
# | **标准库**   | `import json`, `import os`        | Python 自带，无需安装 |
# | **第三方包** | `import requests`, `import numpy` | 用 `pip install` 安装 |
# | **自定义包** | `from mytools import ...`         | 你自己写的模块/包     |

# ✅ 你正在学习的就是 **自定义包** 的构建！

# 🎯 九、最佳实践总结
# | 建议                          | 说明                                      |
# | ----------------------------- | ----------------------------------------- |
# | ✅ 每个 `.py` 文件是一个模块   | 职责单一（如 `file_utils.py` 只处理文件） |
# | ✅ 用包组织相关模块            | 如 `core/`, `utils/`, `api/`              |
# | ✅ `__init__.py` 用于简化导入  | 不要留空，暴露关键接口                    |
# | ✅ 优先使用绝对导入            | 更清晰、更安全                            |
# | ✅ 避免 `from module import *` | 除非在 `__init__.py` 中用 `__all__` 控制  |
# | ✅ 项目结构清晰                | 主程序在顶层，逻辑在子包                  |