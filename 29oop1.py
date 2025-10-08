from datetime import datetime
from typing import Any
from typing import Self


class Contact:
    """
    联系人类：封装姓名、电话、创建时间等信息。
    所有数据访问均通过属性管理，确保数据一致性与安全性。
    """

    species: str = "Human"  # ← 类属性：所有联系人都是人类
    VERSION: str = "1.0"  # ← 类属性

    name: str  # ← 实例属性
    phone: str
    email: str

    # email 是一个可选参数，类型是字符串或空值，默认为 None”
    def __init__(
        self, name: str, phone: str | None = None, email: str | None = None
    ) -> None:  # 初始化方法
        # ✅ 显式初始化所有内部属性（防御性编程）
        self._name = None
        self._phone = None  # ← 1. 先初始化内部存储（受保护）
        self._email = None
        self._created_at = datetime.now().isoformat()  # ← 内部存储创建时间

        # ✅ 通过公共接口赋值（触发验证）
        self.name = name  # ← 实例属性 # 公有：直接暴露
        # 系统会这么读取：c1.phone = "15699882233", 实例c1里没有phone属性，但是系统中phone被@property装饰了，
        # phone从属性变成了property对象，会自动调用phone对象的__set__方法，又因为在类中定义了对phone的赋值的setter自定义方法
        # 系统会执行你自定义的setter方法：   def phone(self, value) -> self == c1, value == "15699882233"
        self.phone = phone  # ← 2. 通过“公共接口”赋值（会触发验证！）
        self.email = email or "123456@qq.com"  # ← 实例属性,默认值是 123456@qq.com

    def __str__(self) -> str:  # ← 实例方法
        return f"{self.name} - {self.phone}"

    def __repr__(self) -> str:  # ← 实例方法
        # Contact(name='Alice', phone='13800138000') 加了!r会输出''单引号，方便开发人员查看
        # Contact(name=Alice, phone=13800138000)  没有加!r，看不出是字符串！
        return f"Contact(name={self.name!r}, phone={self.phone!r})"

    @classmethod  # ← 类方法注解
    def from_dict(cls, data: dict[str, Any]) -> Self:  # ← 类方法，返回自身
        return cls(
            name=data.get("name"),  # ← 获取字典中的name键对应的值
            phone=data.get("phone"),
            email=data.get("email")
        )

    @classmethod  # ← 类方法注解
    def get_version(cls) -> str:  # ← 类方法
        return cls.VERSION  # ← 通过 cls 访问类属性

    @staticmethod  # ← 静态方法注解
    def validate_email(email: str) -> bool:  # ← 静态方法，没有self
        """验证邮箱是否合法（工具函数）"""
        return "@" in email

    @staticmethod  # ← 静态方法注解
    def validate_name(name: str) -> bool:  # ← 静态方法，没有self
        """验证姓名是否合法（工具函数）"""
        return bool(name.strip())

    @staticmethod  # ← 静态方法注解
    def validate_phone(phone: str) -> bool:  # ← 静态方法，没有self
        """验证电话号码是否合法（工具函数）"""
        return bool(isinstance(phone, str) and phone.isdigit() and len(phone) == 11)

    # ===== name 属性管理 =====
    @property
    def name(self) -> str:
        """获取联系人姓名（只读，不能为空）"""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("姓名必须是字符串")
        value = value.strip()  # ← 去除前后空格
        if not value:
            raise ValueError("姓名不能为空")
        self._name = value

    # ===== phone 属性管理 =====
    @property  # ← property装饰器, 将phone属性变成了一个property对象
    def phone(self) -> str:  # ← getter方法   # ← 这是“读取”接口
        """获取电话号码（返回 '未设置' 或有效号码）"""
        return self._phone if self._phone is not None else "未设置"  # ← 读取私有属性

    @phone.setter  # 自定义phone的setter方法
    def phone(self, value: str) -> None:  # ← setter方法   # ← 这是“写入”接口
        """设置电话号码（必须为11位数字字符串）"""
        if value is None:
            self._phone = None
            return
        if not self._is_valid_phone(value):  # 调用内部方法
            raise ValueError("电话必须是11位，且只能是数字！")
        self._phone = value

    def _is_valid_phone(self, phone: str) -> bool:  # ← 内部方法
        """验证电话号码是否合法（工具函数）"""
        return len(phone) == 11 and phone.isdigit() and isinstance(phone, str)

    @phone.deleter
    def phone(self):  # ← deleter方法   # ← 这是“删除”接口
        """删除电话号码"""
        print("电话号码已删除")
        self._phone = None

    # ===== email 属性管理 =====
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if not self._is_valid_email(value):
            raise ValueError("邮箱格式不正确！")
        self._email = value

    def _is_valid_email(self, email: str) -> bool:
        return "@" in email and isinstance(email, str)

    # ===== created_at 只读属性 =====
    @property  # 只有property，没有setter，只读
    def created_at(self) -> datetime:  # ← getter方法   # ← 这是“读取”接口
        """获取联系人创建时间（只读）"""
        return self._created_at

    # ===== 公共方法 =====
    def is_valid(self) -> bool:  # ← 公共接口
        """判断联系人是否有效（姓名必填，电话可选）"""
        return self._name is not None

    # ===== 计算属性 =====
    @property
    def full_info(self) -> str:
        return f"{self.name} <{self.phone}>"

    # ====== 对象转成字典（常用于 API 返回） ======
    def to_dict(self) -> dict:
         """将联系人转为字典（排除私有属性和方法）"""
         return {
             "name": self.name,
             "phone": self.phone,
             "email": self.email,
             "created_at": self.created_at
         }
    # 或者更通用的动态方式（谨慎使用）：
    def to_dict_dynamic(self) -> dict:
        return {    
            k: v for k, v in self.__dict__.items() 
            # if not k.startswith("_") # 排除私有属性
        }
'''
# 第一章：OOP 基础概念
# 第二步：类（Class）与对象（Object
'''
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
print(c1)

'''
# 第二章：类的结构与成员
# 第三步：实例属性与类属性
'''

# 实例属性 是在 __init__（或其他实例方法）中通过 self.xxx 定义的属性。
# 每个对象都有自己的一份副本，互不干扰。

# 类属性 是在 类内部、方法外部 直接定义的变量。
# 它属于类本身，所有实例共享同一个值。

print(c1.species)  # Human（直接通过类访问）
print(c2.species)  # Human
Contact.species = "Person"  # 修改类属性
print(c1.species)  # Person（所有实例都变了！）
print(c2.species)  # Person

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


'''
# 第四步：方法（Methods）：实例方法、类方法、静态方法
'''
# 1️⃣ 实例方法（Instance Method）
# - **最常见的方法**
# - 第一个参数必须是 `self`（代表当前对象）
# - 可以访问和修改 **实例属性** 和 **类属性**

print(c1.is_valid())  # True ← 调用实例方法
print(c1.__str__())

# ✅ **特点**：必须通过**对象**调用，自动传入 `self`

# 2️⃣ 类方法（Class Method）→ `@classmethod`
# - 用 `@classmethod` 装饰
# - 第一个参数是 `cls`（代表当前类，不是对象！）
# - 可以访问 **类属性**，但**不能直接访问实例属性**（因为还没创建对象）

# 🧪 使用场景：**替代构造函数**（工厂方法）
data = {
    "name": "小明",
    "phone": "15599883377",
    "email": "123456@qq.com"
}
c3 = Contact.from_dict(data)  # ← 不用传 name/phone，直接从字典创建对象
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

# print(Contact.validate_phone("13636")) # False
# print(Contact.validate_phone("13800138000")) # True
print(Contact.validate_email("123456@qq.com"))  # True
print(Contact.validate_name("小明"))  # True

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

'''
# 第五步：`self`参数详解
'''
# 1️⃣ `self` 是什么？—— “我自己！”
# **`self` 就是当前对象的引用**。
# 它让你在类的方法里，能访问“我自己”的属性和方法。
# 2️⃣ 为什么必须写 `self`？—— Python 的显式哲学
# 🐍 Python 的选择：
# **“显式优于隐式”**（Zen of Python）
# 所以 Python **强制你写 `self`**，原因有三：
# | 原因          | 说明                                                        |
# | ------------- | ----------------------------------------------------------- |
# | **1. 明确性** | 一眼看出这是实例属性/方法（`self.name` vs 普通变量 `name`） |
# | **2. 灵活性** | 你可以把方法当成普通函数调用（如 `Contact.is_valid(c)`）    |
# | **3. 一致性** | 所有实例方法都统一格式，没有魔法                            |
# 3️⃣ `self` 与实例的关系 —— “每次调用，自动绑定”
# 关键机制：
# > 当你用 **对象调用方法** 时，Python **自动把对象作为第一个参数传给方法**。
# 🔍 底层过程（以你的代码为例）：
# c = Contact("张三", "13800138000")  # 创建对象，c 是对象的引用
# result = c.is_valid()              # 调用方法

# Python 实际执行的是：

# result = Contact.is_valid(c)  # ← 手动传 c 作为 self

# 所以方法定义必须能接收这个参数 → 这就是 `self` 的由来！

# 4️⃣ 能不能不用 `self`？—— 技术上能，但千万别！
# 📌 **记住：`self` 不是语法要求，而是社区共识。遵守它，你的代码才“Pythonic”**

# ✅ 小结：三句话记住 `self`
# 1. **`self` 就是对象自己**，是方法的第一个参数
# 2. **必须写**，因为 Python 要显式传递对象引用
# 3. **名字可以换，但永远用 `self`**（这是 Python 的礼仪！）

"""
# 第三章：封装（Encapsulation）
# 第六步：访问控制
"""
# 1️⃣ 封装（Encapsulation）—— 信息隐藏的艺术
### ✅ 核心思想：

# > 把对象的**内部实现细节隐藏起来**，只提供**安全的公共接口**供外部使用。
# ✅ 外部代码只需要调用 `contact.is_valid()`，**不需要知道**：

# - 电话是不是 11 位？
# - 名字是不是空？
# - 有没有特殊字符？

# > 这就是封装：**“你只管问我‘是否有效’，别管我怎么判断！”**
# 2️⃣ Python 的“访问控制”—— 没有强制，只有约定
# ⚠️ **重要前提**：

# > **Python 没有像 Java/C++ 那样的 `private`/`protected` 关键字！**
# > 所有属性和方法**默认都是公有的**（public）。

# 但 Python 用 **命名约定** 来表达“访问意图”：
# | 命名方式 | 含义                | 访问建议                       | 你的项目例子       |
# | -------- | ------------------- | ------------------------------ | ------------------ |
# | `name`   | 公有（public）      | ✅ 随便用                       | `contact.name`     |
# | `_name`  | 受保护（protected） | ⚠️ “内部使用，请勿直接访问”     | `_validate()`      |
# | `__name` | 私有（private）     | ❌ “强烈不建议访问”（会改名！） | `__internal_cache` |

# 3️⃣ 详细解析：`_` 和 `__` 的区别
### 🔹 3.1 单下划线 `_xxx` → “受保护”（Protected）

# - **作用**：告诉其他开发者：“这是内部实现，未来可能变，别依赖它”
# - **实际效果**：**没有任何限制**！你仍然可以访问
# - **from module import \*** 时会被忽略（但一般不用 `import *`）

# 💡 **最佳实践**：用 `_` 标记那些“可能变化”或“仅内部使用”的辅助方法/属性。
# ✅ 改进你的代码（建议）：
# class Contact:
#     def __init__(self, name, phone):
#         self.name = name
#         self._phone = phone  # ← 电话应受保护，通过方法访问

#     @property
#     def phone(self):  # ← 公共只读接口
#         return self._phone

#     @phone.setter
#     def phone(self, value):  # ← 公共写入接口（可加验证）
#         if not self._validate_phone(value):
#             raise ValueError("无效电话")
#         self._phone = value

#     def _validate_phone(self, phone):  # ← 内部方法
#         return len(phone) == 11 and phone.isdigit()


# 这样：

# - 外部用 `c.phone`（像公有属性）
# - 内部用 `self._phone` 和 `self._validate_phone()`
# - 未来改验证逻辑，不影响外部代码

# 🔹 3.2 双下划线 `__xxx` → “私有”（Name Mangling）
# - **作用**：触发 **名称改写（Name Mangling）**，避免子类意外覆盖
# - **实际效果**：`__xxx` 会被改名为 `_ClassName__xxx`
# - **不是真正的私有**！只是更难直接访问

#### 🧪 实验：

# class Contact:
#     def __init__(self, name, phone):
#         self.__phone = phone  # ← 双下划线

# c = Contact("张三", "13800138000")

# # 直接访问会报错
# # print(c.__phone)  # ❌ AttributeError

# # 但你可以这样访问（不推荐！）
# print(c._Contact__phone)  # ✅ "13800138000" ← 名称被改写了！

# #### 🔍 查看对象内部：

# print(c.__dict__)
# # 输出: {'_Contact__phone': '13800138000'}

# > ✅ **用途**：当你写框架或库，**绝对不想**让用户/子类碰到某个属性时使用。

# #### ⚠️ 注意：

# - 不要滥用 `__`！大多数情况 `_` 就够了
# - 它主要是为**避免命名冲突**，不是为了“安全”

# 4️⃣ 三种成员对比总结
# | 类型                    | 命名                   | 访问权限           | 用途         | 你的项目建议                     |
# | ----------------------- | ---------------------- | ------------------ | ------------ | -------------------------------- |
# | **公有（Public）**      | `name`, `is_valid()`   | ✅ 任意访问         | 对外 API     | `name`, `phone`（通过 property） |
# | **受保护（Protected）** | `_name`, `_validate()` | ⚠️ 约定不访问       | 内部实现细节 | `_phone`, `_validate_phone()`    |
# | **私有（Private）**     | `__name`               | ❌ 名称改写后可访问 | 避免子类冲突 | 一般不用                         |


# 💡 封装的最佳实践（结合你的项目）
# class Contact:
#     def __init__(self, name, phone):
#         self.name = name          # 公有：直接暴露
#         self._phone = None        # 受保护：内部存储
#         self.phone = phone        # 通过 setter 验证

#     @property
#     def phone(self):
#         return self._phone

#     @phone.setter
#     def phone(self, value):
#         if not self._is_valid_phone(value):
#             raise ValueError("电话必须是11位数字")
#         self._phone = value

#     def _is_valid_phone(self, phone):  # ← 内部方法
#         return phone.isdigit() and len(phone) == 11

#     def is_valid(self):  # ← 公共接口
#         return bool(self.name.strip()) and self._phone is not None


# ✅ 这样做的好处：
# 1. **封装验证逻辑**：外部不能直接改 `phone` 绕过验证
# 2. **清晰的接口**：`c.phone = "123"` 会自动验证
# 3. **易于扩展**：以后加格式化、加密等，只需改内部

## ✅ 小结：三句话记住封装

# 1. **Python 没有真正的私有**，只有命名约定
# 2. **`_xxx` = “请勿直接访问”**，`__xxx` = “我真的不想被访问（会改名）”
# 3. **封装的核心是提供安全接口**，而不是锁死数据

# 此时的phone是property对象
print(Contact.phone)
print(c1.phone)  # 读取的时候，会自动调用 @property 装饰的方法，对象.属性
c1.phone = "15522990011"  # 写入的时候，会自动调用 @phone.setter 装饰的方法
print(c1.phone)

# 补充：
# 1️⃣ 如何用 @property 实现只读属性？
# ✅ 什么是只读属性？
# 外部可以读取，但不能修改的属性。

# 🔧 实现方法：
# 只定义 @property，不定义 @xxx.setter

# 🧪 你的项目实战：让 created_at 只读

c = Contact("张三", "13800138000")
# 读取的时候，会自动调用 @property 装饰的方法，对象.属性(直接访问created_at名字，不需要加括号)
print(c.created_at)  # ✅ 可以读：2025-10-06 15:30:45.123456
# c.created_at = "2020-01-01"  # ❌ 报错！
# 💡 其他只读属性场景（你的项目中）：
# | 属性                        | 为什么只读？                                   |
# | --------------------------- | ---------------------------------------------- |
# | `id`                        | 数据库主键，不应被修改                         |
# | `created_at` / `updated_at` | 时间戳，应由系统自动管理                       |
# | `full_info`                 | 计算属性（如 `"张三 <138...>"`），不应直接赋值 |

# 例子：计算型只读属性
c3 = Contact("lisi", "13800138000")
# 读取的时候，会自动调用 @property 装饰的方法，对象.属性(直接访问full_info名字，不需要加括号)
print(c3.full_info)  # ✅ 可以读：lisi <13800138000>

# 2️⃣ 如何避免 setter 无限递归？
### ❓ 什么是 setter 无限递归？


# 当你在 setter 里**不小心又给自己赋值**，就会不断调用自己，直到栈溢出。
# 🚫 错误示范（你绝对会遇到！）：
class Contact1:
    @property
    def phone(self):
        return self.phone  # ❌ 错！读取时又触发 property → 无限递归！

    @phone.setter
    def phone(self, value):
        self.phone = value  # ❌ 错！赋值时又触发 setter → 无限递归！


# 运行任一都会报错：
# RecursionError: maximum recursion depth exceeded
### ✅ 正确做法：**用不同的内部属性名存储数据**

#### 原则：


# > **property 的名字（如 `phone`）≠ 内部存储的名字（如 `_phone`）**
# 🔧 正确代码模板：
class Contact2:
    def __init__(self, name, phone):
        self._phone = None  # ← 内部存储用 _phone
        self.phone = phone  # ← 通过 property 赋值

    @property
    def phone(self):  # 读取接口
        return self._phone  # ← 返回内部属性

    @phone.setter
    def phone(self, value):  # 写入接口
        # 在这里做验证、日志等
        if not value.isdigit():
            raise ValueError("电话必须是数字")
        self._phone = value  # ← 存到内部属性，不再触发 setter！


### 🧠 为什么这样就安全？

# - `self.phone = ...` → 触发 setter → 执行 `self._phone = ...`
# - `self._phone` 是**普通属性**，赋值不会触发任何方法
# - **没有循环调用**！

# 🛠 命名建议（行业惯例）：
# | 用途               | 命名方式 | 例子      |
# | ------------------ | -------- | --------- |
# | 公共属性接口       | `xxx`    | `phone`   |
# | 内部存储           | `_xxx`   | `_phone`  |
# | 私有存储（极少见） | `__xxx`  | `__phone` |

# ✅ **永远不要在 property 的 getter/setter 里使用和 property 同名的属性！**

# 🧪 综合实战：安全的 Contact 类

# from datetime import datetime

# class Contact:
#     def __init__(self, name, phone):
#         self.name = name
#         self._phone = None
#         self.phone = phone          # 触发 setter 验证
#         self._created_at = datetime.now()

#     @property
#     def phone(self):
#         return self._phone

#     @phone.setter
#     def phone(self, value):
#         if not (isinstance(value, str) and value.isdigit() and len(value) == 11):
#             raise ValueError("电话必须是11位数字字符串")
#         self._phone = value

#     @property
#     def created_at(self):  # 只读
#         return self._created_at

#     @property
#     def full_info(self):   # 只读计算属性
#         return f"{self.name} <{self.phone}>"

# ✅ 测试所有功能：
c = Contact("王五", "13500135000")
print(c.full_info)  # "王五 <13500135000>"
print(c.created_at)  # 2025-10-06 15:40:00.123456

c.phone = "13600136000"  # ✅ 可修改（经过验证）
print(c.phone)  # "13600136000"

# ✅ 小结：两句话记住
# 1. **只读属性**：只写 `@property`，不写 `@xxx.setter`
# 2. **避免递归**：property 用 `xxx`，内部存储用 `_xxx`（名字必须不同！）

"""
第七步：属性管理
"""
# 1. **为什么需要 property？** → 用方法控制属性访问，但保持点号语法
# 2. **`@property`** → 定义 getter（读取）
# 3. **`@<name>.setter`** → 定义 setter（写入）
# 4. **`@<name>.deleter`** → 定义 deleter（删除）
# 5. **三者如何协同工作？**

# 2️⃣ 三位一体：getter / setter / deleter
# 🔧 完整模板（记住这个结构！）：

# class MyClass:
#     def __init__(self, value):
#         self.my_attr = value  # ← 触发 setter

#     @property
#     def my_attr(self):                # ← getter
#         """读取 my_attr"""
#         return self._my_attr

#     @my_attr.setter
#     def my_attr(self, value):         # ← setter
#         """设置 my_attr（可加验证）"""
#         self._my_attr = value

#     @my_attr.deleter
#     def my_attr(self):                # ← deleter
#         """删除 my_attr"""
#         self._my_attr = None
#         # 或 del self._my_attr


# 📌 **关键**：三个方法**必须同名**，且都用 `@property`、`@name.setter`、`@name.deleter` 装饰

# 3️⃣ 你的 Contact 类实战：完整属性管理
from datetime import datetime


class Contact_Demo:
    # “phone 是一个可选参数，类型是字符串或空值，默认为 None”
    def __init__(
        self, name: str, phone: str | None = None, created_at: str | None = None
    ) -> None:
        self.name = name
        self.phone = phone  # 触发 setter 验证, 这里不创建_phone, setter的时候会创建
        self._created_at = datetime.now()

    @property
    def phone(self) -> str:
        """读取电话号码"""
        if not self._phone:
            return "未设置"
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:  # setter方法没有返回值
        """设置电话号码（可加验证）"""
        if value is None:
            self._phone = None  # ← 创建 _phone 属性！
            return
        if not (isinstance(value, str) and value.isdigit() and len(value) == 11):
            raise ValueError("手机号必须是11位数字字符串")
        self._phone = value  # ← 创建 _phone 属性！

    @phone.deleter
    def phone(self) -> None:
        """删除电话号码"""
        self._phone = None

    @property
    def created_at(self) -> str:
        return self._created_at
        # 每次调用都会返回新的当前时间（如果属性不存在）。不会缓存！
        # return getattr(self, '_created_at', datetime.now())


# 4️⃣ 测试所有操作（CRUD）
contact_Demo = Contact_Demo("小明")

print(contact_Demo.phone)  # 未设置

contact_Demo.phone = "13899330022"
print(contact_Demo.phone)  # 13899330022

# 无效赋值（触发验证）
try:
    contact_Demo.phone = "123"
except ValueError as e:
    print(e)  # "手机号必须是11位数字字符串"

del contact_Demo.phone
print(contact_Demo.phone)  # 未设置

print(contact_Demo.created_at)  # 2025-10-06 17:52:59.224081

# 5️⃣ 关于 `@<name>.deleter` 的重要说明
### ❓ 什么时候需要 deleter？

# - 当你希望支持 `del obj.attr` 语法
# - 并且需要**自定义删除行为**（如清理资源、记录日志等）

### ⚠️ 如果没定义 deleter：

# class Simple:
#     @property
#     def data(self):
#         return self._data

# 使用
# s = Simple()
# s._data = "hello"
# del s.data  # ❌ AttributeError: can't delete attribute 'data'

### ✅ 如果定义了 deleter：

# - `del obj.attr` 会调用你的 deleter 方法
# - 你可以在里面做任何事（设为 None、删除键、关闭连接等）

# 6️⃣ 高级技巧：动态属性 or 计算属性
# 💡 场景：`full_name` 由 `first_name` + `last_name` 组成


class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        parts = value.split(" ", 1)
        self.first_name = parts[0]
        self.last_name = parts[1] if len(parts) > 1 else ""


# 使用
p = Person("张", "三丰")
print(p.full_name)  # 张 三丰
p.full_name = "李 小龙"
print(p.first_name)  # 李
print(p.last_name)  # 小龙

# ✅ 这就是 **计算属性的双向绑定**！
# ✅ 小结：property 三件套
# | 装饰器          | 作用               | 是否必需             | 你的项目用途           |
# | --------------- | ------------------ | -------------------- | ---------------------- |
# | `@property`     | 定义 getter（读）  | ✅ 必须先有它         | 读取 phone、created_at |
# | `@name.setter`  | 定义 setter（写）  | ❌ 可选（只读就不写） | 验证并设置 phone       |
# | `@name.deleter` | 定义 deleter（删） | ❌ 可选               | 安全删除 phone         |


# 🔑 **记住**：

# - 先有 `@property`，才能有 `.setter` 和 `.deleter`
# - 三个方法**函数名必须相同**
# - 内部存储用 `_xxx` 避免递归

'''
# 第八步：**`__dict__` 与动态属性**
'''
# 💥 Python 的强大之处在于：**对象的属性不是固定的，可以在运行时动态增删改查！**  
# 而这一切的背后，就是 `__dict__` —— **每个对象的“属性仓库”**。

# 1️⃣ `__dict__` 是什么？—— 对象的“属性仓库”
# 在 Python 中，**每个对象（实例）默认都有一个 `__dict__` 属性**，它是一个字典（`dict`），存储了该对象的所有**实例属性**。
print(c1.__dict__)
# {'_name': 'Alice', '_phone': '15522990011', '_email': '123456@qq.com', '_created_at': '2025-10-07T11:57:35.017702'}
# ✅ **`__dict__` 就是对象所有属性的“真相”**！
# 2️⃣ 类也有 `__dict__`！但内容不同
print(Contact.__dict__.keys())
# **输出**（部分）：
# dict_keys(['__module__', '__firstlineno__', '__annotations__', '__doc__', 'species', 'VERSION', '__init__', '__str__', '__repr__', 'from_dict', 'get_version', 'validate_email', 'validate_name', 'validate_phone', 'name', 'phone', '_is_valid_phone', 'email', '_is_valid_email', 'created_at', 'is_valid', 'full_info', '__static_attributes__', '__dict__', '__weakref__'])
# ⚠️ 注意：  
# - **类的 `__dict__` 存的是类属性、方法、描述符（如 `@property`）**  
# - **实例的 `__dict__` 存的是实例变量（如 `_name`）**  
# - `@property` 定义的 `phone` 是**类属性（描述符）**，不会出现在实例的 `__dict__` 中！
# 3️⃣ 动态添加/修改/删除属性
# Python 允许你在**运行时**给对象添加新属性，哪怕类定义里没有！
# ✅ 动态添加属性
print(c1.__dict__)
c1.age = 30    # 动态添加属性
c1.roles = ["student", "teacher"]  # 动态添加属性
print(c1.__dict__)  # {'_name': 'Alice', '_phone': '15522990011', '_email': '123456@qq.com', '_created_at': '2025-10-07T11:57:35.017702', 'age': 30, 'roles': ['student', 'teacher']}
# ✅ 动态修改
c1.age = 66
print(c1.__dict__)  # {'_name': 'Alice', '_phone': '15522990011', '_email': '123456@qq.com', '_created_at': '2025-10-07T11:57:35.017702', 'age': 66, 'roles': ['student', 'teacher']}

# ✅ 动态删除
del c1.age  # 删除属性
del c1.roles
print(c1.__dict__)
print(hasattr(c1, "age"))  # False
print(hasattr(c1, "roles"))  # False

# 4️⃣ 更安全的方式：`getattr()` / `setattr()` / `delattr()`
# 虽然可以直接用 `obj.attr = value`，但在**属性名是变量**时，必须用内置函数：
# | 操作 | 直接语法           | 函数式（推荐动态场景）          |
# | ---- | ------------------ | ------------------------------- |
# | 读取 | `obj.attr`         | `getattr(obj, 'attr', default)` |
# | 写入 | `obj.attr = value` | `setattr(obj, 'attr', value)`   |
# | 删除 | `del obj.attr`     | `delattr(obj, 'attr')`          |

# 🔧 示例：批量设置属性
c5 = Contact("lisi")
# 属性名来自外部（如配置文件、用户输入）
fields = {"age": 49, "department": "IT"}
for key, value in fields.items():
    setattr(c5, key, value) # 动态设置
print(c5.__dict__)
print(hasattr(c5, "age"))  # True
print(c5.department)  # IT

# 🔒 安全读取（带默认值）
priority = getattr(c5, "priority", "普通") #如果没有priority，返回"普通"
print(priority)
# 🔒 安全删除
delattr(c5, "department")
print(hasattr(c5, "department"))  # False

# 5️⃣ 动态属性 vs `@property`：谁优先？
# **关键规则**：  
# **实例属性（在 `__dict__` 中）会覆盖同名的类属性（包括 `@property`）！**
### ⚠️ 危险示例：

# c = Contact("赵六", "13900139000")
# print(c.phone)  # 13900139000 （通过 @property getter）

# ❌ 错误：直接给 phone 赋值（绕过 setter！）
# c.phone = "绕过验证的垃圾数据"  # ← 这会创建实例属性 phone！

# print(c.phone)  # "绕过验证的垃圾数据" （不再调用 @property！）
# print(c.__dict__)  # {'_name': ..., '_phone': '13900139000', 'phone': '绕过验证...'}

# 💥 **`@property` 被“遮蔽”了！** 因为实例字典里有了 `phone`，Python 不再查找类的描述符。

# ✅ 正确做法：
# - 永远通过**公共接口**操作属性（即 `c.phone = ...` 会调用 setter）
# - **不要**手动给 `@property` 同名的属性赋值（除非你知道后果）

# 6️⃣ 什么时候用动态属性？—— 场景与陷阱
# ✅ 推荐场景：
# | 场景               | 说明                                                         |
# | ------------------ | ------------------------------------------------------------ |
# | **配置对象**       | `config.debug = True`，属性名不固定                          |
# | **ORM / 数据模型** | 从数据库行动态创建对象属性                                   |
# | **插件系统**       | 运行时注入新功能                                             |
# | **JSON 反序列化**  | 把字典转成对象：`for k, v in data.items(): setattr(obj, k, v)` |
# ❌ 避免场景：
# | 场景                 | 风险                                     |
# | -------------------- | ---------------------------------------- |
# | **替代明确的类设计** | 如果你知道属性名，就该写在 `__init__` 里 |
# | **破坏封装**         | 绕过 `@property` 的验证逻辑              |
# | **团队协作**         | 动态属性难以被 IDE 识别，降低可读性      |

# 7️⃣ 如何禁止动态属性？—— `__slots__`
# 如果你希望**禁止动态添加属性**（提升性能 + 防止误用），可以用 `__slots__`：

class StrictContact:
    __slots__ = ("_name", "_phone", "_created_at") #只允许创建这三个属性

    def __init__(self, name, phone = None, created_at = None):
        self._name = name
        self._phone = phone
        self._created_at = datetime.now().isoformat()
sc = StrictContact("小明")
# sc.age = 29 # AttributeError: 'StrictContact' object has no attribute 'age' and no __dict__ for setting new attributes

# ✅ `__slots__` 会：
# - 禁止 `__dict__`（节省内存）
# - 只允许预定义的属性
# - 常用于高性能或嵌入式场景    
# ✅ 小结：`__dict__` 与动态属性核心要点
# | 概念                   | 说明                                                        |
# | ---------------------- | ----------------------------------------------------------- |
# | **`obj.__dict__`**     | 对象的属性字典，存储所有实例变量                            |
# | **动态添加**           | `obj.new_attr = value` 或 `setattr(obj, 'new_attr', value)` |
# | **动态读取**           | `getattr(obj, 'attr', default)`（安全！）                   |
# | **`@property` 优先级** | 实例属性会覆盖同名的 `@property`（危险！）                  |
# | **`__slots__`**        | 禁止动态属性，提升性能和安全性                              |

# 动手练习：用 `__dict__` 实现 `to_dict()`
# 给你的 `Contact` 类加一个方法，把对象转成字典（常用于 API 返回）：
print("to_dict():",c1.to_dict())
print("__dict__:",c1.__dict__)
print("to_dict_dynamic():",c1.to_dict_dynamic())

