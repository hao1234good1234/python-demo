"""
面向对象编程（OOP）
"""

# **类（Class）** 就能封装数据 + 行为：
class Contact:
    def __init__(self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.last_contacted = None
    def validate_phone(self):
        return len(self.phone) == 11 and self.phone.isdigit()
    def to_vcard(self):
        return f"BEGIN:VCARD\nVERSION:3.0\nN:{self.name}\nTEL:{self.phone}\nEND:VCARD"
# ✅ **数据（属性） + 操作（方法） = 对象**


# ✅ 第二步：核心概念速成（结合你的项目）    
# 1. `class` 和 `__init__`（构造函数）

class Contact:
    def __init__(self, name, phone):

        # self 代表“当前这个对象”
        self.name = name   # 实例属性
        self.phone = phone

# 创建对象（实例化）
alice = Contact("Acile", "13899990022")
print(alice.name)  # Acile

# 💡 `__init__` 是对象创建时自动调用的“初始化方法”。

# 2. `self` 是什么？
# `self` 不是关键字，只是一个**约定俗成的名字**
# 它代表**当前实例对象本身**
# 所有实例方法第一个参数必须是 `self`

class Contact:
    def __init__(self, name, phone):

        # self 代表“当前这个对象”
        self.name = name   # 实例属性
        self.phone = phone
    def say_hello(self):  # 必须有 self
        return f"Hello, I'm {self.name}"

alice = Contact("Alice", "13800138000")
print(alice.say_hello())  # 自动传入 alice 作为 self
# 🔍 你可以把 `self` 想象成“这个联系人自己”。

# 3. 实例属性 vs 类属性
class Contact:
    category = "personal"  # 类属性, 所有实例共享
    def __init__(self, name, phone):
        self.name = name # 实例属性：每个联系人不同
        self.phone = phone

alice = Contact("Alice", "15688992233")
bob = Contact("Bob", "15633992200")

print(alice.category)  # personal
print(bob.category)   # personal
Contact.category = "work" # 修改类属性
print(alice.category)  # work
print(bob.category)   # work

# ⚠️ 一般用**实例属性**，类属性用于全局配置。
# 4. 方法（Methods）
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def is_valid(self):
        return len(self.phone) == 11 and self.phone.isdigit()
    def display(self):
        return f"{self.name} - {self.phone}"
# 使用
alice =  Contact("Alice", "13800138000")
print(alice)
if alice.is_valid():
    print(alice.display())

# 5. 特殊方法（Magic Methods / Dunder Methods）
# 让对象支持 `print()`、`len()`、`+` 等操作。
# 方法1：`__str__`：定义 `print()` 输出

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def __str__(self):
        return f"联系人：{self.name} - {self.phone}"
alice = Contact("Alice", "15588992233")
# 当你写 print(alice) 时，Python 并不是直接打印对象本身，而是：先调用 str(alice) 然后打印 str(alice) 返回的字符串
# str(alice) 会自动触发 alice 所属类中的 __str__ 方法！
# 所以 print(obj) → str(obj) → obj.__str__()
print(alice)  # 输出：联系人：Alice - 15588992233
print(str(alice))  # 输出：联系人：Alice - 15588992233
print(alice.__str__())  # 输出：联系人：Alice - 15588992233

# 方法2：__repr__ 是给开发者看的 定义调试输出（更详细）
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def __str__(self):
        return f"{self.name} - {self.phone}"          # 给用户看
    
    def __repr__(self):
        
        return f"Contact(name='{self.name}', phone='{self.phone}')"  # 给程序员看

alice = Contact("Alice", "13800138000")
print(alice)        # 调用 __str__ → Alice - 13800138000
print(repr(alice))  # 调用 __repr__ → Contact(name='Alice', phone='13800138000')

# 在交互式环境（如 Jupyter、Python REPL）中直接输入 alice，会调用 __repr__

# 📌 规则：

# print(obj) → __str__
# repr(obj) 或调试器 → __repr__
# 如果没定义 __str__，print 会退而求其次用 __repr__
# 如果都没定义，就显示 <__main__.Contact object at 0x...>

# 方法3：`__eq__`：定义 `==` 比较
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def __eq__(self, other):
        if isinstance(other, Contact):
            return self.phone == other.phone
        return False
alice = Contact("Alice", "13899990011")
a = Contact("A", "13899990011")
print(alice == a)  # True 因为 alice.phone == a.phone
# ✅ 这些方法让你的对象“像内置类型一样好用”。

# 6. 继承（Inheritance）——代码复用神器

# 假设你要区分“个人联系人”和“公司联系人”：
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def display(self):
        return f"{self.name} - {self.phone}"
# 公司联系人 继承自 Contact
class BusinessContact(Contact):
    def __init__(self, name, phone, company):
        super().__init__(name, phone)
        self.company = company
    def display(self):
        return f"{self.name} - {self.phone} - {self.company}"
# 使用
alice = Contact("Alice", "13599998888")
ibm_john = BusinessContact("John", "13988883333", "IBM")
print(alice.display()) # Alice - 13599998888
print(ibm_john.display()) # John - 13988883333 - IBM
# 🔁 **继承 = “是一个”关系**（公司联系人“是一个”联系人）

## 第三步：用 OOP 重构你的 `contact_app2`

### 1. 创建 `Contact` 类（`src/contact_app/models.py`）

# src/contact_app/models.py
import json
from datetime import datetime

class Contact:
    def __init__(self, name, phone, email=None, created_at=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.created_at = created_at or datetime.now().isoformat()
    
    def is_valid(self):
        return bool(self.name) and len(self.phone) == 11 and self.phone.isdigit()
    
    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            phone=data["phone"],
            email=data.get("email"),
            created_at=data.get("created_at")
        )
    
    def __str__(self):
        return f"{self.name} - {self.phone}"
    
    def __repr__(self):
        return f"Contact(name='{self.name}', phone='{self.phone}')"

### 2. 修改存储逻辑（`core/storage.py`）

# src/contact_app/core/storage.py
import json
import os
from pathlib import Path
from contact_app.models import Contact

DATA_DIR = Path("data")
CONTACTS_FILE = DATA_DIR / "contacts.json"

def load_contacts():
    if not CONTACTS_FILE.exists():
        return []
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Contact.from_dict(item) for item in data]

def save_contacts(contacts):
    DATA_DIR.mkdir(exist_ok=True)
    data = [contact.to_dict() for contact in contacts]
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

### 3. 修改 CLI 命令（`cli.py`）

# cli.py 中的 add 命令
# from contact_app.models import Contact

# @cli.command()
# @click.argument("name")
# @click.argument("phone")
# def add(name, phone):
#     contact = Contact(name, phone)
#     if not contact.is_valid():
#         logger.warning(f"无效联系人: {contact}")
#         click.echo("❌ 数据无效", err=True)
#         raise click.Abort()
    
#     contacts = load_contacts()
#     contacts.append(contact)
#     save_contacts(contacts)
#     logger.info(f"添加成功: {contact}")
#     click.echo(f"✅ {contact}")

## ✅ 第四步：OOP 如何帮助你学 Web 开发？