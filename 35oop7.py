"""
# 第九章：实战与项目应用

# 第二十二步：**构建一个小型 OOP 项目**
"""

# 🎯 项目选择：图书管理系统（Library System）

# 🧱 项目目标
# 实现以下功能：

# 添加图书（书名、作者、ISBN）
# 借书（用户借一本可用的书）
# 还书
# 查询某本书是否可借
# 查看某用户借了哪些书
# ✅ 要求：代码结构清晰，未来可轻松替换“内存存储”为“数据库”

# 📂 推荐项目结构（应用你学的模块化）
# library_system/
# ├── core/                   # 核心业务逻辑（纯 Python，无外部依赖）
# │   ├── __init__.py
# │   ├── models.py           # Book, User
# │   ├── services.py         # LibraryService
# │   └── interfaces.py       # BookRepository, UserRepository (Protocol)
# ├── infrastructure/         # 实现细节（内存存储）
# │   ├── __init__.py
# │   └── in_memory_repos.py  # InMemoryBookRepo, InMemoryUserRepo
# ├── main.py                 # 命令行交互入口
# └── tests/                  # 单元测试（可选但推荐）
#     └── test_library.py