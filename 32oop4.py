"""
# 第六章：特殊方法（魔术方法 / Magic Methods）
# 第十四步：常用魔术方法
"""

## 🔮 什么是魔术方法？

# - 以双下划线开头和结尾的方法，如 `__init__`、`__str__`
# - **不是直接调用**，而是由 Python **在特定语法下自动触发**
# - 它们定义了对象的“行为协议”——只要你实现了对应方法，就能支持对应操作

# > 💡 核心哲学：**“协议优于继承”**（Duck Typing 的体现）


# 1️⃣ `__str__` 与 `__repr__`：对象的字符串表示
# 用途对比
# | 方法       | 调用方式                  | 目标用户     | 要求                             |
# | ---------- | ------------------------- | ------------ | -------------------------------- |
# | `__str__`  | `str(obj)`, `print(obj)`  | **终端用户** | 可读、简洁、友好                 |
# | `__repr__` | `repr(obj)`, 交互式解释器 | **开发者**   | 尽可能精确，最好能 `eval()` 还原 |
# 容器（如 list）打印时调用的是元素的 __repr__，不是 __str__！
# ✅ 正确示例
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"姓名：{self.name}, 年龄：{self.age} 岁"

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"


p = Person("Alice", 20)
print(p)  # → 姓名：Alice, 年龄：20 岁
print(str(p))  # → 姓名：Alice, 年龄：20 岁
print(repr(p))  # → Person(name='Alice', age=20)


# ⚠️ 常见错误
class Bad:
    def __str__(self):
        return "友好显示"


lst = [Bad()]
print(Bad())
print(lst)  # 输出: [<__main__.Bad object at 0x...>] ❌


# 原因：容器（如 list）打印时调用的是元素的 __repr__，不是 __str__！
### ✅ 最佳实践
# - **所有类都应实现 `__repr__`**（调试必备）
# - 如果需要用户友好输出，再实现 `__str__`
# - 如果只写一个，**优先写 `__repr__`**
# 2️⃣ `__len__`：支持 `len(obj)`
# 让对象支持内置函数 `len()`。
class MyContainer:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


c = MyContainer([1, 2, 3])
print(len(c))  # 入参是列表，返回的是列表的长度
c2 = MyContainer("hello")
print(len(c2))  # 入参是字符串，返回的是字符串的长度
student = {"Alice": 85, "Bob": 92}
print(len(student))  # 入参是字典，返回的是字典的长度

# ⚠️ **必须返回非负整数**，否则会抛出 `TypeError`


# 3️⃣ `__getitem__`, `__setitem__`, `__delitem__`：支持索引操作 `obj[key]`
# 🌰 实现一个类字典对象
class MyDict:
    def __init__(self):
        self._data = {}

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]

    def __delitem__(self, key):
        del self._data[key]

    def __contains__(self, key):
        return key in self._data  # 支持 'key in obj'


d = MyDict()
d["name"] = "Alice"  # → 自动调用默认的__setitem__
print(d["name"])  # → 自动调用默认的__getitem__ → 韩梅梅
print("name" in d)
del d["name"]  # → 自动调用默认的 __delitem__
print("name" in d)  # → 自动调用默认的__contains__


# 🌰 支持切片（类列表）
class MyList:
    def __init__(self, items):
        self._items = list(items)

    def __getitem__(self, index):
        return self._items[index]  # list 自动处理 int 和 slice

    def __len__(self):
        return len(self._items)


ml = MyList([1, 4, 6, 20, 50])
print(ml[0])  # → 1
print(ml[1:3])  # → [4, 6] ✅ 切片自动工作！
# ✅ `index` 可能是 `int`、`slice` 对象，甚至自定义类型（如 NumPy）

# 4️⃣ `__call__`：使对象可调用（像函数一样）
# 让对象支持 `obj()` 语法。
import functools


class Multiplier:
    def __init__(self, factor):  #  这个是初始化的时候传的参数factor
        self.factor = factor

    def __call__(self, x):  # __call__是回调
        if callable(x):
            # x 是函数 → 用作装饰器
            @functools.wraps(x)
            def wrapper(*args, **kwargs):
                result = x(*args, **kwargs)
                return result * self.factor

            return wrapper
        else:
            # x 是普通值 → 直接相乘
            return x * self.factor


double = Multiplier(2)
print(double(8))  # → 16


# 用做装饰器
@Multiplier(3)
def get_num():
    return 6


print(get_num())  # → 18

# ✅ 典型用途：回调、策略对象、状态机、装饰器


# 5️⃣ 比较方法：`__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__ne__`
# 🌰 基础比较
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented  # 返回 NotImplemented
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) < (other.x, other.y)

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"


# 使用
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(0, 5)
print(p1 == p2)  # → True
print(p1 < p3)  # False ← (1,2) > (0,5)
print(p1 != p3)  # True  # True （自动取反）

# print(p1 < "hello")
# print(p1 < 1)
# ⚠️ 关键点
# **返回 `NotImplemented`**，不是 `False`
# → 让 Python 尝试调用 `other.__eq__(self)`，支持不同类型比较


# 如果对象**不可变**且需要作为 `dict` key 或 `set` 元素，**必须实现 `__hash__`**
def __hash__(self):
    return hash((self.x, self.y))


# ✅ 懒人技巧：`@total_ordering`
# 只需实现 `__eq__` + 一个比较方法（如 `__lt__`），其余的`__le__`, `__gt__`, `__ge__`, `__ne__`自动生成：
from functools import total_ordering


@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)


c = Point(1, 2)
d = Point(1, 2)
print(c == d)  # True
print(c < d)  # False
print(c <= d)  # True
print(c > d)  # False
print(c >= d)  # True
print(c != d)  # False

# 🔥 综合实战：构建一个“全能”自定义序列类
from functools import total_ordering


@total_ordering
class SmartList:
    def __init__(self, items: list | None = None):
        self._items = list(items or [])  # 如果 items 不存在，则创建一个空列表

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __repr__(self):
        return f"smartlist({self._items!r})"

    def __str__(self):
        return f"[{', '.join(map(str, self._items))}]"  # map() 返回迭代器

    def __eq__(self, other):
        if not isinstance(other, SmartList):
            return NotImplemented
        return self._items == other._items

    def __lt__(self, other):
        if not isinstance(other, SmartList):
            return NotImplemented
        return self._items < other._items

    def __call__(self, item):
        return item in self._items  # 支持 obj(value) 查询


s = SmartList([1, 5, 8, 19])
print(len(s))  # 4
print(s[0])  # 1
s[0] = 88
print(s)  # smartlist([88, 5, 8, 19])
print(str(s))  # [88, 5, 8, 19]
print(s == SmartList([88, 5, 8, 19]))  # True
print(s(19))  # True ← 调用 __call__, 支持 obj(value) 查询

# ✅ 最佳实践总结
# | 魔术方法      | 何时实现             | 注意事项                           |
# | ------------- | -------------------- | ---------------------------------- |
# | `__repr__`    | **所有类**           | 尽量可 `eval()` 还原               |
# | `__str__`     | 需要用户显示时       | 可读性强                           |
# | `__len__`     | 容器类               | 返回非负整数                       |
# | `__getitem__` | 支持索引/切片        | 处理 `int` 和 `slice`              |
# | `__setitem__` | 可变容器             | 通常配合 `__getitem__`             |
# | `__call__`    | 对象需像函数         | 实现回调、策略                     |
# | `__eq__`      | 需要比较             | 返回 `NotImplemented` 而非 `False` |
# | `__hash__`    | 对象不可变且需作 key | 与 `__eq__` 一致                   |

"""
第十五步：上下文管理协议
"""

# 学完本章，你将能：

# - ✅ 理解 `with` 语句的原理（不只是“打开文件”）
# - ✅ 掌握 `__enter__` 和 `__exit__` 的作用与签名
# - ✅ **自定义类支持 `with obj:` 语法**
# - ✅ 实现**自动资源清理**（如数据库连接、锁、临时文件）
# - ✅ 正确处理 `__exit__` 中的异常（不丢失原始错误！）

# 🔮 一、什么是上下文管理器？为什么需要它？
### 🌰 问题：手动管理资源容易出错

# f = open('data.txt', 'r')
# data = f.read()
# f.close()  # ← 忘记写？出错？文件没关闭！

# 如果中间抛出异常，`f.close()` 可能不会执行！

# ✅ 解决方案：`with` 语句（上下文管理器）
with open("hello.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data)
# 文件自动关闭！即使发生异常！
# 💡 **核心思想**：**“获取资源 → 使用资源 → 无论成功失败，都释放资源”**

# 🔹 二、上下文管理协议：`__enter__` 与 `__exit__`
# 只要一个类实现了这两个方法，它的对象就能用于 `with` 语句：
# | 方法                                             | 作用                                     | 返回值                                   |
# | ------------------------------------------------ | ---------------------------------------- | ---------------------------------------- |
# | `__enter__(self)`                                | 进入 `with` 块时调用                     | 通常返回 `self` 或资源对象               |
# | `__exit__(self, exc_type, exc_value, traceback)` | 退出 `with` 块时调用（**一定会调用！**） | 返回 `True` 表示“抑制异常”，否则传播异常 |

# 🧪 三、实战：自定义一个计时器上下文管理器
# `__enter__`记录的是开始时间，`__exit__`记录的是结束时间，即使出现异常，也会计算耗时多长时间
import time


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self  # ← 通常返回 self，这样 as 后的变量就是它

    def __exit__(self, exc_type, exc_value, traceback):  #  traceback 是异常的调用栈
        elapsed = time.time() - self.start
        print(f"耗时：{elapsed:.4f} 秒")


# 使用
# with Timer() as t:
#     time.sleep(4)
#     print("正在执行任务...")
# 输出:
# 正在执行任务...
# 耗时：4.0010 秒

# ✅ 即使中间出错，也会打印耗时：
# with Timer():
# raise ValueError("出错了！")
# 依然会打印耗时，然后抛出异常
# 输出:
# 耗时：0.0000 秒
# 🔥 四、实战：自定义数据库连接管理器（带异常处理）


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        print(f"连接数据库：{self.db_name}")
        self.connection = f"connection to {self.db_name}"  # 模拟连接
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"正在关闭数据库{self.db_name}连接...")
        # 这里可以调用 self.connection.close()
        if exc_type is not None:
            print(f"捕获到异常：{exc_value}")
            # 返回 False（或不返回）→ 异常继续传播
            # return True → 抑制异常（不推荐，除非你明确知道在做什么）
        else:
            print(f"数据库操作成功！")
        return False  # 显式表示不抑制异常（默认行为）


# 使用
try:
    with DatabaseConnection("my_app.db") as conn:
        print(f"使用连接：{conn}")
        raise RuntimeError("模拟数据库错误")
except Exception as e:
    print(f"外部捕获异常：{e}")
# 无异常输出:
# 连接数据库：my_app.db
# 使用连接：connection to my_app.db
# 正在关闭数据库my_app.db连接...
# 数据库操作成功！

# 有异常输出：
# 连接数据库：my_app.db
# 使用连接：connection to my_app.db
# 正在关闭数据库my_app.db连接...
# 捕获到异常：模拟数据库错误
# 外部捕获异常：模拟数据库错误

# ✅ **关键点**：`__exit__` **总被执行**，且能知道是否发生了异常！

# 📌 五、`__exit__` 的参数详解
# def __exit__(self, exc_type, exc_value, traceback):
# | 参数        | 含义                      | 无异常时 | 有异常时           |
# | ----------- | ------------------------- | -------- | ------------------ |
# | `exc_type`  | 异常类（如 `ValueError`） | `None`   | 异常类型           |
# | `exc_value` | 异常实例                  | `None`   | 异常对象（含消息） |
# | `traceback` | 跟踪信息                  | `None`   | traceback 对象     |

# 💡 你可以用这些信息**记录日志、回滚事务、发送告警**等。

## ⚠️ 六、重要规则：不要轻易返回 `True`

# - 如果 `__exit__` **返回 `True`** → Python 会**吞掉异常**，外部看不到错误！
# - **除非你明确想“忽略某种异常”**，否则**不要返回 `True`**

### ❌ 危险示例（掩盖错误）：

# def __exit__(self, *args):
#     self.close()
#     return True  # ← 所有异常都被吃掉！调试困难！

### ✅ 安全做法：

# def __exit__(self, exc_type, exc_value, traceback):
#     self.close()
    # 不 return，或 return False → 异常正常传播


## 🧩 七、替代方案：用 `@contextmanager` 装饰器（更简洁！）

# 如果你不想写类，可以用 `contextlib.contextmanager`：
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    try:
        yield  # ← 这里是 with 块执行的地方
    finally:
        elapsed = time.time() - start
        print(f"耗时：{elapsed:.4f} 秒")

with timer():
    time.sleep(2)
    print("任务完成")    

# ✅ 适合**简单场景**；复杂逻辑（如需要状态）还是用类。

# ✅ 八、常见应用场景
# | 场景       | 例子                       |
# | ---------- | -------------------------- |
# | 文件操作   | `open()`（内置）           |
# | 线程锁     | `threading.Lock`           |
# | 数据库事务 | 自动 commit/rollback       |
# | 临时目录   | 创建 → 使用 → 自动删除     |
# | API 限流   | 获取令牌 → 使用 → 释放令牌 |
# | 测试 mock  | 打桩 → 测试 → 恢复         |

# 🔚 九、总结：上下文管理器的核心价值
# **“确保 cleanup 代码一定执行，无论成功或失败。”**
# | 特性         | 说明                                        |
# | ------------ | ------------------------------------------- |
# | **自动调用** | `__enter__` / `__exit__` 由 `with` 自动触发 |
# | **异常安全** | 即使崩溃，`__exit__` 也会运行               |
# | **资源隔离** | 避免资源泄漏（文件、内存、连接等）          |
# | **代码清晰** | 资源管理逻辑集中，业务代码干净              |

