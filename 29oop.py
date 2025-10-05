from datetime import datetime
from typing import Any
from typing import Self
class Contact:
    species: str = "Human" # ← 类属性：所有联系人都是人类
    VERSION: str = "1.0"

    name: str # ← 实例属性
    phone: str
    email: str
    created_at: str

    def __init__(self, name: str, phone: str, email: str | None = None, created_at: str | None = None) -> None:  # 初始化方法
        self.name = name  # ← 实例属性
        self.phone = phone
        self.email = email or "123456@qq.com" # ← 实例属性,默认值是 123456@qq.com
        self.created_at = created_at or datetime.now().isoformat()

    def is_valid(self) -> bool: # ← 实例方法
        return self.validate_name(self.name) and self.validate_phone(self.phone)
    
    def __str__(self) -> str: # ← 实例方法
        return f"{self.name} - {self.phone}"
    
    @classmethod # ← 类方法注解
    def from_dict(cls, data: dict[str, Any]) -> Self:# ← 类方法，返回自身

        return cls(
            name = data.get("name"), # ← 获取字典中的name键对应的值
            phone = data.get("phone"),
            email = data.get("email"),
            created_at = data.get("created_at")
        )
    @classmethod # ← 类方法注解
    def get_version(cls) -> str: # ← 类方法
        return cls.VERSION # ← 通过 cls 访问类属性
    
    @staticmethod # ← 静态方法注解
    def validate_phone(phone: str) -> bool: # ← 静态方法
        """验证电话号码是否合法（工具函数）"""
        return len(phone) == 11 and phone.isdigit()
    @staticmethod
    def validate_email(email: str) -> bool: # ← 静态方法
        """验证邮箱是否合法（工具函数）"""
        return "@" in email
    @staticmethod
    def validate_name(name: str) -> bool: # ← 静态方法
        """验证姓名是否合法（工具函数）"""
        return bool(name.strip())


# 2、类、实例
# 💡 类本身**不占用内存**，它只是“说明书”。只有当你用它造出对象时，才真正存在。
#  类是模板，对象是实例
# ⚠️ 严格说，Python 先调用 `__new__` 创建对象，再调用 `__init__` 初始化。但初学者可以认为 `__init__` 就是构造方法
c1 = Contact("Alice", "13800138000")
c2 = Contact("小明", "13800138001")
print(c1.name)
print(c2.name)
print(type(c1))
print(c1 is c2)
print(c1.__dict__)

# 3、实例属性和类属性
# 实例属性 是在 __init__（或其他实例方法）中通过 self.xxx 定义的属性。
# 每个对象都有自己的一份副本，互不干扰。

# 类属性 是在 类内部、方法外部 直接定义的变量。
# 它属于类本身，所有实例共享同一个值。

print(c1.species)  # Human（直接通过类访问）
print(c2.species)  # Human
Contact.species = "Person" # 修改类属性
print(c1.species)  # Person（所有实例都变了！）
print(c2.species) # Person

# ✅ 正确做法：类属性应该通过 类名 修改（Contact.species = ...），而不是实例。
#  对比总结表
# | 特性             | 实例属性                                    | 类属性                                           |
# | ---------------- | ------------------------------------------- | ------------------------------------------------ |
# | **定义位置**     | `__init__` 或实例方法中（`self.xxx = ...`） | 类内部、方法外部（`xxx = ...`）                  |
# | **归属**         | 属于**每个对象自己**                        | 属于**类本身**                                   |
# | **内存**         | 每个对象一份                                | 所有对象共享一份                                 |
# | **修改影响**     | 只影响当前对象                              | 影响所有未覆盖该属性的对象                       |
# | **访问方式**     | `obj.attr`                                  | `ClassName.attr` 或 `obj.attr`（但不推荐用 obj） |
# | **你的项目例子** | `name`, `phone`, `email`                    | （目前没有，但可以加 `version = "1.0"`）         |

# 属性的访问与修改规则
# | 操作             | 语法                      | 说明                         |
# | ---------------- | ------------------------- | ---------------------------- |
# | **读取实例属性** | `obj.name`                | 直接访问                     |
# | **修改实例属性** | `obj.name = "新名字"`     | 只影响该对象                 |
# | **读取类属性**   | `Contact.VERSION`         | 推荐用类名访问               |
# | **修改类属性**   | `Contact.VERSION = "2.0"` | 影响所有实例                 |
# | **错误修改**     | `obj.VERSION = "2.0"`     | 会创建实例属性，遮盖类属性！ |


# 4、方法（Methods）：实例方法、类方法、静态方法
# 1️⃣ 实例方法（Instance Method）
# - **最常见的方法**
# - 第一个参数必须是 `self`（代表当前对象）
# - 可以访问和修改 **实例属性** 和 **类属性**

print(c1.is_valid()) # True ← 调用实例方法
print(c1.__str__())

# ✅ **特点**：必须通过**对象**调用，自动传入 `self`

# 2️⃣ 类方法（Class Method）→ `@classmethod`
# - 用 `@classmethod` 装饰
# - 第一个参数是 `cls`（代表当前类，不是对象！）
# - 可以访问 **类属性**，但**不能直接访问实例属性**（因为还没创建对象）

# 🧪 使用场景：**替代构造函数**（工厂方法）
data = {"name": "小明", "phone": "15599883377", "email": "123456@qq.com", "created_at": "2022-01-01"}
c3 = Contact.from_dict(data) # ← 不用传 name/phone，直接从字典创建对象
print(c3.__dict__)

# 💡 为什么不用普通函数？
# - 它属于 `Contact` 类，语义清晰
# - 子类继承时会自动变成子类的类方法（多态支持）

# 🧪 类方法也能访问类属性：
print(Contact.get_version())

# ✅ **特点**：通过**类或对象**调用，自动传入 `cls`

# 3️⃣ 静态方法（Static Method）→ `@staticmethod`
# - 用 `@staticmethod` 装饰
# - **没有 `self` 或 `cls` 参数**
# - **不能访问实例属性或类属性**
# - 本质上是一个**普通函数**，只是逻辑上属于这个类

print(Contact.validate_phone("13636")) # False
print(Contact.validate_phone("13800138000")) # True

# 💡 为什么不用独立函数？
# - 这个功能**和 Contact 强相关**，放在一起更清晰
# - 避免污染全局命名空间
# ✅ **特点**：和类/对象无关，只是“住”在类里

# 🔍 三者终极对比表
# | 特性                 | 实例方法                  | 类方法 (`@classmethod`)            | 静态方法 (`@staticmethod`)         |
# | -------------------- | ------------------------- | ---------------------------------- | ---------------------------------- |
# | **第一个参数**       | `self`（对象）            | `cls`（类）                        | 无                                 |
# | **能访问实例属性？** | ✅ 是                      | ❌ 否                               | ❌ 否                               |
# | **能访问类属性？**   | ✅ 是                      | ✅ 是                               | ❌ 否                               |
# | **调用方式**         | `obj.method()`            | `Class.method()` 或 `obj.method()` | `Class.method()` 或 `obj.method()` |
# | **典型用途**         | 操作对象数据              | 替代构造函数、操作类状态           | 工具函数（与类相关但不依赖状态）   |
# | **你的项目例子**     | `is_valid()`, `__str__()` | `from_dict()`                      | （可新增 `validate_phone()`）      |

# 💡 使用场景总结（记住这几句！）
# - **用实例方法**：当你需要操作**某个具体对象**的数据（90% 的情况）  
# - **用类方法**：当你想**创建对象**但参数格式不同（如从 JSON、字典、字符串创建）  
# - **用静态方法**：当你有一个**工具函数**，和类相关但不需要类或对象的数据

# ✅ 小结：一句话区分
# - **实例方法**：我要操作**我自己**（`self`）  
# - **类方法**：我要操作**我的家族**（`cls`）  
# - **静态方法**：我只是**住在这儿**，和你们没关系