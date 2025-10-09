"""
# 第七章：高级特性
# 第十六步：描述符（Descriptor）
"""
# 🔮 一、什么是描述符？—— Python 的“属性拦截器”
# **描述符是一个实现了 `__get__`、`__set__` 或 `__delete__` 方法的对象。**  
# 它可以**控制对另一个对象属性的访问行为**。

# 当你写：
# obj.attr = value   # → 可能触发描述符的 __set__
# x = obj.attr       # → 可能触发描述符的 __get__
# del obj.attr       # → 可能触发描述符的 __delete__
# Python 会检查 `attr` 是否是一个**描述符**，如果是，就调用对应方法！
# 🔹 二、描述符协议：三个核心方法
# | 方法         | 触发时机   | 签名                               |
# | ------------ | ---------- | ---------------------------------- |
# | `__get__`    | 访问属性时 | `__get__(self, obj, objtype=None)` |
# | `__set__`    | 设置属性时 | `__get__(self, obj, value)`        |
# | `__delete__` | 删除属性时 | `__delete__(self, obj)`            |
# ⚠️ **关键规则**：描述符必须作为**类属性**定义，**不能是实例属性**！

# 🧪 三、实战 1：手写一个 `@property`（只读属性）
# Python 内置的 `@property` 就是一个**只实现了 `__get__` 的描述符**。
# ✅ 我们来自己实现一个：
class property:
    def __init__(self, func):
        self.func = func
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self  # 类访问时返回描述符自身
        return self.func(obj)  # 调用原函数
# 使用
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return 3.14159 * self.radius ** 2
c = Circle(5)
print(c.area)  #78.53975
# c.area = 100  # 会报错！因为我们没实现 __set__

# ✅ 这就是 `@property` 的简化版！  
# （真实 `property` 还支持 setter/deleter，我们后面讲）

# 🧪 四、实战 2：带类型检查的描述符
class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None # 稍后由元类或 __set_name__ 设置
    def __set_name__(self, owner, name):
        # Python 3.6+：自动记录属性名
        self.name = name
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]
    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"期望类型：{self.expected_type.__name__}, 但实际类型是：{type(value).__name__}")
        obj.__dict__[self.name] = value

# 使用
class Person:
    name = Typed(str)
    age = Typed(int)

p = Person()
p.name = "xiaoming"
p.age = 29
# p.age = "19" # TypeError: 期望类型：int, 但实际类型是：str
print(p.name, p.age)
# ✅ 这就是 ORM（如 Django Model）字段的底层原理！

# 🔍 五、描述符如何工作？—— 属性查找顺序
# 当你访问 `obj.attr`，Python 按以下顺序查找：
# 1. **数据描述符**（实现了 `__set__` 或 `__delete__`） → 优先！
# 2. **实例字典** `obj.__dict__['attr']`
# 3. **非数据描述符**（只实现 `__get__`）
# 4. **类字典**、父类等...
# 🌰 示例：为什么描述符必须在类上？
class Desc:
    def __get__(self, obj, objtype):
        return "来自描述符"
class A:
    attr = Desc() # 类属性
a = A()
print(a.attr)  # → 来自描述符

# 错误做法
a.bad_desc = Desc() # 实例属性 → 不是描述符！
print(a.bad_desc) #<__main__.Desc object at 0x0000016C3B12CB90> （直接返回对象）

# ✅ **只有类属性才能触发描述符协议！**
## 🔥 六、揭秘 `@property` 的完整实现

# Python 内置的 `property` 是一个**数据描述符**，支持 getter/setter/deleter：

class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("不可读")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("不可写")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("不可删除")
        self.fdel(obj)

    def setter(self, fset):
        # 返回一个新的 property 对象（支持链式调用）
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

# 使用
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @MyProperty
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = value

t = Temperature()
t.celsius = 25
print(t.celsius)  # 25
# t.celsius = -300  # ValueError

# > ✅ 这就是 `@property` 的完整工作原理！


## ⚠️ 七、常见陷阱与最佳实践

## ❌ 陷阱 1：描述符被实例属性覆盖（非数据描述符）
class Desc:
    def __get__(self, obj, objtype):
        return "来自描述符"
class A:
    attr = Desc()
a = A()
a.attr = "来自实例属性" # 覆盖了描述符！
print(a.attr)  # "来自实例属性" （描述符失效）
# ✅ **解决方案**：实现 `__set__`（变成数据描述符），优先级更高！
### ❌ 陷阱 2：多个实例共享描述符状态

class BadDesc:
    value = None  # 类变量 → 所有实例共享！

    def __set__(self, obj, value):
        self.value = value  # 错！修改的是描述符自身的属性

class A:
    x = BadDesc()

# ✅ **正确做法**：把值存到 **实例的 `__dict__`** 中（如前面 `Typed` 示例）

### ✅ 最佳实践

# - 用 `__set_name__`（Python 3.6+）自动获取属性名
# - 值存储在 `obj.__dict__`，避免共享
# - 数据描述符（有 `__set__`）优先级高于实例属性
# - 非数据描述符（只有 `__get__`）可被实例属性覆盖

# 🧩 八、描述符 vs `__getattr__` / `__setattr__`
# | 方案          | 粒度                 | 性能                      | 适用场景                     |
# | ------------- | -------------------- | ------------------------- | ---------------------------- |
# | **描述符**    | **单个属性**         | 高（只拦截特定属性）      | 类型检查、计算属性、ORM 字段 |
# | `__getattr__` | **所有未找到的属性** | 低（每次都要走 fallback） | 代理、动态属性               |
# | `__setattr__` | **所有属性赋值**     | 低（全局拦截）            | 日志、验证所有属性           |

# ✅ **描述符是“精准打击”，其他是“全面监控”**

## ✅ 九、总结：描述符的核心思想
# > **“将属性的访问逻辑封装成独立对象，实现关注点分离。”**

# | 特性           | 说明                                       |
# | -------------- | ------------------------------------------ |
# | **协议驱动**   | 实现 `__get__`/`__set__` 即可              |
# | **类级别定义** | 必须是类属性                               |
# | **控制粒度细** | 可针对单个属性定制行为                     |
# | **性能高**     | 只拦截目标属性                             |
# | **应用广泛**   | `@property`, `@classmethod`, ORM, 验证器等 |

# 🧪 动手实验：打印每一步，亲眼看到描述符运行
class LoggedDescriptor:
    def __set_name__(self, owner, name):
        self.name = name  # 自动记录属性名，比如 'age'
        print(f"描述符'{name}'已经绑定到类{owner.__name__}上")
    def __get__(self, obj, objtype=None):# → 此时 `obj` 是 `None`，是因为 通过类访问（不是实例），你应该返回描述符自身（或类级别数据）。
        print(f"调试描述符：__get__ called: self={self}, obj={obj}, objtype={objtype}")
        if obj is None:
            print(f"通过类访问: {objtype.__name__}.{self.name}")
            return self # 返回描述符对象本身
        print(f"读取实例 {obj} 的 '{self.name}'属性") 
        return self.__dict__.get(self.name, "未设置") # 从实例字典读
    def __set__(self, obj, value):
        print(f"设置实例 {obj} 的 '{self.name}'属性为{value}")
        self.__dict__[self.name] = value # 存到实例字典
# 使用：像声明变量一样使用！
class Student:
    score = LoggedDescriptor() # 类属性 ← 这不是普通变量！是描述符！ 执行完会输出：描述符'score'已经绑定到类Student上

# 创建实例
s1 = Student()
s2 = Student()

print("\n-----设置s1.score-----")
s1.score = 98           #设置<__main__.Student object at 0x000001E1AE8D7770>的'score'属性为98
print("\n-----读取s1.score-----")
print("结果：", s1.score)   #读取<__main__.Student object at 0x000001E1AE8D7770>的'score'属性
print("\n-----设置s2.score-----")
s2.score = 99
print("\n-----读取s2.score-----")
print("结果：", s2.score)
print(Student.score)  # 通过类访问（不是实例）

# ✅ 你看：**同一个描述符（score）被两个实例共享，但数据（95, 88）是分开存储的！**

# 📌 关键总结
# | 访问方式        | `obj` 参数        | 正确做法                                              |
# | --------------- | ----------------- | ----------------------------------------------------- |
# | `Student.score` | `obj = None`      | 返回 `self` 或类级别数据，**不要访问 `obj.__dict__`** |
# | `s.score`       | `obj = s`（实例） | 可以安全使用 `obj.__dict__`                           |



# 描述符的本质是：**  
# **“把属性的访问行为（get/set）变成可编程的函数调用”**

## 🤔 回答你可能的疑问

### ❓ 为什么不能把描述符定义在 `__init__` 里？

# def __init__(self):
#     self.score = LoggedDescriptor()  # ❌ 错误！

# → 因为这样 `score` 是**实例属性**，Python **不会触发描述符协议**！  
# → 描述符必须是**类属性**，Python 才会在属性访问时检查它。

### ❓ `__get__` 里的 `obj` 为什么有时是 `None`？

# print(Student.score)  # 通过类访问（不是实例）

# → 此时 `obj` 是 `None`，你应该返回描述符自身（或类级别数据）。

### ❓ 和 `@property` 有什么区别？

# - `@property` 是描述符的**特例**（只读或带 setter）
# - 描述符是**通用机制**，可复用、可参数化（如 `PositiveInteger()`）
'''
第十七步：**元类（Metaclass）**
'''
# 99% 的 Python 程序员不需要写元类，但 100% 的 Python 程序员应该理解它。
# - ✅ 理解 **“类也是对象”** 的核心思想
# - ✅ 掌握 `type` 的双重身份：**类型构造器** vs **元类**
# - ✅ 编写自定义元类，**在类创建时自动修改类行为**
# - ✅ 看懂 Django、SQLAlchemy、Pydantic 等框架的元类魔法
# - ✅ 知道何时该用（或不该用）元类

# 🔮 一、前置认知：在 Python 中，**一切皆对象**
x = 34
print(type(x))  # 输出：<class 'int'>
print(type(int))  # 输出:<class 'type'>

def f(): pass
f_field = f()
print(type(f))  # 输出:<class 'function'>
# print(type(function)) # NameError → 但 function 类型也是 type 的实例

class MyCls: pass
print(type(MyCls))  # 输出:<class 'type'>   ← 类本身也是对象！

# ✅ **关键结论**：  

# - `42` 是 `int` 的实例  
# - `int` 是 `type` 的实例  
# - `MyClass` 是 `type` 的实例  
# - **`type` 是“类的类” → 这就是元类！**

# 🔹 二、`type` 的两种用法
### 1️⃣ 查看对象类型（常见用法）

type(42)        # → <class 'int'>
type("hello")   # → <class 'str'>

### 2️⃣ **动态创建类**（元类用法！）
# 等价于：class MyClass:
#             x = 10
MyClass = type("MyClass", (), {"x": 10})
obj = MyClass()
print(obj.x)

# `type(name, bases, dict)` 三个参数：

# - `name`：类名（字符串）
# - `bases`：父类元组（如 `(object,)`）
# - `dict`：类属性字典（方法、变量等）

# > ✅ **`type` 就是 Python 默认的元类！**

# 🔥 三、什么是元类？—— “类的制造工厂”
# **元类（Metaclass）是创建类的类。**  
# 普通类 → 创建实例  
# 元类 → 创建类
# | 创建者             | 对象               | 关系                       |
# | ------------------ | ------------------ | -------------------------- |
# | 类（如 `MyClass`） | 实例（如 `obj`）   | `obj = MyClass()`          |
# | 元类（如 `type`）  | 类（如 `MyClass`） | `MyClass = MetaClass(...)` |

## 🧪 四、自定义元类：拦截类的创建过程

### 场景：自动将所有方法名转为大写（演示用）
class UpperMeta(type): # 继承 type
    def __new__(mcs, name, bases, namespace): # 重写 __new__
        # mcs = 元类自身（UpperMeta）
        # name = 类名
        # bases = 父类元组
        # namespace = 类的属性字典（包含方法、变量）
        # 修改 namespace：把所有函数名转大写
        new_namespace = {}
        for key,value in namespace.items():
            if callable(value) and not key.startswith("__"): # 如果是函数 且 不是私有属性
                new_namespace[key.upper()] = value
            else:
                new_namespace[key] = value
        # 调用父类（type）创建类
        return super().__new__(mcs, name, bases, new_namespace)
    
# 使用元类
class MyClass(metaclass=UpperMeta):
    def hello(self):
        print("hello")
    def world(self):
        print("world")

# 测试
obj = MyClass()
# print(obj.hello()) # 报错'MyClass' object has no attribute 'hello'
print(obj.HELLO()) 
print(obj.WORLD())

# ✅ **元类在类定义时就生效了！** 不是实例化时。

# 🔍 五、元类的典型使用场景（框架开发）
# ✅ 1. **自动注册子类**（插件系统、工厂模式）
registry = {}
class RegisterMeta(type):
    def __new__(mcs, name, bases, namespace):
        new_cls = super().__new__(mcs, name, bases, namespace)
        if name != "Base":  # 跳过基类
            registry[name] = new_cls
        return new_cls
class Base(metaclass=RegisterMeta):
    pass
class Dog(Base):
    pass
class Cat(Base):
    pass
print(registry) # 元类是在类定义时就生效了！所以 registry 中已经有数据了！ 
# 🌰 Django Admin、Flask 蓝图、FastAPI 路由都用类似机制。
# ✅ 2. **ORM 模型字段收集**（如 Django Model）
class Field:
    def __init__(self, field_type):
        self.field_type = field_type
class ModelMeta(type):
    def __new__(mcs, name, bases, namespace):
        fields = {}
        for key, value in list(namespace.items()):
            if isinstance(value, Field):
                fields[key] = value
                namespace.pop(key)   # 从类属性中移除，避免实例覆盖
        namespace["_fields"] = fields
        return super().__new__(mcs, name, bases, namespace)
class Model(metaclass=ModelMeta):
    pass
class User(Model):
    name = Field(str)
    age = Field(int)

print(User._fields)
# ✅ 这就是 Django `User.objects.create(name="Alice")` 背后的魔法！
# ✅ 3. **强制接口实现**（类似抽象基类，但更灵活）
class InterfaceMeta(type):
    def __new__(mcs, name, bases, namespace):
        if name != "BaseAPI":
            required_methods = {"connect", "disconnect"}
            implemented_methods = {k for k, v in namespace.items() if callable(v)}
            missing_methods = required_methods - implemented_methods
            if missing_methods:
                raise TypeError(f"类{name}缺少方法：{missing_methods}")
        return super().__new__(mcs, name, bases, namespace)
class BaseAPI(metaclass=InterfaceMeta):
    pass
class MyAPI(BaseAPI):
    def connect(self): pass
    def disconnect(self): pass # ✅ 完整实现
# class BadAPI(BaseAPI):
#     def connect(self): pass  # ❌ 缺少 disconnect，报错！
# ⚠️ 六、元类 vs 类装饰器？何时用哪个？
# | 特性                  | 元类               | 类装饰器   |
# | --------------------- | ------------------ | ---------- |
# | **作用时机**          | 类创建时           | 类创建后   |
# | **能否修改类名/继承** | ✅ 可以             | ❌ 不行     |
# | **能否影响子类**      | ✅ 可以（通过继承） | ❌ 仅当前类 |
# | **复杂度**            | 高                 | 低         |
# | **可读性**            | 较差               | 较好       |

# ✅ **建议**：  

# - 优先用 **类装饰器** 或 **描述符**  
# - 只有当需要 **影响子类** 或 **修改类结构** 时，才用元类

## 🔒 七、元类的继承规则

# Python 如何决定用哪个元类？

# 1. 如果类指定了 `metaclass=...`，就用它
# 2. 否则，从父类中继承元类
# 3. 如果多个父类有不同元类，必须兼容（通常用 `type` 的子类）

class MetaA(type): pass
class MetaB(type): pass

class A(metaclass=MetaA): pass
class B(metaclass=MetaB): pass

# class C(A, B):  # ❌ 报错！元类冲突
#     pass

# 解决方案：定义兼容的元类
class MetaAB(MetaA, MetaB): pass

class C(A, B, metaclass=MetaAB): pass  # ✅


## ✅ 八、总结：元类的核心思想
# **“不要问对象能做什么，而要问它的类是怎么被创建的。”**
# | 概念                  | 说明                               |
# | --------------------- | ---------------------------------- |
# | **类是对象**          | `MyClass` 本身是一个 `type` 的实例 |
# | **元类是类的类**      | 控制类如何被创建                   |
# | **`type` 是默认元类** | 所有类都由 `type` 创建             |
# | **元类用于“元编程”**  | 在类定义阶段修改类行为             |
# | **慎用！**            | 95% 的场景可用装饰器/描述符替代    |

## 💡 九、一句话记住元类

# > **“元类让你在 `class MyClass:` 这一行代码执行时，插入自己的逻辑。”**


'''
第十八步：**数据类（dataclass）**（Python 3.7+）
'''
# 它解决了 Python 中一个经典痛点：  
# > “我只想定义一个简单的数据容器，为什么要写 20 行样板代码？”
# `@dataclass` 就是答案！

## 🔮 一、痛点：没有 dataclass 时的“样板代码地狱”

# 假设你想定义一个 `Person` 类，包含 `name` 和 `age`：

# 没有 dataclass 的写法（Python 3.6 及以前）
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash((self.name, self.age))

# > 😩 20 行代码，只为存两个字段！而且容易出错。

# ✨ 二、`@dataclass`：一行搞定！
from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int
# ✅ 自动生成了什么？
# | 方法            | 自动生成？ | 行为                                           |
# | --------------- | ---------- | ---------------------------------------------- |
# | `__init__`      | ✅          | `def __init__(self, name: str, age: int): ...` |
# | `__repr__`      | ✅          | `Person(name='Alice', age=30)`                 |
# | `__eq__`        | ✅          | 按字段值比较是否相等                           |
# | `__hash__`      | ❌（默认）  | 如果 `eq=True` 且 `frozen=False`，则不生成     |
# | `__lt__` 等比较 | ❌          | 需手动开启                                     |

# 🧪 测试一下：
p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
print(p1)   # Person(name='Alice', age=30)
print(p1 == p2)  # True
print(p1 is p2)  # False
# ✅ **结构化数据，值语义比较** —— 这正是我们想要的！

# 🔧 三、控制 dataclass 行为：装饰器参数
# `@dataclass` 接受多个参数，精细控制生成逻辑：
@dataclass(
    init=True,      # 是否生成 __init__
    repr=True,      # 是否生成 __repr__
    eq=True,        # 是否生成 __eq__
    order=False,    # 是否生成 __lt__, __le__, __gt__, __ge__
    unsafe_hash=False,
    frozen=False,   # 是否只读（类似 namedtuple）
    slots=False,    # Python 3.10+：是否使用 __slots__
)
class MyClass:
    ...

# 🌰 示例：只读数据类（`frozen=True`）
@dataclass(frozen=True)
class Point:
    x: float
    y: float
p = Point(1.0, 3.0)
print(p)  # Point(x=1.0, y=3.0)
# p.x = 2. #dataclasses.FrozenInstanceError: cannot assign to field 'x'

# ✅ 这比手写 `__slots__` + 私有属性 + property 更简洁！

# 📦 四、字段（Field）控制：`field()`

# 有时你需要更精细地控制**每个字段**的行为，比如：

# - 设置默认值
# - 指定哪些字段参与比较
# - 标记某些字段“仅用于内部，不参与 repr”

# 这时用 `field()` 函数：

from dataclasses import dataclass,field
@dataclass
class Student:
    name: str
    age: int 
    score: float = 0.0 # 默认值：简单类型直接赋值
    courses: list = field(default_factory=list)   # 复杂默认值（如 list, dict）必须用 default_factory！
    _id: int = field(default=0, repr=False, compare=False)  # 内部字段：不参与 repr 和比较
    hobbies: tuple = field(default_factory=tuple)
#测试
s = Student("Alice", 30)
print(s)  # Student(name='Alice', age=30, score=0.0, courses=[], hobbies=())
s.score = 88
print(s)  # Student(name='Alice', age=30, score=88.0, courses=[], hobbies=())

# ⚠️ 重要：为什么用 `default_factory`？
# ❌ 千万不要这样写！
# bad_courses: list = []  # 所有实例共享同一个 list！

# ✅ 正确写法
# courses: list = field(default_factory=list)  # 每个实例新建一个 list
# 💡 `default_factory` 必须是**无参可调用对象**（如 `list`, `dict`, `lambda: [...]`）



# 🧪 五、实战：完整示例
from dataclasses import dataclass,field
@dataclass(order=True) # 启用排序（按字段在类中声明的顺序，组成元组比较）
class Employee:
    # 排序时只考虑 rank 和 name
    # 把排序用的组合字段sort_index放第一个！
    sort_index: int = field(init=False, repr=False) # - init=False：创建对象时不用传这个参数 - repr=False：打印对象时不显示这个内部字段
    name: str
    age: int
    rank: str = "Junior"
    skills: list[str] = field(default_factory=list)

    def __post_init__(self): # `__post_init__` 是 dataclass 特有的钩子，用于初始化'__init__'后处理！
        # 初始化后自动计算 sort_index
        self.sort_index = (self.rank, self.name) #组合字段 sort_index = (rank, name)

# 使用
e1 = Employee("Alice", 30, "Senior", ["Python", "Java"])
e2 = Employee("Bob", 25, "Junior", ["Python", "C++"])
print(e1)  # Employee(name='Alice', age=30, rank='Senior', skills=['Python', 'Java'])
#实际上是这样排序的：
# (self.sort_index, self.name, self.age, self.rank) > (other.sort_index, other.name, other.age, other.rank)
print(e1 > e2)  # True（因为 "Senior" > "Junior"）
employees = [e1, e2]
employees.sort()  # 根据 sort_index 排序，默认是升序
print(employees)  # [Employee(name='Alice', age=30, rank='Senior', skills=['Python', 'Java']), Employee(name='Bob', age=25, rank='Junior', skills=['Python', 'C++'])]
# ✅ `__post_init__` 是 dataclass 特有的钩子，用于初始化后处理！

# 🔍 六、`@dataclass` vs 其他方案对比
# | 方案                | 优点                             | 缺点                             | 适用场景                 |
# | ------------------- | -------------------------------- | -------------------------------- | ------------------------ |
# | **`@dataclass`**    | 自动生成方法、类型提示友好、灵活 | 需 Python 3.7+                   | **大多数结构化数据类** ✅ |
# | `namedtuple`        | 内存高效、不可变                 | 不支持默认值（旧版）、无类型提示 | 简单不可变记录           |
# | 普通类              | 完全控制                         | 样板代码多                       | 需要复杂逻辑的类         |
# | `typing.NamedTuple` | 带类型提示的 namedtuple          | 仍是 tuple，不能继承             | 类型安全的轻量结构       |
# | `attrs` 库          | 功能更强大（第三方）             | 需要安装                         | 老版本 Python 或高级需求 |
# ✅ **现代 Python 开发首选：`@dataclass`**
# ⚙️ 七、高级技巧
@dataclass
class Animal:
    name: str

@dataclass
class Dog(Animal):
    hobby: str
# 自动生成 __init__(self, name: str, hobby: str)
e = Dog("xiaobu","eat dog food")
print(e)    # Dog(name='xiaobu', hobby='eat dog food')

# 2. **禁用某个方法**
@dataclass(eq=False)  # 不生成 __eq__
class UniqueObject:
    id: str
# 3. **与 `__slots__` 结合（Python 3.10+）**
@dataclass(slots=True)
class Point:
    x: float
    y: float
# 自动添加 __slots__ = ('x', 'y') → 节省内存
print(Point.__slots__)

# ✅ 八、总结：`@dataclass` 的核心价值
# **“用声明式语法，自动生成数据类的样板代码。”**
# | 特性             | 说明                                      |
# | ---------------- | ----------------------------------------- |
# | **减少样板代码** | 自动实现 `__init__`, `__repr__`, `__eq__` |
# | **类型提示友好** | 原生支持 `name: str` 语法                 |
# | **高度可配置**   | 通过参数和 `field()` 精细控制             |
# | **可扩展**       | 支持继承、`__post_init__`、手动覆盖方法   |
# | **现代标准**     | Python 官方推荐的数据类方案               |

