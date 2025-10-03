"""
**项目结构与模块化设计**。这是从“写脚本”迈向“写工程”的分水岭！
"""

# 本课目标：把你的通讯录项目从“单文件脚本” → “专业模块化项目”

# 学完你能
# - 把功能拆分成多个 `.py` 文件
# - 正确使用 `import` 导入自己写的模块
# - 避免 `ModuleNotFoundError`（最常见错误！）
# - 写出清晰、可维护、可测试的代码结构

# 🧱 一、为什么需要模块化？
# ❌ 单文件脚本的问题（你可能遇到过）：

# contact_manager.py (500行)
# def add_contact(): ...      # 业务逻辑
# def save_to_file(): ...     # 文件操作
# def validate_phone(): ...   # 工具函数
# def main(): ...             # 主流程
# 所有代码混在一起 → 难读、难改、难测！

# ✅ 模块化后：

# contact_app/
# ├── main.py                 # 只负责启动程序
# ├── core/
# │   ├── __init__.py
# │   ├── contacts.py         # 联系人业务逻辑（增删查改）
# │   └── storage.py          # 文件读写（JSON）
# ├── utils/
# │   ├── __init__.py
# │   └── validators.py       # 输入校验（电话、邮箱）
# └── data/                   # 存放数据文件（可选）
#     └── contacts.json

# ✅ **好处**：  
# - 改存储方式？只动 `storage.py`  
# - 加新校验规则？只改 `validators.py`  
# - 测试业务逻辑？不用碰文件系统！

# 🛠️ 二、核心概念速成
# 1. **模块（Module）** = 一个 `.py` 文件
# core/contacts.py
# def add_contact(contacts, name, phone):
#     ...
# 2. **包（Package）** = 带 `__init__.py` 的文件夹
# core/__init__.py （可以为空，但必须存在！）

# 3. **导入方式**
# 绝对导入（推荐！）
# from core.contacts import add_contact
# from utils.validators import is_valid_phone

# 相对导入（在包内部使用）
# from .contacts import add_contact   # 在 core/ 内部用

# 🧪 三、实战：重构你的通讯录项目
# 我们一步步把单文件项目变成模块化结构！
# 步骤 1：创建项目结构
# contact_app/
# ├── main.py
# ├── core/
# │   ├── __init__.py
# │   ├── contacts.py
# │   └── storage.py
# ├── utils/
# │   ├── __init__.py
# │   └── validators.py
# └── requirements.txt


# ✅ 用命令行快速创建（Windows）：
