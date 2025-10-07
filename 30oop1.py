"""
**第四章：继承（Inheritance）** —— 面向对象三大支柱之一！
🎯 **继承的核心思想**：
**“子类自动拥有父类的能力，并可以扩展或修改它。”**
"""

"""
# 第四章：继承（Inheritance）
# 第九步：单继承
"""


# 1️⃣ 单继承：子类继承父类
# ✅ 语法：`class 子类(父类):`
class Parent:
    def greet(self):
        print("Hello from Parent!")


# 子类继承父类
class Child(Parent):
    pass  # 什么都不写，但已经继承了父类的所有能力！


c = Child()
c.greet()  # 输出：Hello from Parent!
# 🔑 **关键点**：
# - Python 支持**多继承**，但**单继承最常用、最清晰**
# - 子类自动获得父类的**所有方法和属性**


# 2️⃣ 方法重写（Override）：定制行为
# 子类可以**重新定义父类的方法**，实现自己的逻辑。
# 🌰 示例：重写 `__repr__`
class Contact:
    def __init__(self, name: str, phone: str | None = None) -> None:
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"Contact(name={self.name!r}, phone={self.phone!r})"


# VIP联系人，重写`__repr__`
class VIPContact1(Contact):
    def __repr__(self):
        return f"🌟 VIPContact(name={self.name!r}, phone={self.phone!r})"


# 测试
c1 = Contact("张三")
c2 = VIPContact1("李四")
print(c1)  # 输出：Contact(name='张三', phone=None)
print(c2)  # 输出：🌟 VIPContact(name='李四', phone=None)
# ✅ **重写规则**：
# - 方法名必须**完全相同**（包括参数）
# - 子类方法会**完全替代**父类方法（除非你主动调用父类）


# 3️⃣ `super()`：调用父类逻辑（关键！）
# 很多时候，我们**不想完全替换父类行为，而是“在父类基础上扩展”**。
# 🛠 用法：`super().方法名(...)`
# 🌰 示例：扩展 `__init__`
class VIPContact2(Contact):
    def __init__(self, name, phone=None, level: int = 1):
        # ✅ 先调用父类的 __init__，初始化 name 和 phone
        super().__init__(name, phone)
        # ✅ 再初始化自己的新属性
        self.level = level  # VIP等级 （1~5）

    def __repr__(self):
        # 调用父类的 __repr__ 并扩展
        base_repr = super().__repr__()
        return f"🌟 VIP(level={self.level}) {base_repr}" 
# 测试
vip = VIPContact2("李四", "13800138000", level=4)
print(vip)  # 输出：🌟 VIP(level=4) Contact(name='李四', phone='13800138000')
# 🔥 **`super()` 的作用**：  
# - 避免重复写父类逻辑（如验证 `name`）  
# - 保持代码可维护性（父类改了，子类自动受益）  
# - 支持多继承时的正确方法解析顺序（MRO）
# 4️⃣ 属性继承与扩展
# 子类可以：
# - **继承**父类的所有属性（包括 `@property`）
# - **添加**自己的新属性
# - **重写**父类的属性（谨慎！）

# 🌰 示例：VIP 联系人专属属性
class VIPContact3(Contact):
    def __init__(self, name, phone: str | None = None, level: int = 1):
        super().__init__(name, phone)
        self._validate_level(level)  # ← 调用公共校验
        self._level = level

    @property
    def level(self) -> int:
        return self._level
    @level.setter
    def level(self, value: int) -> None:
        self._validate_level(value)  # ← 调用公共校验
        self._level = value
    # 新方法 ：升级VIP等级
    def upgrade(self) -> None:
        if self.level < 5:
            self.level += 1
            print(f"VIP等级升级为 {self.level}")

    # 提取公用的校验逻辑
    def _validate_level(self, value: int) -> None:
        """私有方法：统一校验 VIP 等级"""
        if not(1 <= value <= 5) or not isinstance(value, int):
            raise ValueError("VIP等级必须是 1~5 之间的整数！")

vip = VIPContact3("lisi", "13899889900")
print(vip.level)  # 输出：1
vip.upgrade()  # 输出：VIP等级升级为 2
print(vip.level)  # 输出：2

# 避免代码重复？可以用“私有校验方法”优化
# 你说“写两遍校验逻辑”感觉重复，这个直觉是对的！  
# 但解决方案**不是删掉 setter 的校验**，而是**提取公共逻辑**。
# ✨ 优化写法：提取 `_validate_level`
class VIPContact4(Contact):
    def __init__(self, name: str, phone: str | None = None, level: int = 1):
        super().__init__(name, phone)
        self._validate_level(level)  # ← 调用公共校验
        self._level = level

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, value: int):
        self._validate_level(value)  # ← 同样调用
        self._level = value

    def _validate_level(self, value: int):
        """私有方法：统一校验 VIP 等级"""
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("VIP 等级必须是 1~5 的整数")

    def upgrade(self):
        if self.level < 5:
            self.level += 1  # ← 这里也会触发 setter 校验！
            print(f"🎉 VIP 等级已升至 {self.level}！")
# ✅ **好处**：
# - 校验逻辑**只写一次**
# - `__init__` 和 `setter` **都复用它**
# - 未来修改规则（比如支持 1~10）只需改一处
# 🔁 **这是“不要重复自己”（DRY）原则的正确应用方式**：  
# **提取重复逻辑，而不是删除必要的校验**。

# 5️⃣ 类型检查：`isinstance()` 与 `issubclass()`
# ✅ `isinstance(obj, 类)`：检查对象是否是某类（或子类）的实例
c = Contact("Alice")
vip = VIPContact3("Bob", level=3)
print(isinstance(c, Contact))  # 输出：True
print(isinstance(vip, Contact))  # 输出：True ✅ VIPContact 是 Contact 的子类！
print(isinstance(c, VIPContact3))  # 输出：False
print(isinstance(vip, VIPContact3))  # 输出：True

# ✅ `issubclass(子类, 父类)`：检查类之间的继承关系
print(issubclass(VIPContact3, Contact))  # 输出：True
print(issubclass(Contact, VIPContact3))  # 输出：False
# 💡 **多态的基础**：你可以把 `VIPContact` 当作 `Contact` 使用！
# 6️⃣ 完整实战：`Contact` → `VIPContact`
from datetime import datetime
class ContactDemo:
    def __init__(self, name: str, phone: str | None = None):
        if not name.strip():
            raise ValueError("姓名不能为空！")
        self._name = name.strip()
        self._phone = phone
        self._created_at = datetime.now().isoformat()
    @property
    def name(self) -> str:
        return self._name
    @property
    def phone(self) -> str:
        return self._phone if self._phone else "未设置"
    def __repr__(self):
        return f"Contact(name={self.name!r}, phone={self.phone!r})"
class VIPContactDemo(ContactDemo):
    def __init__(self, name, phone: str | None = None, level: int = 1):
        super().__init__(name, phone)
        self.level = level
    @property
    def level(self) -> int:
        return self._level
    @level.setter
    def level(self, value: int) -> None:
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("VIP等级必须是 1~5 之间的整数！")
        self._level = value
    def __repr__(self):
        return f"VIPContact(name={self.name!r}, phone={self.phone!r}, level={self.level!r})"
    def assign_dedicated_manager(self):
        """为 VIP 联系人分配专属经理"""
        print(f"为 VIP 联系人 {self.name} 分配专属经理")
    def upgrade(self):
        if self.level < 5:
            self.level += 1
            print(f"VIP等级升级为 {self.level}")
            
# 测试
c = ContactDemo("lisi", "15588993300")
vip = VIPContactDemo("zhangsan", "14488993322", level=2)
print(vip)
vip.assign_dedicated_manager()
vip.upgrade()

# 多态
contacts = [c, vip]
for contact in contacts:
    print(contact) # 自动调用各自的 __repr__
# ✅ 继承的核心原则
# | 原则                       | 说明                                                         |
# | -- |  |
# | **IS-A 关系**              | “VIPContact **是** 一种 Contact” → 适合用继承                |
# | **不要为了复用代码而继承** | 如果只是想复用方法，考虑**组合（Composition）**              |
# | **Liskov 替换原则**        | 子类对象应该能**无缝替换**父类对象（你的 VIPContact 完全符合！） |
# | **优先组合，其次继承**     | 但当 IS-A 成立时，继承是最自然的选择                         |

'''
# 第十步：多继承
'''
#  第一部分：多继承基础语法
# ✅ 语法：`class 子类(父类1, 父类2, ...):`
class A:
    def method(self):
        print("A.method")
class B:
    def method(self):
        print("B.method")
class C(A, B):
    pass

c = C()
c.method() # 输出：A.method， # 输出什么？→ 看 MRO！

# 📌 **关键点**：

# - Python 支持任意数量的父类
# - 子类会继承**所有父类的方法和属性**
# - 如果多个父类有同名方法，**MRO 决定谁先被调用**

# 🔹 第二部分：方法解析顺序（MRO）——多继承的灵魂
# 🎯 什么是 MRO？
# **MRO（Method Resolution Order）** 是 Python 在多继承中**查找方法的顺序列表**。  
# 它决定了：当调用 `obj.method()` 时，Python 先找哪个类的 `method`。
# 🔍 如何查看 MRO？类名.__mro__
print(C.__mro__)  # 输出：(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# - MRO 是一个**元组**，从左到右表示查找优先级
# - **越靠左，优先级越高**
# 所以 `c.method()` 会调用 `A.method`（因为 A 在 B 前面）。

# 💎 深入：C3 线性化算法（MRO 的计算规则）
# Python 使用 **C3 算法** 计算 MRO，规则如下（简化版）：

# 1. **子类优先于父类**
# 2. **父类声明顺序保留**（即 `class C(A, B)` 中 A 在 B 前）
# 3. **单调性**：父类的 MRO 顺序不能被破坏
# 🌰 经典案例：钻石问题（Diamond Problem）
class A:
    def method(self):
        print("A.method")
class B(A):
    def method(self):
        print("B.method")
class C(A):
    def method(self):
        print("C.method")
class D(B, C): # B 在 C 前
    pass
print(B.__mro__)
print(C.__mro__)
print(D.__mro__)
d = D()
d.method()  # 输出：B.method
print("============================================")
# 🔍 计算 D 的 MRO：
# - `B.__mro__` = (B, A, object)
# - `C.__mro__` = (C, A, object)
# - `D.__mro__` = (D, B, C, A, object) ← **C3 合并结果**
# ✅ 所以 `d.method()` 调用的是 **`B.method`**（因为 B 在 C 前）。
# 📌 **关键结论**：  
# **Python 的 MRO 保证了每个类在 MRO 中只出现一次，且父类顺序合理**，从而**解决了钻石问题**！

# 🔹 第三部分：`super()` 的真实工作原理

### ❌ 常见误解：

# “`super()` 就是调用父类方法”

### ✅ 真相：

# **`super()` 返回一个代理对象，它会从当前类的 MRO 中，找到“下一个类”并调用其方法。**

# 🔧 语法：
# super()  # Python 3 简写，等价于 super(当前类, self)

# 🌰 示例：多继承中的 `super()` 协作
class A:
    def method(self):
        print("A.method")
class B(A):
    def method(self):
        print("B.method")
        super().method() # ← 调用 MRO 中 B 的下一个类（即 C）
class C(A):
    def method(self):
        print("C.method")
        super().method()  # ← 调用 A.method
class D(B, C):
    def method(self):
        print("D.method")
        super().method()  # ← 调用 B.method
d = D()
d.method()
# 🧠 执行流程（按 MRO: D → B → C → A）：
# 1. `D.method()` → 打印 "D.method"，调用 `super().method()` → 进入 **B**
# 2. `B.method()` → 打印 "B.method"，调用 `super().method()` → 进入 **C**（不是 A！）
# 3. `C.method()` → 打印 "C.method"，调用 `super().method()` → 进入 **A**
# 4. `A.method()` → 打印 "A.method"
# ✅ 输出：
# D.method
# B.method
# C.method
# A.method
# 💥 **这就是 `super()` 的魔力**：  
# 它让所有类**协作完成一次完整的方法调用链**，而不是各自为政。
# ✅ **结论：在多继承中，必须用 `super()`，不能硬编码父类名！**

# 🔹 第四部分：实战模式 —— Mixin（推荐的多继承用法）
## ✅ 正确思路：**功能拆分 + 按需组合**

# 我们希望：
# - 把“JSON 序列化”做成一个**独立模块**
# - 把“日志记录”做成另一个**独立模块**
# - 然后像“搭积木”一样，**按需混入（Mixin）到任何类**
# 这就是 **Mixin 模式** 的核心思想！

# 🔹 Mixin定义（通俗版）：
# **Mixin 是一种“功能插件”类**，它：
# Mixin 是一个“功能插件”类，它不独立使用，只用来给其他类“添加能力”。
# - 不独立使用
# - 只提供**特定功能**
# - 通过多继承“混入”到主类中

# 🔹 Mixin 的 5 个关键特征：
# | 特征                        | 说明                                          | 为什么重要                   |
# |  |  | - |
# | **1. 不单独实例化**         | 你不会写 `m = JsonMixin()`                    | 它只是“功能包”，不是完整对象 |
# | **2. 不继承业务类**         | Mixin 通常只继承 `object`（或什么都不写）     | 避免污染继承链               |
# | **3. 方法名设计避免冲突**   | 用明确名字，如 `to_json()` 而不是 `process()` | 防止和主类方法重名           |
# | **4. 通常不调用 `super()`** | 除非明确知道 MRO                              | 避免意外调用未知类           |
# | **5. 通过多继承“混入”**     | `class MyClass(Base, Mixin1, Mixin2)`         | 实现灵活组合                 |

# 🌰 实战：为 `Contact` 添加功能
# ===== Mixin类 1: 功能是：JSON 序列化 =====
import json
from datetime import datetime
class JsonSerializableMixin:
    """JSON 序列化混入类"""
    # 子类可覆盖此属性，指定要序列化的字段名
    _JSON_FIELDS = None  # 默认 None 表示用 __dict__ 过滤

    def to_json(self):

        if self._JSON_FIELDS is not None:
            # 显式指定字段：支持属性（property）和普通属性
            data = {field: getattr(self, field) for field in self._JSON_FIELDS}
        else:
            # 默认行为：只取非私有属性
            # 获取所有 public 属性（非下划线开头）
            data = {
                k: v for k, v in self.__dict__.items()
                if not k.startswith("_")
            }
        return json.dumps(data, ensure_ascii=False, indent=2)
# ===== Mixin类 2: 功能是：日志记录 =====
class LoggableMixin:
    """日志记录混入类"""
    def log_action(self, action: str):
        print(f"[{datetime.now()}] {self.__class__.__name__} {action}")
# ===== 主类 + Mixin =====
class VIPContact(Contact, JsonSerializableMixin, LoggableMixin):
    _JSON_FIELDS = ("name", "phone", "level")
    def __init__(self, name, phone: str | None = None, level: int = 1):
        super().__init__(name, phone)
        self.level = level
        self.log_action("创建 VIP 联系人") # 使用 Mixin 的方法
    @property
    def level(self) -> int:
        return self._level
    @level.setter
    def level(self, value: int) -> None:
        if not (1 <= value <= 5) or not isinstance(value, int):
            raise ValueError("等级必须是 1-5 的整数")
        self._level = value
        self.log_action(f"VIP 等级升级到 {self._level}")
    def __repr__(self):
        return f"VIPContact(name='{self.name}', phone='{self.phone}', level={self.level})"
# 测试：
vip = VIPContact("lisi", "13899889900", level=2)
print(vip.to_json())
vip.level = 4
print(vip.to_json())


# ✅ **优势**：

# - 功能解耦：日志、JSON 序列化独立成模块
# - 复用性强：任何类都可以混入这些功能
# - 避免复杂继承树

# Mixin vs 普通多继承 vs 组合
# | 方式                    | 适用场景                                                    | 优点                             | 缺点                     |
# | -- | -- | -- |  |
# | **Mixin（多继承）**     | 添加通用功能（JSON、日志、序列化）                          | 代码简洁、自动继承、方法直接可用 | 需理解 MRO，属性名需小心 |
# | **普通多继承**          | 真实的“既是 A 又是 B”关系（如“鸭子既是鸟又是会游泳的动物”） | 表达 IS-A 关系                   | 容易复杂，MRO 难理解     |
# | **组合（Composition）** | “拥有”某个功能（如 `contact.logger.log(...)`）              | 更灵活、更安全、更容易测试       | 代码稍啰嗦，需手动代理   |

# ✅ **经验法则**：  

# - 如果功能是 **“附加能力”** → 用 **Mixin**  
# - 如果关系是 **“本质身份”** → 用 **单继承**  
# - 如果功能复杂或需要配置 → 用 **组合**

# ✅ 总结：Mixin 的核心思想
# > **“把横切关注点（cross-cutting concerns）封装成可复用的插件，通过多继承按需组合。”**

# - **横切关注点**：日志、序列化、权限检查、缓存等，**与业务逻辑无关但到处需要的功能**
# - **Mixin 就是这些功能的“标准化插件”**

# 🔹 第五部分：常见陷阱与最佳实践
### 🚫 陷阱 1：`__init__` 初始化顺序混乱

class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        print("B init")
        super().__init__()

class C(A):
    def __init__(self):
        print("C init")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D init")
        super().__init__()

# ✅ **正确输出**（按 MRO: D → B → C → A）：

# D init
# B init
# C init
# A init

# > 🔑 **关键**：每个 `__init__` 必须调用 `super().__init__()`，否则链会中断！


### 🚫 陷阱 2：属性名冲突

class Mixin1:
    def __init__(self):
        self.config = "mixin1"

class Mixin2:
    def __init__(self):
        self.config = "mixin2"  # ← 覆盖了 Mixin1 的 config！

class MyClass(Mixin1, Mixin2):
    pass

# ✅ **解决方案**：

# - 使用**私有属性**（`_mixin1_config`）
# - 或使用**命名空间**（`self.mixin1_config`）

# ✅ 最佳实践总结
# | 建议                                          | 说明                                      |
# |  | -- |
# | **优先使用 Mixin 模式**                       | 而不是复杂的多继承层次                    |
# | **所有方法用 `super()`**                      | 确保 MRO 链完整                           |
# | **每个 `__init__` 调用 `super().__init__()`** | 避免初始化遗漏                            |
# | **避免属性名冲突**                            | 用前缀或私有属性                          |
# | **用 `cls.__mro__` 调试**                     | 不确定顺序时，打印 MRO                    |
# | **不要为了复用而继承**                        | 如果只是复用方法，考虑组合（Composition） |

# 📌 终极建议：何时使用多继承？
# | 场景                                      | 推荐方案                        |
# | -- | - |
# | **IS-A 关系**（如 VIPContact 是 Contact） | ✅ 单继承                        |
# | **HAS-A 功能**（如“可序列化”、“可日志”）  | ✅ Mixin（多继承的一种安全形式） |
# | **复杂业务继承树**                        | ❌ 改用组合（Composition）       |

# 🌟 **记住**：  
# **“组合优于继承”**，但 **“Mixin 是多继承的安全子集”**。


'''
第十一步：**`isinstance()` 与 `issubclass()`**

'''

# **`isinstance()` 与 `issubclass()`** —— 这两个 Python 中用于**运行时类型检查**的核心函数。
# - `isinstance(obj, 类)`：检查对象是否是某类（或子类）的实例
# - `issubclass(子类, 父类)`：检查类之间的继承关系

# 🔹 第一部分：`isinstance(obj, class_or_tuple)` —— 检查对象类型
### 📌 一句话定义：

# > **`isinstance(obj, Class)` 返回 `True`，当且仅当 `obj` 是 `Class` 或其任意子类的实例。**

### ✅ 基础语法

# isinstance(对象, 类)          # 检查是否是某个类的实例
# isinstance(对象, (类1, 类2))  # 检查是否是多个类中任意一个的实例

### 🌰 示例 1：基本用法
class Animal: pass
class Dog(Animal): pass
dog = Dog()

print(isinstance(dog, Animal))  # 输出：True ← 继承关系被认可！
print(isinstance(dog, Dog))     # 输出：True
print(isinstance(dog, object))  # 输出：True ← 所有类都继承 object
print(isinstance(dog, str))     # 输出：False

# 🌰 示例 2：支持元组（多类型检查）
x = 42 
print(isinstance(x, (int, float)))  # 输出：True
y = "hello"
print(isinstance(y, (list, dict, str))) # 输出：True
# 💡 这等价于：`isinstance(x, int) or isinstance(x, float)`
# ⚠️ 重要：`isinstance` vs `type()`
# | 写法                     | 是否认子类？ | 推荐度          |
# |  |  |  |
# | `isinstance(obj, Class)` | ✅ 认子类     | ⭐⭐⭐⭐⭐           |
# | `type(obj) is Class`     | ❌ 不认子类   | ⭐（仅特殊场景） |
# 🌰 对比演示：

class MyInt(int): pass
x = MyInt(10)
print(type(x) is int)  # 输出：False
print(isinstance(x, int))  # 输出：True
# 📌 **结论**：  
# **永远优先用 `isinstance`，除非你明确需要“精确类型匹配”（极少见）**

# 🔹 第二部分：`issubclass(cls, class_or_tuple)` —— 检查类的继承关系
### 📌 一句话定义：

# > **`issubclass(A, B)` 返回 `True`，当且仅当 `A` 是 `B` 的子类（直接或间接）。**

# ✅ 基础语法
# issubclass(子类, 父类)
# issubclass(类, (父类1, 父类2))  # 是否是任一父类的子类
# 🌰 示例：
class Amimal: pass
class Mammal(Animal): pass
class Dog(Mammal): pass

print(issubclass(Dog, Animal))  # 输出：True  ← 间接继承也算！
print(issubclass(Dog, Mammal))  # 输出：True
print(issubclass(Animal, Dog))  # 输出：False
print(issubclass(Dog, object))  # 输出：True
print(issubclass(Dog, (Mammal, Animal)))  # 输出：True

# 🌰 多继承场景：
class A: pass
class B: pass
class C(A, B): pass

print(issubclass(C, A))  # 输出：True
print(issubclass(C, B))  # 输出：True
print(issubclass(C, (A, B)))  # 输出：True
print(issubclass(A, C))  # 输出：False
## 🔥 第三部分：结合你已学知识 —— Mixin 与多继承中的实战

### 场景：判断一个对象是否“混入”了某个功能

class JsonSerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__, ensure_ascii=False, indent=2)

class LoggableMixin:
    def log(self, msg):
        print(f"[LOG] {msg}")

class Contact:
    def __init__(self, name):
        self.name = name

# 混入两个功能
class SmartContact(Contact, JsonSerializableMixin, LoggableMixin):
    pass

# 创建对象
contact = SmartContact("张三")
# ✅ 检查它是否支持 JSON 序列化
if isinstance(contact, JsonSerializableMixin):
    print(contact.to_json())
# ✅ 检查它是否可日志
if isinstance(contact, LoggableMixin):
    contact.log("已创建")

# ✅ **这就是 Mixin + `isinstance` 的经典配合**：  
# **“如果对象混入了某功能，就启用它”**

# 场景：批量处理对象，只处理特定类型
objects = [
    SmartContact("lisi"),
    Contact("Alice"),
    "hello",
    42,
    Dog()
]
# 只处理能转 JSON 的对象
for obj in objects:
    if isinstance(obj, JsonSerializableMixin):
        print(obj, obj.to_json())
    elif hasattr(obj, "__dict__"):
        # 退而求其次：用 __dict__ 序列化
        print(obj, json.dumps(obj.__dict__))
## ⚠️ 第四部分：常见陷阱与最佳实践

### ❌ 陷阱 1：滥用类型检查，违背“鸭子类型”

# > Python 哲学：**“不关心你是什么类型，只关心你能做什么。”**

# ❌ 不推荐：强行要求 list
def process(items):
    if not isinstance(items, list):
        raise TypeError("必须是 list")
    for item in items: ...

# ✅ 推荐：只要可迭代就行
def process(items):
    try:
        for item in items:
            ...
    except TypeError:
        raise TypeError("对象不可迭代")


# > ✅ **建议**：  
# >
# > - 在**框架、API 入口、序列化等边界处**使用 `isinstance` 做安全检查  
# > - 在**内部逻辑**中优先使用 **EAFP（Easier to Ask for Forgiveness than Permission）** 风格



### ❌ 陷阱 2：试图用 `isinstance` 检查泛型类型（如 `List[int]`）

from typing import List

x = [1, 2, 3]
print(isinstance(x, List[int]))  # ❌ 运行时错误！


# > ✅ **正确做法**：
# >
# > - 用 `isinstance(x, list)` 检查容器类型
# > - 用 `mypy` 等工具做**静态类型检查**
# > - 运行时不检查泛型参数

# ✅ 最佳实践清单

# | 场景                           | 推荐做法                                 |
# | ------------------------------ | ---------------------------------------- |
# | 检查对象是否属于某类（含子类） | ✅ `isinstance(obj, Class)`               |
# | 检查类是否继承自某类           | ✅ `issubclass(cls, Parent)`              |
# | 需要 exact type（极少）        | `type(obj) is Class`                     |
# | 只需要某个方法/属性            | ✅ `hasattr(obj, 'method')` 或 try/except |
# | 框架/插件系统类型过滤          | ✅ `isinstance` + Mixin                   |
# | 日常业务逻辑                   | ❌ 尽量避免，用鸭子类型                   |

# ✅ 总结
# | 函数                      | 用途                               | 关键特性                                 |
# | ------------------------- | ---------------------------------- | ---------------------------------------- |
# | `isinstance(obj, Class)`  | 检查对象是否是某类（或子类）的实例 | ✅ 支持多继承<br>✅ 支持元组<br>✅ 尊重 MRO |
# | `issubclass(cls, Parent)` | 检查类是否继承自某父类             | ✅ 支持间接继承<br>✅ 支持元组             |

# 🎯 **记住**：  
# **它们是“运行时类型安全”的守护者，但不要滥用——Python 更爱“鸭子类型”。**

# 扩展：
# 🦆 一、什么是“鸭子类型”？—— 从名字说起
# **“If it walks like a duck and quacks like a duck, then it’s a duck.”**  
# （如果它走起来像鸭子，叫起来也像鸭子，那它就是鸭子。）
### ✅ 核心思想：
# > **不关心对象“是什么类型”，只关心它“能做什么”。**

# ⚖️ 四、鸭子类型 vs `isinstance()`：何时用谁？
# | 场景                         | 推荐做法                                 | 原因                             |
# | ---------------------------- | ---------------------------------------- | -------------------------------- |
# | **函数内部逻辑**             | ✅ 鸭子类型（直接调用方法）               | 更通用、更灵活、符合 Python 哲学 |
# | **API 入口 / 框架边界**      | ✅ `isinstance` 做安全检查                | 防止恶意输入，提供清晰错误信息   |
# | **需要特定行为（如序列化）** | ✅ Mixin + `isinstance`                   | 显式声明“我支持这个功能”         |
# | **只是需要某个方法**         | ✅ `hasattr(obj, 'method')` 或 try/except | 不关心类型，只关心能力           |

### 🌰 混合使用示例（最佳实践）：

# def save_contact(contact):
#     # 1. 边界检查：确保是 Contact 或其子类（API 安全）
#     if not isinstance(contact, Contact):
#         raise TypeError("必须是 Contact 实例")

#     # 2. 内部逻辑：用鸭子类型处理序列化
#     if hasattr(contact, 'to_json'):  # 不检查 Mixin，只看有没有方法
#         data = contact.to_json()
#     else:
#         data = json.dumps(contact.__dict__)
#     write_to_file(data) 

# > ✅ **既有安全性，又有灵活性！**

## 🌍 五、为什么 Python “更爱”鸭子类型？

### 1. **动态语言的天然优势**

# - 不需要编译时知道类型
# - 运行时“行为”比“身份”更重要

### 2. **鼓励组合而非继承**

# - 你可以让任何对象“表现得像文件”（只要实现 `read()`、`write()`）
# - 不需要继承 `File` 类！

### 3. **协议（Protocol）思想的前身**

# - Python 的“文件对象”、“可迭代对象”、“上下文管理器”都是**协议**，不是类
# - 鸭子类型是这些协议的基础

# > 💡 现代 Python（3.8+）甚至引入了 `typing.Protocol` 来**静态描述鸭子类型**！

# 🧩 七、鸭子类型在标准库中的体现
# | 协议             | 需要实现的方法              | 示例类型                             |
# | ---------------- | --------------------------- | ------------------------------------ |
# | **可迭代**       | `__iter__` 或 `__getitem__` | `list`, `str`, `range`, 自定义类     |
# | **上下文管理器** | `__enter__`, `__exit__`     | `open()`, `threading.Lock`           |
# | **文件类对象**   | `read()`, `write()`         | `io.StringIO`, 网络 socket           |
# | **可调用**       | `__call__`                  | 函数、lambda、实现了 `__call__` 的类 |

# ✅ 所有这些，**都不依赖继承，只依赖方法存在！**

# ✅ 总结：一句话记住鸭子类型
# **“不问你是谁，只看你能不能做这件事。”**
# | 对比项   | 传统类型系统    | 鸭子类型（Python）     |
# | -------- | --------------- | ---------------------- |
# | 关注点   | 类型（Type）    | 行为（Behavior）       |
# | 检查时机 | 编译时 / 强类型 | 运行时 / 动态          |
# | 灵活性   | 低（需继承）    | 高（只需方法）         |
# | 哲学     | “你是鸭子吗？”  | “你能像鸭子一样叫吗？” |
