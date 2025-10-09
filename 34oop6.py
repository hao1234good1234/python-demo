"""
# 第八章：设计原则与最佳实践

# 第十九步：**SOLID 原则简介**
"""

## 🎯 本章目标：掌握 **SOLID 原则**，写出**高内聚、低耦合、易维护、可扩展**的 Python 代码

# > 💡 **SOLID** 是 5 个面向对象设计原则的首字母缩写，由“设计模式之父”Robert C. Martin（Bob 大叔）提出。  
# > 它们不是规则，而是**指导思想**——帮你避免“代码越改越烂”的陷阱。

# 📚 SOLID 五原则速览
# | 缩写  | 中文名              | 核心思想                     |
# | ----- | ------------------- | ---------------------------- |
# | **S** | 单一职责原则（SRP） | 一个类只干一件事             |
# | **O** | 开闭原则（OCP）     | 对扩展开放，对修改关闭       |
# | **L** | 里氏替换原则（LSP） | 子类必须能替换父类           |
# | **I** | 接口隔离原则（ISP） | 客户端不应依赖它不需要的接口 |
# | **D** | 依赖倒置原则（DIP） | 依赖抽象，而非具体实现       |

## 🔹 1. S — 单一职责原则（Single Responsibility Principle）

# > **“一个类应该只有一个引起它变化的原因。”**
# ✅ 正例：拆分成三个类
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
 # 1. 数据持久化
class UserRepository:
    def save(self, user: User):
        print(f"saving {user.name} to DB")
# 2. 发送邮件
class EmailService:
    def send(self, user: User, msg: str):
        print(f"emailing {user.name} :{msg}")
# 3. 生成报表
class ReportGenerator:
    def generate(self, user: User) -> str:
        return f"Report for {user.name}"
# **好处**：  

# - 修改数据库逻辑？只动 `UserRepository`  
# - 换邮件服务商？只改 `EmailService`  
# - **高内聚，低耦合！**

# > ✅ **SRP 的本质：关注点分离（Separation of Concerns）**

## 🔹 2. O — 开闭原则（Open/Closed Principle）

# > **“软件实体（类、模块、函数）应该对扩展开放，对修改关闭。”**

# ✅ 正例：用多态 + 抽象基类
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: pass
# 圆形
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self) -> float:
        return 3.14 * self.radius ** 2
# 矩形
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
# 三角形
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
# 计算面积
class AreaCalculator:
    def calculate_area(self, shape: Shape) -> float:
        return shape.area() # 多态调用 ✅
# **好处**：  

# - 要支持新形状？**只新增类，不修改现有代码**  
# - 符合 **OCP**：对扩展开放（加新类），对修改关闭（不动 `AreaCalculator`）

# > ✅ **OCP 的实现手段：抽象 + 多态 + 依赖注入**

## 🔹 3. L — 里氏替换原则（Liskov Substitution Principle）

# > **“子类对象必须能够替换父类对象，而不破坏程序正确性。”**
# ✅ 正例：重新设计继承关系
# 鸟 父类
class Bird: pass
# 飞鸟 子类
class FlyBird(Bird):
    def fly(self):
        print("flying...")
# 鸵鸟
class Ostrich(Bird):
    def run(self):
        print("running...")
# 麻雀
class Sparrow(FlyBird):
    pass
# 明确要求会飞的鸟
def make_bird_fly(bird: FlyBird):
    bird.fly()
# ✅ **LSP 的核心：子类必须遵守父类的“契约”（行为约定）**

## 🔹 4. I — 接口隔离原则（Interface Segregation Principle）

# > **“客户端不应该被迫依赖它不使用的方法。”**
# ✅ 正例：拆分成小接口
# 老打印机不能扫描！
# 也不能传真！
# ✅ 正例：拆分成小接口
from abc import ABC, abstractmethod
# 打印接口
class Printer(ABC):
    @abstractmethod
    def print(self, doc): pass

# 扫描接口
class Scanner(ABC):
    @abstractmethod
    def scan(self, doc): pass

# 传真接口
class Fax(ABC):
    @abstractmethod
    def fax(self, doc): pass

# 老打印机只实现 Printer
class OldPrinter(Printer):
    def print(self, doc):
        print("printing", doc)
# 多功能打印机实现多个接口
class ModernPrinter(Printer, Scanner, Fax):
    def print(self, doc):
        print("printing", doc)
    def scan(self, doc):
        print("scanning", doc)
    def fax(self, doc):
        print("faxing", doc)
# ✅ **ISP 的本质：小而专注的接口，按需组合**

## 🔹 5. D — 依赖倒置原则（Dependency Inversion Principle）

# > **“高层模块不应该依赖低层模块，两者都应该依赖抽象。  
# > 抽象不应该依赖细节，细节应该依赖抽象。”**

# ✅ 正例：依赖抽象（接口）
from abc import ABC, abstractmethod
# 可以开关控制的设备
class Switchable(ABC):
    @abstractmethod
    def turn_on(self): pass
    @abstractmethod
    def turn_off(self): pass

# 电灯泡
class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb on")
    def turn_off(self):
        print("LightBulb off")
# 风扇
class Fan(Switchable):
    def turn_on(self):
        print("Fan on")
    def turn_off(self):
        print("Fan off")
# 开关
class Switch:
    def __init__(self, device: Switchable): # 依赖抽象 ✅
        self.device = device

    def operate(self):
        self.device.turn_on()
# 现在 Switch 可以控制任何 Switchable 设备！
switch1 = Switch(LightBulb())
switch1.operate()
switch2 = Switch(Fan())
switch2.operate()

# ✅ **DIP 的实现：依赖注入（Dependency Injection） + 抽象基类**
# 🧩 SOLID 在 Python 中的特别说明
# | 原则    | Python 特点                                               |
# | ------- | --------------------------------------------------------- |
# | **SRP** | 用模块/函数拆分也很有效（不一定要类）                     |
# | **OCP** | Python 的鸭子类型让“接口”更灵活，但仍需抽象               |
# | **LSP** | Python 无强制类型检查，更需靠文档和测试保证               |
# | **ISP** | Python 没有 interface 关键字，用 `ABC` 或协议（Protocol） |
# | **DIP** | 依赖注入在 Python 中非常自然（函数参数即可）              |


# ✅ 总结：SOLID 不是教条，而是思维工具
# | 原则    | 问自己                                     |
# | ------- | ------------------------------------------ |
# | **SRP** | “这个类/函数会不会因为多个原因被修改？”    |
# | **OCP** | “加新功能时，我需要改现有代码吗？”         |
# | **LSP** | “子类能无缝替换父类吗？行为一致吗？”       |
# | **ISP** | “客户端是否被迫实现不需要的方法？”         |
# | **DIP** | “我的代码是否依赖了具体实现，而不是抽象？” |


# 💡 **记住：SOLID 的目标是——让代码更容易**  
# - **理解**（清晰职责）  
# - **测试**（独立模块）  
# - **扩展**（不改旧代码）  
# - **维护**（局部修改）
'''
第二十步：**组合 vs 继承**
'''
# 很多初学者一学 OOP 就疯狂用继承，结果代码变得**脆弱、难以维护、难以测试**。而高手往往说：

# > **“优先使用组合，而不是继承。

## 🔮 一、先看例子：同一个需求，两种实现

### 需求：实现一个“带飞行能力的鸭子”

### ❌ 方案1：用继承（看似自然，实则危险）

class Duck:
    def quack(self):
        print("Quack!")

    def fly(self):
        print("Flying with wings!")

class ToyDuck(Duck):  # 玩具鸭
    def fly(self):
        # 玩具鸭不能飞！但必须重写 fly()
        raise NotImplementedError("Toy duck can't fly!")

# **问题来了**：

# def make_duck_fly(duck: Duck):
#     duck.fly()  # 如果传入 ToyDuck，崩溃！❌

# make_duck_fly(ToyDuck())  # 抛异常！

# > 💥 **这就是“脆弱基类问题” + 违反 LSP（里氏替换原则）**

# ✅ 方案2：用组合（灵活解耦）
from abc import ABC, abstractmethod
# 定义“飞行行为”接口
class FlyBehavior(ABC):
    @abstractmethod
    def fly(self): pass
# 用翅膀飞
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Flying with wings!")
# 不会飞
class CanNotFly(FlyBehavior):
    def fly(self):
        print("Can't fly!")
# 鸭子类“拥有”一个飞行行为（组合）
class Duck:
    def __init__(self, fly_behavior: FlyBehavior):
        self.fly_behavior = fly_behavior  # ← 组合！
    def quack(self):
        print("Quack!")
    def fly(self):
        self.fly_behavior.fly() # 委托给行为对象

# 使用
real_duck = Duck(FlyWithWings())
toy_duck = Duck(CanNotFly())
real_duck.fly()  # Flying with wings!
toy_duck.fly()  # Can't fly!

# ✅ **优势**：

# - 行为可动态切换：`duck.fly_behavior = FlyWithRocket()`
# - 新增行为不用改 `Duck` 类
# - 完全符合 **开闭原则（OCP）**
# - 没有“被迫实现不需要的方法”

# > 🌟 这就是著名的 **“策略模式（Strategy Pattern）”** —— 用组合实现行为解耦。
# 🔍 二、本质区别：**“is-a” vs “has-a”**
# | 关系                    | 含义                                | 适用场景                              | 示例                |
# | ----------------------- | ----------------------------------- | ------------------------------------- | ------------------- |
# | **继承（Inheritance）** | “A **is a** B”<br>（A 是一种 B）    | 表达**类型层次**，共享**公共接口**    | `Dog is a Animal`   |
# | **组合（Composition）** | “A **has a** B”<br>（A 拥有一个 B） | 表达**部分-整体**关系，或**行为委托** | `Car has an Engine` |

### ✅ 正确使用继承的例子：

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):      # Dog is an Animal ✅
    def make_sound(self):
        return "Woof!"

class Cat(Animal):      # Cat is an Animal ✅
    def make_sound(self):
        return "Meow!"

# 这里 `Dog` **确实是**一种 `Animal`，且必须实现 `make_sound`，**符合 LSP**。
## ⚠️ 三、继承的四大陷阱（为什么慎用？）

### 1. **脆弱基类问题（Fragile Base Class）**

# - 修改父类 → 所有子类可能崩溃
# - 子类依赖父类的**实现细节**，而非接口

### 2. **紧耦合（Tight Coupling）**

# - 子类与父类**强绑定**，难以单独测试或替换

### 3. **多重继承的复杂性（Python 有 MRO，但仍危险）**

# - 菱形继承、方法解析顺序混乱

### 4. **违反单一职责（SRP）**

# - 父类承担太多职责，子类被迫继承不需要的功能

# > 💡 **继承 = 白盒复用（暴露内部）**  
# > **组合 = 黑盒复用（只依赖接口）**

# ✅ 四、组合的三大优势
# | 优势           | 说明                                             |
# | -------------- | ------------------------------------------------ |
# | **灵活性**     | 运行时动态更换组件（如换数据库、换日志器）       |
# | **可测试性**   | 可轻松 mock 依赖（如用 `MockEmailService` 测试） |
# | **符合 SOLID** | 尤其 OCP（开闭）、DIP（依赖倒置）                |

# 🌰 组合实战：可插拔的日志系统
# 文件日志
class FileLogger:
    def log(self, msg):
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(msg + "\n")

# 控制台日志
class ConsoleLogger:
    def log(self, msg):
        print(f"[CONSOLE] {msg}")
# 邮件日式
class EmailLogger:
    def log(self, msg):
        # 发邮件
        print(f"[EMAIL] {msg}")
        pass
# 用户服务
class UserService:
    def __init__(self, logger): # 依赖注入（组合） # ← 显式传入依赖 
        self.logger = logger
    def create_user(self, name):
        self.logger.log(f"创建用户：{name}")
# 使用
service1 = UserService(FileLogger())
service2 = UserService(ConsoleLogger())  # 不用改 UserService！
service3 = UserService(EmailLogger())

service2.create_user("Alice")
service3.create_user("Bob")

## 🧭 五、决策指南：何时用继承？何时用组合？

# ### ✅ **优先用组合，除非满足以下所有条件**：
# | 条件                            | 说明                         |
# | ------------------------------- | ---------------------------- |
# | ✅ **“is-a” 关系非常明确**       | 如 `Rectangle is a Shape`    |
# | ✅ **子类能完全替代父类（LSP）** | 不会抛 `NotImplementedError` |
# | ✅ **需要多态行为**              | 通过统一接口调用不同实现     |
# | ✅ **不会频繁修改父类**          | 避免脆弱基类问题             |

# ❌ **不要用继承的情况**：
# | 场景                                     | 正确做法                         |
# | ---------------------------------------- | -------------------------------- |
# | 只是为了复用代码                         | → 用**工具函数**或**组合**       |
# | 子类“不是”父类（如 `Stack is a Vector`） | → 用**组合**（Stack has a list） |
# | 行为需要动态变化                         | → 用**策略模式（组合）**         |
# | 多个维度变化（如鸭子 + 飞行 + 叫声）     | → 用**组合 + 多个行为类**        |

# 📌 经验法则：  

# 如果你写 class A(B) 时，心里想的是“为了复用 B 的代码”，那就错了！  

# 正确想法应该是：“A 在类型上就是 B 的一种”。

# 🔧 六、Python 特色：鸭子类型让组合更自然
# Python 不强制继承，**只要对象有 `.fly()` 方法，就能飞**！
class Rocket:
    def fly(self):
        print(f"Flying with a rocket!")
class Bird:
    def fly(self):
        print(f"Flying with wings!")
def launch(thing_that_files):
    thing_that_files.fly() # 不关心类型，只关心行为 ✅

launch(Rocket()) 
launch(Bird()) # —— 这就是“鸭子类型”
# ✅ **组合 + 鸭子类型 = Python 最优雅的设计方式**
# ✅ 七、总结：一张表看懂
# | 特性           | 继承               | 组合               |
# | -------------- | ------------------ | ------------------ |
# | **关系**       | is-a               | has-a              |
# | **耦合度**     | 高（紧耦合）       | 低（松耦合）       |
# | **灵活性**     | 低（编译时确定）   | 高（运行时可换）   |
# | **复用方式**   | 白盒（看内部）     | 黑盒（看接口）     |
# | **适用场景**   | 类型层次、多态接口 | 行为委托、功能组装 |
# | **SOLID 支持** | 易违反 LSP/SRP     | 天然支持 OCP/DIP   |
# 💡 **记住这句话**：  
# **“继承表达‘是什么’，组合表达‘有什么’。”**

# 扩展：
# 鸭子类型和组合的区别：

# 🎯 核心区别：**“是否有明确的‘角色契约’？”**
# | 维度         | 可插拔日志系统（组合）               | 鸭子类型示例                               |
# | ------------ | ------------------------------------ | ------------------------------------------ |
# | **设计目标** | **替换实现**（同一个角色的不同实现） | **复用行为**（不同对象碰巧有相同方法）     |
# | **角色抽象** | ✅ 有隐含/显式的“Logger”角色          | ❌ 没有“Flyable”角色，只是碰巧都有 `.fly()` |
# | **依赖关系** | `UserService` **依赖一个日志组件**   | `launch` **不依赖任何类型，只依赖行为**    |
# | **可测试性** | 极高（可注入 `MockLogger`）          | 一般（靠约定，无类型检查）                 |
# | **扩展方式** | 实现“Logger 接口”即可                | 只要定义 `.fly()` 就行                     |

# 🧩 关键洞察：**“组合”强调‘角色’，‘鸭子类型’强调‘行为’**
### ✅ 组合 = “我需要一个**扮演特定角色**的对象”

# - `UserService` 说：“我需要一个 **Logger**，它必须能 `.log()`。”
# - 这个“Logger”是一个**设计角色**，哪怕 Python 没写 `class Logger(ABC)`，**语义上它存在**。
# - 你可以（也应该）用 `Protocol` 或 `ABC` 明确这个角色：

from typing import Protocol

class Logger(Protocol):
    def log(self, msg: str) -> None: ...

class UserService:
    def __init__(self, logger: Logger):  # ← 明确契约
        self.logger = logger

# > ✅ 这就是 **“组合 + 协议”** —— 既灵活又安全。
### 🦆 鸭子类型 = “我不关心你是谁，只要你能做这件事”

# - `launch` 说：“我不在乎你是什么，**只要你能 `.fly()`，我就用你**。”
# - 没有“飞行器”这个角色，`Rocket` 和 `Bird` **本质完全不同**，只是**偶然行为重合**。
# - 这是一种**弱约定**，适合快速脚本、小型项目。

# > ❗ 但如果 `Car` 也有 `.fly()`（比如飞行汽车），也能传进去——**这是特性，也是风险**。

## 🧪 对比实验：如果出错了，谁更容易发现？

### 场景：有人不小心把 `logger` 写错了

#### 情况1：组合 + Protocol（推荐）

class BadLogger:
    def write_log(self, msg):  # ❌ 方法名错了！
        print(msg)

service = UserService(BadLogger())  # ← 类型检查器（如 mypy）会报错！

# ✅ **静态检查就能发现问题**

#### 情况2：纯鸭子类型

class BrokenThing:
    def glide(self):  # ❌ 没有 .fly()
        pass

# launch(BrokenThing())  # ← 运行时才报错：AttributeError: 'BrokenThing' object has no attribute 'fly'

# ❌ **只有运行到那一行才崩溃**

## ✅ 总结：一句话分清

# > **组合** 是：**“我需要一个符合 XXX 角色的对象”**（强调职责）  
# > **鸭子类型** 是：**“我不关心你是什么，只要你会做 YYY”**（强调行为）

# |              | 组合                            | 鸭子类型                         |
# | ------------ | ------------------------------- | -------------------------------- |
# | **关注点**   | 对象的**角色/职责**             | 对象的**行为/方法**              |
# | **设计意图** | **替换实现**（策略、插件）      | **复用行为**（偶然共性）         |
# | **推荐用法** | 用 `Protocol` 或 `ABC` 明确角色 | 用于简单脚本或行为高度一致的场景 |

# 💡 最佳实践建议（Python 现代写法）
from typing import Protocol

# 1. 用 Protocol 定义“角色”（组合的契约）
class Notifier(Protocol):
    def send(self, msg: str) -> None: ...

# 2. 实现不同策略
class EmailNotifier:
    def send(self, msg: str) -> None:
        print(f"Email: {msg}")

class SMSNotifier:
    def send(self, msg: str) -> None:
        print(f"SMS: {msg}")

# 3. 使用组合（依赖角色，而非具体类）
class OrderService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def confirm_order(self):
        self.notifier.send("Order confirmed!")
# ✅ 这样既保留了**组合的灵活性**，又通过 `Protocol` 获得了**类型安全**和**文档清晰性**。


# 扩展：
# 🔧  二、传统方案：用 `ABC`（抽象基类）定义“名义子类型” > 💥 **名义子类型（Nominal Subtyping）**：必须“声明我是你儿子”，才能算数。
# - **必须显式继承 `Animal`**！
# - 如果有一个第三方类 `RobotDuck`，它有 `.quack()`，但**没继承 `Animal`**，就不能用！

# ✨ 三、`Protocol` 的诞生：结构化子类型（Structural Subtyping）
# “只要你有 `.quack()` 方法，你就是 `Animal`！”
from typing import Protocol
class Quackable(Protocol):
    def quack(self) -> None: ...
# 这两个类都没继承 Quackable！
class Duck:
    def quack(self):
        print("Quack!")
class RobotDuck:
    def quack(self):
        print("Beep quack!")
def make_sound(animal: Quackable): # ← 类型提示，但不要求继承
    animal.quack()

make_sound(Duck())        # ✅ OK
make_sound(RobotDuck())   # ✅ OK —— mypy 也通过！
### ✅ 关键点：

# - `Quackable` 是一个 **协议（Protocol）**，不是基类
# - **任何类，只要结构（方法签名）匹配，就自动符合协议**
# - **无需显式继承**！
# - **类型检查器（如 mypy, PyCharm）能正确识别**

# > 🌟 这就是 **“鸭子类型 + 静态类型检查” 的终极融合！**

## 🔍 四、`Protocol` vs `ABC` 对比

# | 特性             | `Protocol`                     | `ABC`                        |
# | ---------------- | ------------------------------ | ---------------------------- |
# | **子类型判断**   | 结构化（看方法）               | 名义化（看继承）             |
# | **是否需要继承** | ❌ 不需要                       | ✅ 必须                       |
# | **运行时开销**   | 几乎为零（纯类型提示）         | 有（`isinstance` 检查）      |
# | **适用场景**     | 组合、行为契约、第三方类适配   | 明确的类型层次、强制接口实现 |
# | **Python 版本**  | 3.8+（或 `typing_extensions`） | 2.6+                         |

### 📌 简单记：

# - **用 `Protocol` 表达“行为契约”**（如 `Logger`, `Notifier`）
# - **用 `ABC` 表达“类型家族”**（如 `Shape`, `Animal`）

# 🧪 五、`Protocol` 实战：让组合设计更安全
# 回到你的日志系统例子：
from typing import Protocol
class Logger(Protocol):
    def log(self, msg: str) -> None: ...
class ConsoleLogger:
    def log(self, msg: str) -> None:
        print(f"[CONSOLE] {msg}")
class FileLogger:
    def log(self, msg: str) -> None:
        print(f"[FILE] {msg}")
# 第三方库的类，没听过Logger协议，但是有log方法
class ThirdPartyLogger:
    def log(self, message: str) -> None: # 注意：参数名不同，但签名兼容
        print(f"[THIRD-PARTY] {message}")
class UserService:
    def __init__(self, logger: Logger):  # ← 类型安全！
        self.logger = logger
    def create_user(self, name):
        self.logger.log(f"创建用户：{name}")
# 全部都能用
UserService(ConsoleLogger()).create_user("Alice")
UserService(FileLogger()).create_user("Bob")
UserService(ThirdPartyLogger()).create_user("Charlie")  # ✅ mypy 也认可！
# ✅ **这就是“组合 + Protocol” 的威力：灵活 + 安全 + 兼容第三方**
## ⚙️ 六、高级用法

### 1. **带属性的 Protocol**

class Readable(Protocol):
    name: str          # 必须有 name 属性
    def read(self) -> str: ...

### 2. **泛型 Protocol**

from typing import TypeVar, Protocol

T = TypeVar('T')

class Comparable(Protocol[T]):
    def __lt__(self, other: T) -> bool: ...

def sort_items(items: list[Comparable[T]]) -> list[T]:
    return sorted(items)

### 3. **运行时检查（谨慎使用）**

from typing import runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...

# if isinstance(obj, Drawable):  # ← 只有加了 @runtime_checkable 才能用
#     obj.draw()

# > ⚠️ 注意：`isinstance` 检查有性能开销，**一般只用于调试或插件系统**


# ✅ 七、总结：为什么 `Protocol` 是现代 Python 的必备技能？
# | 问题                 | `Protocol` 的解决方案          |
# | -------------------- | ------------------------------ |
# | 鸭子类型无法类型检查 | ✅ 提供结构化类型提示           |
# | 组合设计缺乏契约     | ✅ 用 Protocol 明确“角色接口”   |
# | 第三方类无法适配     | ✅ 无需修改源码，自动兼容       |
# | 继承导致紧耦合       | ✅ 用组合 + Protocol 实现松耦合 |
# 💡 **记住**：  
# **`Protocol` 不是类，不是接口，而是一个“行为契约”的声明。**  
# **它让 Python 的灵活性和类型安全性终于握手言和。**



'''
# 第二十一步：**OOP 代码组织与模块化**
'''

# - 类的拆分与协作
# - 包与模块中的类设计

# 太棒了！你已经从 **SOLID 原则 → 组合 vs 继承 → Protocol 类型契约**，一路进阶到了 **大型项目代码组织** 的核心问题：

# > **“如何把一堆类，组织成清晰、可维护、可扩展的系统？”**

# 这是区分“写脚本的人”和“构建系统的人”的关键一步！


# ## 🎯 本章目标：掌握 **Python 中面向对象项目的模块化设计**

# 学完本章，你将能：

# - ✅ 合理拆分类与模块，避免“上帝类”和“面条代码”
# - ✅ 设计清晰的 **包（package）结构**
# - ✅ 管理类之间的 **依赖与协作**
# - ✅ 使用 `__init__.py` 控制公开接口
# - ✅ 避免循环导入（circular import）等常见陷阱


# ## 🧱 一、核心思想：**高内聚 + 低耦合 + 清晰边界**

# | 原则         | 含义                       | 反例                                               | 正例                                         |
# | ------------ | -------------------------- | -------------------------------------------------- | -------------------------------------------- |
# | **高内聚**   | 一个模块/类只做一件事      | `utils.py` 里有 200 个不相关的函数                 | `auth/` 只处理认证逻辑                       |
# | **低耦合**   | 模块间依赖尽量少、尽量抽象 | `user.py` 直接 import `database.py` 并调用具体函数 | `user.py` 依赖 `Repository` 抽象             |
# | **清晰边界** | 每个包/模块有明确职责      | 所有类塞在 `models.py`                             | 按领域拆分：`users/`, `orders/`, `payments/` |


# ## 📂 二、典型项目结构（中小型 Web 服务为例）

# my_project/
# ├── __init__.py
# ├── main.py                 # 入口
# ├── core/                   # 核心业务逻辑（纯 Python，无框架依赖）
# │   ├── __init__.py
# │   ├── user.py             # User 领域模型
# │   ├── order.py
# │   └── interfaces.py       # Protocol 定义（如 UserRepository）
# ├── infrastructure/         # 基础设施（数据库、邮件、第三方 API）
# │   ├── __init__.py
# │   ├── db.py               # SQLAlchemy / Pydantic 模型
# │   ├── email_service.py
# │   └── user_repository.py  # 实现 core/interfaces.py 中的协议
# ├── api/                    # Web 层（FastAPI / Flask）
# │   ├── __init__.py
# │   ├── user_routes.py
# │   └── schemas.py          # 请求/响应模型
# └── config.py               # 配置

# > ✅ 这种结构叫 **“端口与适配器”（Ports and Adapters）** 或 **“六边形架构”**  
# >
# > - **core** 是“内核”，不依赖任何外部库  
# > - **infrastructure** 是“适配器”，实现 core 定义的接口  
# > - **api** 是“驱动器”，调用 core 业务逻辑


# ## 🔍 三、类的拆分原则：按“职责”而非“类型”

# ### ❌ 反例：按类型拆分（导致高耦合）

# # models.py
# class User: ...
# class Order: ...

# # services.py
# class UserService: ...
# class OrderService: ...

# # repositories.py
# class UserRepository: ...
# class OrderRepository: ...

# **问题**：  

# - 修改“用户”功能，要改 3 个文件  
# - `UserService` 依赖 `UserRepository`，但它们在不同模块 → 难以理解上下文


# ### ✅ 正例：按“领域”拆分（高内聚）

# users/
# ├── __init__.py
# ├── models.py        # User
# ├── service.py       # UserService
# └── repository.py    # UserRepository

# orders/
# ├── __init__.py
# ├── models.py
# ├── service.py
# └── repository.py

# **优势**：

# - 所有“用户”相关代码在一个目录
# - 新人看 `users/` 就懂用户模块全貌
# - 可独立测试、甚至拆成微服务

# > 📌 **DDD（领域驱动设计）思想：以业务领域为中心组织代码**


# ## 🔗 四、类之间的协作：如何安全依赖？

# ### 场景：`UserService` 需要保存用户到数据库

# #### ❌ 错误方式：直接依赖具体实现

# # users/service.py
# from infrastructure.db import get_db_session

# class UserService:
#     def create_user(self, name):
#         db = get_db_session()
#         db.execute("INSERT ...")  # 紧耦合！无法 mock 测试

# #### ✅ 正确方式：依赖抽象（Protocol）

# # core/interfaces.py
# from typing import Protocol

# class UserRepository(Protocol):
#     def save(self, user: User) -> None: ...

# # users/service.py
# from core.interfaces import UserRepository

# class UserService:
#     def __init__(self, user_repo: UserRepository):  # ← 依赖抽象
#         self.user_repo = user_repo

#     def create_user(self, name):
#         user = User(name)
#         self.user_repo.save(user)  # 委托给实现

# # infrastructure/user_repository.py
# from core.interfaces import UserRepository

# class SQLUserRepository(UserRepository):  # 实现协议
#     def save(self, user: User):
#         # 实际数据库操作

# > ✅ 这样：
# >
# > - `core` 不依赖 `infrastructure`
# > - 测试时可注入 `MockUserRepository`
# > - 切换数据库？只需换 `infrastructure` 中的实现


# ## 🚫 五、避免循环导入（Circular Import）

# ### 常见陷阱：

# # users/models.py
# from orders.models import Order

# class User:
#     def get_orders(self) -> list[Order]: ...

# # orders/models.py
# from users.models import User

# class Order:
#     def get_user(self) -> User: ...

# **结果**：`ImportError: cannot import name 'Order'`


# ### ✅ 解决方案：

# #### 方案1：**延迟导入（在函数内 import）**

# # users/models.py
# class User:
#     def get_orders(self):
#         from orders.models import Order  # ← 运行时导入
#         return [Order(...)]

# #### 方案2：**用字符串类型注解 + `from __future__ import annotations`**

# from __future__ import annotations  # Python 3.7+

# class User:
#     def get_orders(self) -> list[Order]: ...  # ← Order 是字符串，不会立即解析

# class Order:
#     def get_user(self) -> User: ...

# #### 方案3：**提取公共接口到上层模块**

# # core/models.py
# class UserRef: ...  # 轻量引用
# class OrderRef: ...

# # users/models.py
# from core.models import UserRef, OrderRef

# > 💡 **最佳实践：尽量避免模块间双向依赖，用“依赖方向图”检查**


# ## 📦 六、`__init__.py` 的妙用：控制公开 API

# ### 默认行为：

# # users/__init__.py （空文件）
# # 外部只能通过完整路径导入：
# from users.service import UserService

# ### ✅ 优化：在 `__init__.py` 中聚合公开接口

# # users/__init__.py
# from .models import User
# from .service import UserService
# from .repository import SQLUserRepository

# __all__ = ["User", "UserService", "SQLUserRepository"]

# 现在外部可以简洁导入：

# from users import UserService, User

# > ✅ **好处**：
# >
# > - 隐藏内部实现（如 `repository.py` 细节）
# > - 提供稳定的公共 API
# > - 未来重构内部文件不影响调用方


# ## 🧪 七、实战：一个用户注册流程的模块化

# # core/user.py
# from typing import Protocol

# class User:
#     def __init__(self, email: str, name: str): ...

# class EmailService(Protocol):
#     def send_welcome_email(self, user: User) -> None: ...

# class UserRepository(Protocol):
#     def save(self, user: User) -> None: ...

# class UserService:
#     def __init__(self, repo: UserRepository, emailer: EmailService):
#         self.repo = repo
#         self.emailer = emailer

#     def register(self, email: str, name: str) -> User:
#         user = User(email, name)
#         self.repo.save(user)
#         self.emailer.send_welcome_email(user)
#         return user

# # infrastructure/email.py
# from core.user import EmailService, User

# class SMTPEmailer(EmailService):
#     def send_welcome_email(self, user: User):
#         print(f"Sending email to {user.email}")

# # api/user_routes.py
# from fastapi import APIRouter
# from core.user import UserService
# from infrastructure import SQLUserRepository, SMTPEmailer

# # 依赖注入（可在 app startup 时配置）
# user_service = UserService(SQLUserRepository(), SMTPEmailer())

# router = APIRouter()
# @router.post("/register")
# def register(email: str, name: str):
#     return user_service.register(email, name)

# ✅ **完全解耦**：  

# - `core` 不知道 FastAPI、SMTP、SQL  
# - 替换邮件服务？只需改 `infrastructure`  
# - 单元测试 `UserService`？注入 mock 对象即可


# ## ✅ 总结：模块化设计 Checklist

# | 问题                  | 检查点                                                   |
# | --------------------- | -------------------------------------------------------- |
# | **结构清晰吗？**      | 按业务领域（而非技术类型）组织包                         |
# | **依赖方向对吗？**    | `core` → 不依赖其他；`infrastructure` → 实现 `core` 接口 |
# | **类职责单一吗？**    | 一个类只做一件事，一个模块只解决一个子问题               |
# | **公开 API 稳定吗？** | 通过 `__init__.py` 控制导出，隐藏内部细节                |
# | **可测试吗？**        | 业务逻辑不依赖具体实现，能轻松 mock                      |
# | **无循环导入吗？**    | 用延迟导入、字符串注解或重构解决                         |


# - #### 问题：

#   - #### 问题1：很抽象，是不是理解就行了

#   - 你的感觉非常真实！👍  
#     **“很抽象”不是你的问题，而是因为这些概念脱离了具体场景。**

#     好消息是：**你不需要一开始就完美掌握所有设计理论**。  
#     在实际编程中，模块化和类组织的技能，**是在“踩坑 + 重构”中慢慢长出来的**。


#     ### ✅ 所以，简单总结成 **3 条你能立刻用上的实践原则**：

#     #### 1. **一个文件别超过 200 行，一个类别超过 100 行**

#     - 如果 `user.py` 越来越长 → 拆成 `models.py`、`service.py`
#     - **目的**：找代码时不用滚半天屏幕

#     #### 2. **不要把所有类塞在一个文件里**

#     - ❌ 别写一个 `models.py` 包含 User、Order、Payment、Product……

#     - ✅ 按功能拆目录：

#       /users    → User 相关
#       /orders   → Order 相关
#       /common   → 公共工具（logger, config）

#     #### 3. **如果两个类互相 import，就危险了！**

#     - 出现循环导入？说明它们**耦合太紧**
#     - 解法：把共用的部分抽出来，或改用函数内 `import`


#     ### 🛠 举个接地气的例子

#     你写了个小项目：

#     # app.py
#     class User:
#         def __init__(self, name): ...
    
#     class Database:
#         def save(self, user): ...
    
#     class EmailService:
#         def send(self, user): ...
    
#     class UserService:
#         def register(self, name):
#             user = User(name)
#             db = Database()
#             db.save(user)
#             email = EmailService()
#             email.send(user)

#     ✅ **现在这样完全 OK！**  
#     等你发现：

#     - `app.py` 超过 300 行
#     - 想换数据库但改不动
#     - 测试 `UserService` 很麻烦

#     **那时**，你自然会想：“啊，是不是该拆一拆了？”

#     → 于是你开始：

#     - 把 `User` 放 `models/`
#     - 把 `Database` 和 `EmailService` 放 `services/`
#     - 让 `UserService` 接收依赖（而不是自己 new）

#     **这就是成长路径**：**先写，再重构，再理解设计原则**。


#     ### 💡 所以结论是：

#     > **理解核心思想（高内聚、低耦合、按功能组织）就够了，不用死记架构图。**  
#     > **真正的模块化能力，来自你亲手把一个“乱糟糟”的项目，一步步整理清晰的经历。**

#     就像学骑车——  
#     你不需要先学牛顿力学，  
#     **骑上去，摔几次，自然就平衡了。**


#     如果你现在有个小项目（哪怕只是 CLI 工具、爬虫、小 Web 应用），  
#     我可以帮你 **现场指导怎么组织类和模块**，这样最不抽象！

#     要不要试试？🙂

# ## ▶️ 下一步建议

# 你已经掌握了 OOP 项目组织的核心！接下来可以学：

# ### 1. **依赖注入容器实战**

# > 如何用 `dependency-injector` 自动管理对象创建和依赖？

# ### 2. **大型项目架构模式**

# > Clean Architecture / Hexagonal Architecture 在 Python 中的落地

# ### 3. **测试驱动开发（TDD）与模块化**

# > 如何从测试出发，设计出高内聚低耦合的模块？

# 请告诉我你想学哪个？例如：  

# > “请用 dependency-injector 实现自动依赖注入”  
# > 或  
# > “我想看 Clean Architecture 的完整 Python 示例”

# 我会为你打造下一章深度教程！📘✨