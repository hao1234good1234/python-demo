"""
单元测试（pytest）
"""

#  **模块化 + 单元测试 = 专业开发的黄金组合**  

# 🎯 本课目标：为你的通讯录项目添加自动化测试
# ✅ 学完你能：
# - 用 `pytest` 写第一个测试
# - 自动验证 `add_contact`、`is_valid_phone` 等函数是否正确
# - 运行测试并查看结果
# - 理解“测试驱动开发（TDD）”的基本思想

# 一、为什么需要单元测试？
### ❌ 没有测试的痛苦：

# - 改了一行代码，结果其他功能崩了（自己都不知道）
# - 手动测试：每次都要运行程序、输入数据、看结果 → **效率低、易遗漏**
# - 团队协作：别人改了你的代码，你怎么知道没坏？

### ✅ 有测试的好处：

# - **一键运行所有测试**：`pytest`
# - **立即知道哪坏了**：精确到函数、行号
# - **放心重构**：只要测试通过，功能就没错
# - **文档作用**：测试代码就是最好的使用示例

# > 💡 **专业项目标配**：没有测试的代码 = 不可维护的代码


#  二、为什么选 `pytest`？（而不是 `unittest`）
# | 对比项   | `unittest`（Python 内置） | `pytest`（推荐）             |
# | -------- | ------------------------- | ---------------------------- |
# | 语法     | 繁琐（要写类、继承）      | **简洁**（普通函数即可）     |
# | 断言     | `self.assertEqual(a, b)`  | **直接 `assert a == b`**     |
# | 发现测试 | 手动注册                  | **自动发现 `test_*.py`**     |
# | 插件生态 | 弱                        | **强大**（覆盖率、参数化等） |
# | 学习曲线 | 陡峭                      | **平缓**（10 分钟上手）      |

# ✅ **行业标准**：90% 的现代 Python 项目用 `pytest`

# 🔌 三、安装 pytest
# 在你的虚拟环境中运行：
# 激活虚拟环境（如果你有）
# venv\Scripts\activate

# 安装 pytest
# pip install pytest

# 验证安装
# pytest --version
# 输出：pytest 8.2.0

# 💡 **记得更新 `requirements.txt`**：
# pip freeze > requirements.txt

# 📂 四、项目结构更新：加入 `tests/` 目录

# contact_app/
# ├── main.py
# ├── core/
# │   ├── __init__.py
# │   ├── contacts.py
# │   └── storage.py
# ├── utils/
# │   ├── __init__.py
# │   └── validators.py
# ├── tests/                  ← 新增！
# │   ├── __init__.py
# │   ├── test_contacts.py
# │   └── test_validators.py
# ├── data/
# ├── requirements.txt
# └── .gitignore

# ✅ **约定**：  

# - 测试文件以 `test_` 开头  
# - 测试函数以 `test_` 开头