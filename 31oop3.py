"""
# 第五章：多态（Polymorphism）与抽象
# 第十二步：**多态的概念与实现**
"""

# 🔹 第一部分：什么是多态？—— 核心思想
### 📌 一句话定义：

# > **多态：不同类的对象，对同一个方法调用，表现出不同的行为。**

### 🌰 经典比喻：动物叫声

class Animal:
    def speak(self):
        pass
class Cat(Animal):
    def speak(self):
        print("喵喵叫！")
class Dog(Animal):
    def speak(self):
        print("汪汪叫！")
class Duck(Animal):
    def speak(self):
        print("嘎嘎叫！")

# 现在，我们可以**统一处理所有动物**：
animals = [Dog(), Cat(), Duck()]
for animal in animals:
    print(animal.speak())  # ← 同一个方法调用，不同行为！

# ✅ 这就是**多态的力量**：  
# 代码不关心具体类型，只调用统一接口，行为由对象自身决定。


# 🔹 第二部分：Python 中多态的两种实现方式
# 方式 1️⃣：**继承 + 方法重写（经典 OOP 多态）
# - 父类定义**接口（方法名）**
# - 子类**重写（override）** 实现具体逻辑
# - 通过**统一父类引用**调用

# ✅ 优点：结构清晰，适合强约束场景  
# ✅ 缺点：必须继承同一个父类

# 上面的 Animal 示例就是这种方式

# 方式 2️⃣：**鸭子类型（Duck Typing）—— Python 特色多态**
# **不需要共同父类！只要方法名相同，就能多态调用。**
class Dog:
    def speak(self):
        return "汪汪叫"

class Robot:
    def speak(self):
        return "bibi,我是机器人"
class Human:
    def speak(self):
        return "你好"
# 完全无关的类
things =[Dog(), Robot(), Human()]
for thing in things:
    print(thing.speak())  # ← 依然多态！鸭子类型的多态
    print(type(thing)) 
# ✅ **这就是 Python 的“协议多态”**：  
# **只要实现了 `speak()` 方法，就能被当作“可说话的对象”使用。**

# 🔥 第三部分：抽象基类（ABC）—— 强制多态接口
# 鸭子类型很灵活，但**缺乏约束**：如果某个类忘了实现 `speak()`，运行时才报错。

# **抽象基类（Abstract Base Class, ABC）** 解决这个问题！

### ✅ 作用：

# - 定义**必须实现的接口**
# - **禁止直接实例化抽象类**
# - 子类**必须实现所有抽象方法**，否则报错

# 🌰 示例：用 ABC 强制多态
from abc import ABC, abstractmethod
class Speaker(ABC):  # 抽象基类
    @abstractmethod
    def speak(self):
        pass
class Dog(Speaker):
    def speak(self):
        return "汪汪叫"
class Cat(Speaker):
    pass # ← 忘了实现 speak() → 运行时会报错！

try:
    cat = Cat()
except TypeError as e:
    print(e) # Can't instantiate abstract class Cat without an implementation for abstract method 'speak'
# ✅ **ABC 让鸭子类型有了“契约”**：  
# “你想当 Speaker？必须实现 `speak()`！”

## 🔹 第四部分：多态 + Mixin + ABC 实战：可扩展通知系统
### 场景：发送通知（邮件、短信、微信），统一接口

from abc import ABC, abstractmethod
# 1.定义抽象通知接口
class Notifier(ABC):
    @abstractmethod
    def send(self, msg: str) -> bool:
        pass
# 2.定义具体的通知实现
class EmailNotifier(Notifier):
    def send(self, msg):
        print(f"发送邮件通知：{msg}")
        return True
    
class SMSNotifier(Notifier):
    def send(self, msg):
        print(f"发送短信通知：{msg}")
        return True
class WechatNotifier(Notifier):
    def send(self, msg):
        print(f"发送微信通知：{msg}")
        return True
# 3.用户类，接收通知器列表
class User:
    def __init__(self, name: str, notifiers: list[Notifier]) -> None: # 初始化的时候要传入通知器列表
        self.name = name 
        for notifier in notifiers:
            if not isinstance(notifier, Notifier):
                raise TypeError("通知器必须实现 Notifier 接口")
        self.notifiers = notifiers

    def notify(self, msg: str):
        for notifier in self.notifiers:
            notifier.send(f"[{self.name}] {msg}")
# 4.使用
user = User("lisi", [
    SMSNotifier(),
    EmailNotifier()
])
user.notify("您的订单已发货，请注意查收")

# **输出**：
# 发送短信通知：[lisi] 您的订单已发货，请注意查收
# 发送邮件通知：[lisi] 您的订单已发货，请注意查收

# ✅ **优势**：
# - 新增通知方式？只需实现 `Notifier` 接口
# - `User` 完全不需要修改！
# - **开闭原则（对扩展开放，对修改关闭）完美体现**

# ⚠️ 第五部分：多态 vs 鸭子类型 vs 类型检查 —— 如何选择？
# | 需求                           | 推荐方案                                   |
# | ------------------------------ | ------------------------------------------ |
# | **强约束、团队协作、框架开发** | ✅ ABC + `isinstance`                       |
# | **快速原型、脚本、灵活扩展**   | ✅ 鸭子类型（直接调用方法）                 |
# | **需要运行时安全网**           | ✅ `isinstance(obj, Protocol)` 或 `hasattr` |
# | **静态类型检查（mypy）**       | ✅ `typing.Protocol`（下一章可学）          |

# 🧠 第六部分：多态的哲学意义
# **多态的本质，是“解耦”**。
# - 调用方 **不依赖具体实现**
# - 实现方 **自由替换、扩展**
# - 系统 **更易维护、测试、扩展**

# 这正是：
# - 插件系统的基础
# - 依赖注入（DI）的核心
# - 设计模式（策略模式、工厂模式）的根基

# 🧪 完整对比：三种多态风格
# 1. 继承多态
class Animal:
    def speak(self): raise NotImplementedError
class Dog(Animal):
    def speak(self): return "汪"

# 2. 鸭子类型多态
class Robot:
    def speak(self): return "哔哔"

# 3. ABC 强制多态
from abc import ABC, abstractmethod
class Speaker(ABC):
    @abstractmethod
    def speak(self): pass
class Human(Speaker):
    def speak(self): return "你好"

# 统一调用
objects = [Dog(), Robot(), Human()]
for obj in objects:
    print(obj.speak())  # 全部成功！

# ✅ Python 允许你**混合使用**这三种风格！
# ✅ 总结：多态的核心要点
# | 概念                | 说明                                                         |
# | ------------------- | ------------------------------------------------------------ |
# | **多态**            | 同一接口，不同实现                                           |
# | **继承多态**        | 通过父类/子类实现                                            |
# | **鸭子类型多态**    | 通过方法名匹配实现（Python 特色）                            |
# | **抽象基类（ABC）** | 为鸭子类型加上“契约”，防止遗漏实现                           |
# | **最佳实践**        | 用 ABC 定义接口，用鸭子类型保持灵活，用 `isinstance` 做边界检查 |

'''
# 第十三步：抽象基类（ABC）

- `abc` 模块的使用
- `@abstractmethod` 装饰器
- 强制子类实现特定方法
'''
# 🔹 第一部分：为什么需要抽象基类？—— 问题驱动
### 🌰 场景：定义一个“可序列化”接口

class Serializable:
    def to_json(self):
        pass  # 空实现？危险！

class User(Serializable):
    def __init__(self, name):
        self.name = name
    # 忘记重写 to_json()！

user = User("张三")
print(user.to_json())  # 输出: None ← 静默失败！灾难！

# > ❌ **问题**：  
# >
# > - 父类方法是空的，子类可能忘记实现  
# > - 错误在**运行时才暴露**，难以调试

### ✅ 解决方案：用 **抽象基类** 强制实现！

# 🔹 第二部分：`abc` 模块核心组件
# Python 的 `abc` 模块提供三个关键工具：
# | 组件              | 作用                         |
# | ----------------- | ---------------------------- |
# | `ABC`             | 抽象基类的基类（推荐继承它） |
# | `@abstractmethod` | 标记抽象方法（子类必须实现） |
# | `ABCMeta`         | 元类（底层，一般不用直接用） |

# ✅ **推荐写法**：继承 `ABC` + 用 `@abstractmethod`
# 🔹 第三部分：基础语法与示例
# ✅ 步骤 1：定义抽象基类
from abc import ABC, abstractmethod
class Drawable(ABC): # 继承 ABC
    @abstractmethod
    def draw(self):
        pass # 抽象方法，无需实现
    # 也可以有具体方法
    def show(self):
        print("正在显示图形...")
        self.draw() # 调用抽象方法
# ✅ 步骤 2：子类必须实现所有抽象方法

class Circle(Drawable):
    def draw(self): # ✅ 正确：实现了 draw()
        print("画一个圆形...")
c = Circle()
c.show()

# ❌ 步骤 3：如果子类未实现抽象方法？
class Square(Drawable):
    pass  # 忘记实现 draw() 
try:
    s = Square() # 尝试实例化
    # s.show()
except TypeError as e:
    print(e)
#Can't instantiate abstract class Square without an implementation for abstract method 'draw'
# ✅ **错误在实例化时立即抛出**，而不是等到调用方法时！  
# **这就是 ABC 的核心价值：提前暴露设计错误。**
# 🔹 第四部分：高级用法
# 1️⃣ 抽象属性（`@property` + `@abstractmethod`）
# 子类实现抽象方法后，可以使用 `@property` 装饰器来定义抽象属性，子类.属性会自动调用抽象方法

from abc import ABC, abstractmethod
class Shape(ABC):
    @property
    @abstractmethod
    def area(self): pass
class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height
r = Rectangle(3, 5)
print(r.area)  # 输出：15

# ⚠️ 注意顺序：**`@property` 在 `@abstractmethod` 上面**

# 2️⃣ 抽象类方法（`@classmethod` + `@abstractmethod`）
class Database(ABC):
    @classmethod
    @abstractmethod
    def connect(cls): pass
class MysqlDB(Database):
    @classmethod
    def connect(cls):
        print("连接 MySQL 数据库...")
MysqlDB.connect()  # 输出：连接 MySQL 数据库...

# 3️⃣ 抽象静态方法（较少用）
class MathUtil(ABC):
    @staticmethod
    @abstractmethod
    def add(a, b): pass

# 🔥 第五部分：ABC + `isinstance()` = 安全多态
# 场景：只处理实现了特定协议的对象
from abc import ABC, abstractmethod
class JsonSerializable(ABC):
    @abstractmethod
    def to_json(self): pass
class User(JsonSerializable):
    def __init__(self, name: str):
        self.name = name
    def to_json(self):
        return f'{{"name":{self.name!r}}}'
    
class Product:  # 没有实现JsonSerializable
    def __init__(self, title):
        self.title =title   
# 安全处理
objects = [
    User("小明"),
    Product("笔记本"),
    "hello"
]

for obj in objects:
    if isinstance(obj, JsonSerializable):
        print(obj.to_json())
    else:
        # print(f"跳过：{obj.__class__.__name__}")
        print(f"跳过：{type(obj).__name__}")
# **输出**：
# {"name":'小明'}
# 跳过：Product
# 跳过：str

# ✅ **`isinstance(obj, JsonSerializable)` 会返回 True，只要 obj 的类继承了该 ABC 并实现了所有抽象方法！**
# ⚠️ 第六部分：常见误区与最佳实践
# ❌ 误区 1：以为 ABC 是“接口”，不能有具体方法
# ✅ **错误！** ABC 可以有具体方法（如模板方法模式）
class Game(ABC):
    def play(self):  # 具体方法（模板）
        self.initialize()
        self.start_play()
        self.end_play()

    @abstractmethod
    def initialize(self): pass
    @abstractmethod
    def start_play(self): pass
    @abstractmethod
    def end_play(self): pass

# ❌ 误区 2：滥用 ABC，过度设计
# ✅ **建议**：  

# - 只在**需要强制契约**时使用 ABC（如框架、库、团队协作）  
# - 内部脚本、简单逻辑用**鸭子类型**更 Pythonic

# ✅ 最佳实践清单
# | 场景                         | 建议                                    |
# | ---------------------------- | --------------------------------------- |
# | 定义公共接口（如插件、回调） | ✅ 使用 ABC                              |
# | 需要运行时类型检查           | ✅ `isinstance(obj, MyABC)`              |
# | 只需方法存在（不强制）       | ❌ 用鸭子类型（`hasattr` 或 try/except） |
# | 性能敏感代码                 | ⚠️ ABC 有轻微开销，但通常可忽略          |
# | 与 `typing.Protocol` 对比    | ✅ ABC 用于运行时，Protocol 用于静态检查 |

# 🧪 完整实战：可扩展的日志处理器系统
from abc import ABC, abstractmethod
import json
class LogHandler(ABC):
    @abstractmethod
    def write(self, msg): pass

class FileLogHandler(LogHandler):
    def __init__(self, filename):
        self.filename = filename
    def write(self, msg):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
class ConsoleLogHandler(LogHandler):
    def write(self, msg):
        print(f"[CONSOLE] {msg}")

class JSONLogHandler(LogHandler):
    def write(self, msg):
        print(json.dumps({"message": msg}, ensure_ascii=False, indent=2))

class Logger:
    def __init__(self, handlers: list[LogHandler]):
        # 安全检查，确保都是 LogHandler 的子类
        for handler in handlers:
            if not isinstance(handler, LogHandler):
                raise TypeError("处理器必须继承 LogHandler")
            self.handlers = handlers
    def log(self, msg):
        for handler in self.handlers:
            handler.write(msg)

log = Logger([
    FileLogHandler("hello.txt"),
    JSONLogHandler(),
    ConsoleLogHandler()
])
log.log("Hello, world！你好世界！")

# ✅ **优势**：

# - 新增日志方式？只需继承 `LogHandler`
# - `Logger` 完全无需修改
# - **开闭原则 + 多态 + ABC 完美结合**

# 🔗 第七部分：ABC vs 其他概念对比
# | 特性             | 普通基类 | Mixin    | ABC                            |
# | ---------------- | -------- | -------- | ------------------------------ |
# | 可实例化         | ✅        | ✅        | ❌（有抽象方法时）              |
# | 强制子类实现方法 | ❌        | ❌        | ✅                              |
# | 主要目的         | 代码复用 | 功能组合 | 接口契约                       |
# | 是否必须继承     | 否       | 否       | 是（才能通过 isinstance 检查） |

# ✅ 总结：ABC 的核心价值
# > **ABC 不是为了限制你，而是为了保护你和你的用户。**

# - ✅ **提前捕获设计错误**（实例化时报错，而非调用时报错）  
# - ✅ **明确接口契约**（文档 + 代码双重约束）  
# - ✅ **支持安全的多态**（`isinstance` 可靠检查）  
# - ✅ **构建可扩展系统**（插件、策略、处理器模式的基础）