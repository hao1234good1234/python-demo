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
# mkdir contact_app\core contact_app\utils
# type nul > contact_app\core\__init__.py
# type nul > contact_app\utils\__init__.py

# 步骤 2：拆分代码
# `core/contacts.py` —— 业务逻辑

# 🔸 core/contacts.py
from typing import List, Dict

def create_contact(name: str, phone: str) -> Dict[str, str]:
    """创建联系人字典"""
    return {"name": name, "phone": phone}

def add_contact(contacts: List[Dict], name: str, phone: str) -> List[Dict]:
    """添加联系人（返回新列表）"""
    new_contact = create_contact(name, phone)
    return contacts + [new_contact]

def find_contact(contacts: List[Dict], name: str) -> Dict | None:
    """按姓名查找联系人"""
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return None

# 🔸 `core/storage.py` —— 文件存储

# core/storage.py
import json
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path("data/contacts.json")

def ensure_data_dir():
    """确保 data 目录存在"""
    DATA_FILE.parent.mkdir(exist_ok=True)

def save_contacts(contacts: List[Dict]):
    """保存联系人到 JSON 文件"""
    ensure_data_dir()
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)

def load_contacts() -> List[Dict]:
    """从 JSON 文件加载联系人"""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    

# 🔸 `utils/validators.py` —— 输入校验
# utils/validators.py
import re

def is_valid_phone(phone: str) -> bool:
    """简单校验手机号（中国）"""
    return bool(re.match(r"^1[3-9]\d{9}$", phone))

def is_valid_name(name: str) -> bool:
    """校验姓名（非空）"""
    return bool(name.strip())
# 🔸 `main.py` —— 程序入口
# main.py
from core.contacts import add_contact, find_contact
from core.storage import load_contacts, save_contacts
from utils.validators import is_valid_name, is_valid_phone

def main():
    contacts = load_contacts()
    
    # 添加联系人示例
    name = "张三"
    phone = "13800138000"
    
    if not is_valid_name(name):
        print("❌ 姓名无效")
        return
    if not is_valid_phone(phone):
        print("❌ 电话无效")
        return
        
    contacts = add_contact(contacts, name, phone)
    save_contacts(contacts)
    
    # 查找测试
    found = find_contact(contacts, "张三")
    print("✅ 找到:", found)

if __name__ == "__main__":
    main()

# 步骤 3：运行项目（关键！）
# ✅ 正确运行方式（在 `contact_app/` 目录下）：

# 激活虚拟环境（如果你有）
# venv\Scripts\activate

# 运行主程序
# python main.py

# 📌 **重要**：必须在 `contact_app/` 目录下运行！  
# 因为 Python 会把**当前目录**加入模块搜索路径。

# ⚠️ 四、常见错误 & 解决方案

# ❌ 错误 1：`ModuleNotFoundError: No module named 'core'`

# 原因：

# - 你在 `contact_app/` **外面**运行了 `python contact_app/main.py`
# - Python 找不到 `core` 包

# ✅ 正确做法：

# 进入项目目录再运行
# cd contact_app
# python main.py

# ❌ 错误 2：直接双击 `main.py` 运行

# - 双击时工作目录不确定 → 必然报错
# - ✅ **永远用命令行运行！**

# ❌ 错误 3：忘记 `__init__.py`

# - Python 不会把文件夹当包
# - ✅ 确保每个包目录都有 `__init__.py`（可以为空）

# 📦 五、项目结构最佳实践

# | 目录      | 用途         | 示例                        |
# | --------- | ------------ | --------------------------- |
# | `main.py` | 程序入口     | 启动逻辑、命令行解析        |
# | `core/`   | 核心业务逻辑 | 联系人管理、订单处理        |
# | `utils/`  | 工具函数     | 校验、格式化、辅助函数      |
# | `data/`   | 数据文件     | JSON、CSV（不要提交到 Git） |
# | `tests/`  | 单元测试     | 未来学 pytest 时用          |
# | `docs/`   | 文档         | 项目说明                    |

# ✅ **原则**：  

# - 每个文件职责单一  
# - 高内聚（相关功能放一起），低耦合（模块间依赖少）

# 🧩 六、高级技巧（可选）
# 1. 在 `__init__.py` 中简化导入
# core/__init__.py
from .contacts import add_contact, find_contact
from .storage import load_contacts, save_contacts

# 这样外部可以写：
# from core import add_contact  （而不是 from core.contacts import ...）


# 2. 使用 `if __name__ == "__main__"` 测试模块

# core/contacts.py
# def add_contact(...): ...

# if __name__ == "__main__":
#     # 直接运行 contacts.py 时测试
#     contacts = add_contact([], "测试", "13800138000")
#     print(contacts)

# ✅ 七、验证你是否成功

# 运行 `main.py` 后：

# 1. 生成 `data/contacts.json` 文件
# 2. 控制台输出：`✅ 找到: {'name': '张三', 'phone': '13800138000'}`
# 3. 代码分布在多个文件，但能协同工作