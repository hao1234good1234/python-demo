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

# 🧪 五、实战：写第一个测试
# 步骤 1：测试 `is_valid_phone`（最简单）

# 🔸 `tests/test_validators.py`
# tests/test_validators.py
from utils.validators import is_valid_phone

def test_valid_phone():
    """测试有效手机号"""
    assert is_valid_phone("13800138000") == True
    assert is_valid_phone("15912345678") == True

def test_invalid_phone():
    """测试无效手机号"""
    assert is_valid_phone("123") == False          # 太短
    assert is_valid_phone("23800138000") == False  # 不以1开头
    assert is_valid_phone("1380013800a") == False  # 含字母
    assert is_valid_phone("") == False             # 空字符串

# 步骤 2：测试 `add_contact`
# 🔸 `tests/test_contacts.py`
# tests/test_contacts.py
from core.contacts import add_contact, find_contact

def test_add_contact():
    """测试添加联系人"""
    contacts = []
    new_contacts = add_contact(contacts, "张三", "13800138000")
    
    assert len(new_contacts) == 1
    assert new_contacts[0]["name"] == "张三"
    assert new_contacts[0]["phone"] == "13800138000"

def test_find_contact():
    """测试查找联系人"""
    contacts = [
        {"name": "张三", "phone": "13800138000"},
        {"name": "李四", "phone": "13900139000"}
    ]
    
    found = find_contact(contacts, "张三")
    assert found is not None
    assert found["phone"] == "13800138000"
    
    not_found = find_contact(contacts, "王五")
    assert not_found is None

# ▶️ 六、运行测试
# 在 `contact_app/` 目录下运行：
# 运行所有测试
# pytest

# 详细模式（推荐）
# pytest -v

# 只运行某个文件
# pytest tests/test_validators.py -v

# ✅ 成功输出示例：
# ======================== test session starts ========================
# collected 6 items

# tests/test_contacts.py::test_add_contact PASSED                [ 16%]
# tests/test_contacts.py::test_find_contact PASSED               [ 33%]
# tests/test_validators.py::test_valid_phone PASSED              [ 50%]
# tests/test_validators.py::test_invalid_phone PASSED            [ 66%]
# ...
# ========================= 6 passed in 0.02s =========================

# 🎉 **6 passed** = 你的代码通过了所有测试！

# 🐞 七、故意制造一个 Bug，看测试如何保护你
# 修改 `utils/validators.py`：

# def is_valid_phone(phone: str) -> bool:
#     # 错误：允许 12 开头（实际应为 13-19）
#     return bool(re.match(r"^1[2-9]\d{9}$", phone))  # ← 故意写错

# 再次运行测试：
# pytest tests/test_validators.py -v


# ❌ 失败输出：
# FAILED tests/test_validators.py::test_valid_phone - AssertionError: assert False == True

# ✅ **测试立刻发现问题**！你不用等到用户投诉才发现错误。

# 📊 八、进阶技巧（可选但实用）
# 1. **参数化测试**（避免重复代码）
import pytest
from utils.validators import is_valid_phone

@pytest.mark.parametrize("phone, expected", [
    ("13800138000", True),
    ("15912345678", True),
    ("123", False),
    ("23800138000", False),
])
def test_is_valid_phone(phone, expected):
    assert is_valid_phone(phone) == expected

# 2. **测试覆盖率**（知道哪些代码没测到）
# 安装
# pip install pytest-cov

# 运行并生成报告
# pytest --cov=core --cov=utils --cov-report=html

# 打开 htmlcov/index.html 查看覆盖率

# 📝 九、最佳实践总结
# | 原则               | 说明                               |
# | ------------------ | ---------------------------------- |
# | **测试函数要小**   | 一个测试只测一个功能点             |
# | **命名清晰**       | `test_add_contact_with_valid_data` |
# | **不要测私有函数** | 只测公开接口（`def xxx`）          |
# | **避免测试副作用** | 不要依赖文件、网络（用 mock）      |
# | **保持快速**       | 单元测试应在毫秒级完成             |

# 🧩 十、常见问题解答

# ❓ Q：测试文件放哪？要 `__init__.py` 吗？

# ✅ A：放在 `tests/` 目录，**需要 `__init__.py`**（让 pytest 能导入模块）

# ❓ Q：如何测试会写文件的函数（如 `save_contacts`）？
def test_save_contacts(tmp_path):
    data_file = tmp_path / "contacts.json"
    # ... 测试逻辑

# ❓ Q：测试要覆盖 100% 吗？
# ✅ A：**核心逻辑尽量覆盖**，但不必强求 100%。重点是**关键路径**和**边界条件**。


## ✅ 十一、验证你是否成功

# 1. 项目中有 `tests/` 目录
# 2. 运行 `pytest` 显示 **所有测试通过**
# 3. 故意改错代码，测试能**立即失败**