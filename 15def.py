"""
**函数（function）** 的世界了——这是你从“写脚本”迈向“写程序”的关键一步！
"""
# ✅ **函数的核心价值**：

# - **避免重复代码,提高代码的复用性**（DRY 原则：Don’t Repeat Yourself）
# - **提高可读性**（`validate_email()` 比一堆 if 更清晰）
# - **便于测试和调试**（单独测试一个函数）
# - **模块化编程的基础**（后续学类、模块、包都依赖函数）


# 二、定义函数：`def`
# 基本语法
# def 函数名(参数1, 参数2, ...):
#     """文档字符串（可选但推荐）"""
#     # 函数体
#     return 结果  # 可选
def greet(name):
    """返回一个问候语"""
    return f"Hello, {name} !"


message = greet("Alice")
print(message)  # 输出：Hello, Alice !
# 🔸 函数名推荐用 **小写字母 + 下划线**（`calculate_total`）


#  三、函数参数详解
# 1. **位置参数（最常用）**
def add(a, b):
    return a + b


print(add(3, 6))


# 2. **默认参数（可选参数）**
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(greet("小明"))  # 输出：Hello, 小明！
print(greet("小红", "你好"))  # 输出：你好，小红！

# ⚠️ **默认参数必须放在位置参数之后！**  上面的例子，`greeting` 是默认参数，必须放在 `name` 之后！


# 3. **关键字参数（调用时指定参数名）**
def create_user(name, age, city="北京"):
    return {"name": name, "age": age, "city": city}


# 用关键字调用，顺序可变
user = create_user(age=30, name="Alice", city="上海")
print(user)
# 4. **可变参数**
# ✅ **参数顺序黄金法则**：
# `位置参数` → `默认参数` → `*args` → `**kwargs`


# (1) `*args`：接收任意多个**位置参数**（打包成元组）
def sum_all(*args):  # 前面只有一个星号！
    return sum(args)


print(sum_all(1, 4, 6, 7, 2, 9))  # 输出：29


# (2) `**kwargs`：接收任意多个**关键字参数**（打包成字典）
def print_info(**kwargs):  # 前面有两个星号！
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(username="lisi", age=29, is_student=True)


# (3) 混合使用（顺序不能错！）
def mixed_param(a, b=20, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")


mixed_param(10, 40, 70, "hello", "world", name="Nico", age=28)
# a=10, b=40
# args=(70, 'hello', 'world')
# kwargs={'name': 'Nico', 'age': 28}

# ✅ **参数顺序黄金法则**：
# `位置参数` → `默认参数` → `*args` → `**kwargs`


#  四、返回值：`return`

# - 函数可以返回**任意类型**：数字、字符串、列表、字典、甚至另一个函数！
# - 没有 `return` 或 `return` 后无值 → 返回 `None`


# 示例：返回多个值（其实是返回元组！）
def min_max(numbers):
    return min(numbers), max(numbers)


nums = [1, 5, 3, 9, 2]
minimum, maximum = min_max(nums)  # 元组解包
print(minimum, maximum)
# 💡 这就是你之前学的“元组解包”在函数中的经典应用！

# 五、变量作用域（重要！）
# 1. **局部变量 vs 全局变量**
x = "全局变量"


def test():
    x = "局部变量"  # 新建局部变量，不影响全局
    print(x)  # 局部变量


test()  # 输出：局部变量
print(x)  # 输出：全局变量

# 2. **用 `global` 修改全局变量（谨慎使用！）**
count = 0


def increment():
    global count  # 告诉函数，`count` 是全局变量
    count += 1


increment()
print(count)  # 输出：1


# ✅ **最佳实践**：尽量避免 `global`，通过参数和返回值传递数据！
def login_user_good(username, current_count):
    """
     处理用户登录，并返回新的登录次数。

    参数:
        username (str): 用户名
        current_count (int): 当前登录次数

    返回:
        int: 新的登录次数
    """
    new_count = current_count + 1
    print(f"用户 {username} 已登录，登录次数为 {new_count}")
    return new_count  # 返回新的登录次数


login_count = 0
login_count = login_user_good("Alice", login_count)
login_count = login_user_good("Bob", login_count)
print("总登录次数: ", login_count)


# 进阶：用字典管理多个用户状态（更真实场景）
def login_user_v2(username, user_status):
    """
    登录用户，并更新其登录次数。

    参数:
        username (str): 用户名
        user_stats (dict): 用户状态字典，如 {"Alice": 2, "Bob": 1}

    返回:
        dict: 更新后的 user_stats
    """

    user_status = user_status.copy()  # 深拷贝 （防止修改原字典！）
    user_status[username] = user_status.get(username, 0) + 1
    print(f"{username} 登录成功！ 累计{user_status[username]}次登录")
    return user_status


status = {}
status = login_user_v2("Alice", status)
status = login_user_v2("Bob", status)
status = login_user_v2("Alice", status)
print(status)  # 输出：{'Alice': 2, 'Bob': 1}
# 💡 这就是**状态通过参数传入、通过返回值传出**的典型模式，广泛用于 Web 开发、游戏逻辑、数据处理等。

# ✅ **记住一句话**：
# **“函数应该像数学公式：给定输入，返回确定输出，不依赖外部状态。”**


# 六、文档字符串（docstring）
# 用三引号 `"""` 写函数说明，可用 `help()` 查看：
def divide(a, b):
    """
    返回 a 除以 b 的结果。

    参数:
        a (float): 被除数
        b (float): 除数（不能为0）

    返回:
        float: 除法结果

    异常:
        ZeroDivisionError: 当 b 为 0 时
    """
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b


# 查看帮助
# help(divide)
# ✅ 写好 docstring 是专业程序员的习惯！

#  七、函数作为“一等公民”
# 在 Python 中，**函数也是对象**！可以：赋值给变量、作为参数传给其他函数、作为返回值

# 1. 赋值给变量
say_hello = greet
print(say_hello("Tom"))  # 输出：Hello, Tom!


# 2. 作为参数传给其他函数
def apply(func, value):
    return func(value)


result = apply(greet, "Alice")
print(result)  # 输出：Hello, Alice!


# 3. 作为返回值
def make_multiplier(n):
    def multiplier(x):
        return x * n

    return multiplier  # 返回函数对象


double = make_multiplier(2)
print(double(5))  # 输出：10
# 🔸 这就是**闭包（closure）** 的基础，后续学装饰器会用到！
# 代码分析：
### 1. `make_multiplier(2)` 被调用

# - 参数 `n = 2`
# - 定义了一个内部函数 `multiplier(x)`，它会用到 `n`
# - **返回这个内部函数本身**（注意：不是调用它，是返回函数对象！）

# > ✅ 此时，`multiplier` 函数“记住”了 `n = 2`，即使 `make_multiplier` 已经执行完了！

### 2. `double` 现在就是那个“记住 n=2 的函数”

# double = make_multiplier(2)
# double 现在等价于：
# def multiplier(x):
#     return x * 2

### 3. 调用 `double(5)`

# - 相当于调用 `multiplier(5)`
# - 它还记得 `n = 2`，所以返回 `5 * 2 = 10`


## 🌟 关键概念：**闭包（Closure）**

# > **闭包 = 内部函数 + 它“记住”的外部变量**

# 在这个例子中：

# - 内部函数：`multiplier`
# - 记住的变量：`n`（来自外层函数 `make_multiplier` 的参数）
# - 即使外层函数已经结束，`n` 依然被“捕获”并保留！

# ✅ 这就是**闭包**：函数“闭合”了它需要的外部环境。


# 闭包 = 内部函数 + 它“记住”的外部变量

# 闭包的几个例子
# 例子 1：制造“×3”、“×10” 的机器
triple = make_multiplier(3)
times10 = make_multiplier(10)
print(triple(5))  # 输出：15
print(times10(5))  # 输出：50
# 每个函数都“记住”了自己的 `n`！


# 例子 2：用闭包实现计数器（不用 global！）
def make_counter():
    count = 0

    def counter():
        nonlocal count  # 声明要修改外层变量
        count += 1
        return count

    return counter  # 返回函数对象！


# 创建一个计数器
my_counter = make_counter()
print(my_counter())  # 输出：1
print(my_counter())  # 输出：2
print(my_counter())  # 输出：3

# ✅ 这里 `count` 被闭包“记住”，**不需要 global**，也能保持状态！


# 例子 3：经典例子：装饰器（decorator） 感觉像java中的AOP
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"调用{func.__name__}")
        return func(*args, **kwargs)

    return wrapper  # 返回的是闭包


@log_calls
def greet(name):
    print(f"Hello, {name}")


greet("Alice")  # 输出：调用greet    Hello, Alice


# 八、实战项目：简易计算器（用函数）
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide_safe(a, b):
    if b == 0:
        return "错误：除数不能为0"
    return a / b


# 主程序
while True:
    print("============简易计算器============")
    print(" 1. 加法\n 2.减法\n 3.乘法\n 4.除法\n 5.退出")
    choice = input("请选择操作：")
    if choice == "5":
        print("退出计算器")
        break

    num1 = float(input("请输入第一个数："))
    num2 = float(input("请输入第二个数："))

    if choice == "1":
        print("结果是：", add(num1, num2))
    elif choice == "2":
        print("结果是：", subtract(num1, num2))
    elif choice == "3":
        print("结果是：", multiply(num1, num2))
    elif choice == "4":
        print("结果是：", divide_safe(num1, num2))
    elif choice == "5":
        print("退出计算器")
        break
    else:
        print("无效的选择，请重新选择！")

#  九、常见错误 & 避坑指南
# | 错误               | 说明                   | 正确做法                      |
# | ------------------ | ---------------------- | ----------------------------- |
# | 忘记 `return`      | 函数返回 `None`        | 明确写 `return`               |
# | 默认参数是可变对象 | 多次调用共享同一个对象 | 默认值用 `None`，函数内初始化 |
# | 混淆局部/全局变量  | 修改不了全局变量       | 用 `global` 或通过返回值      |
# | 参数顺序错误       | `*args` 放在默认参数前 | 遵守参数顺序规则              |

# ✅ **可变默认参数陷阱**：

# ❌ 危险！
# def add_item(item, target=[]):
#     target.append(item)
#     return target

# print(add_item(1))  # [1]
# print(add_item(2))  # [1, 2] ← 意外！


# ✅ 正确做法
def add_item(item, target=None):
    if target is None:
        target = []
        target.append(item)
        return target


print(add_item(1))  # [1]
print(add_item(2))  # [2]


# ✅ 十、动手练习
# 练习 1：计算阶乘
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # 递归实现


print(factorial(5))


# 练习 2：检查是否为质数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  #  n**0.5 表示 对变量 n 开平方根。
        if n % i == 0:
            return False
    return True


print(is_prime(7))


# 练习 3：合并两个字典（用函数封装）
def merge_dicts(d1, d2):
    # return d1 | d2
    return {**d1, **d2}


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = merge_dicts(d1, d2)
print(merged)


# 📌 十一、函数与其他数据结构结合
# 1. 函数 + 字典：实现“命令模式”
# 字典的值可以是函数，这样就能用字符串“名字”来调用对应的函数，实现“命令模式”。
def handle_add():
    return "执行添加操作"


def handle_delete():
    return "执行删除操作"


actions = {"add": handle_add, "delete": handle_delete}
cmd = "add"
print(actions[cmd]())  # 执行添加操作 actions[add]() → handle_add()


# 模拟命令行工具
def do_add():
    return "执行添加操作"


def do_delete():
    return "执行删除操作"


def do_list():
    return "当前列表为：[1, 2, 3]"


# 命令映射表
commands = {"add": do_add, "delete": do_delete, "list": do_list}
# 用户输入命令
user_input = input("请输入命令（add，delete，list）：")
# 查找并执行命令
if user_input in commands:
    result = commands[user_input]()
    print(result)
else:
    print("无效的命令！")


# 2. 函数 + 列表：批量处理数据
def square(x):
    return x**2


numbers = [1, 2, 3, 4, 5]
squared = [square(x) for x in numbers]
print(squared)  # [1, 4, 9, 16, 25]


# 十二、进阶知识点（了解即可，用到再深究）
# 1. **`nonlocal` 关键字**
# 用于在**嵌套函数**中修改**外层（非全局）变量**
def outer():
    x = 10

    def inner():
        nonlocal x  # 声明要修改外层变量
        x = 30

    inner()
    print(x)


outer()

# ✅ 你之前见过计数器例子，就用到了它。
# ❗ 除非写闭包需要修改外层变量，否则很少用。


# 2. **函数注解（Type Hints）** → **强烈推荐了解！**
# - 给参数和返回值加“类型提示”，提高代码可读性和 IDE 支持
# - **不强制，但现代 Python 项目几乎都用**
def create_useer(name: str, age: int, city: str = "广州") -> dict:
    return {"name": name, "age": age, "city": city}


def add(x: int, y: int) -> int:
    return x + y


# ✅ 虽然 Python 是动态类型，但类型提示能：
# - 让代码更清晰
# - 帮助 IDE 自动补全和错误检查
# - 配合 `mypy` 做静态类型检查

# 3. **Lambda 表达式（匿名函数）**

# - 简短的函数，一行搞定
# - 常用于 `map()`、`filter()`、`sorted()` 等高阶函数


# 普通写法
def square(x):
    return x**2

# lambda 表达式
square_lambda = lambda x: x ** 2

print(square(2))
print(square_lambda(2))

# 实际用途：排序
students = [("Alice", 98), ("Bob", 39), ("Charlie", 71)]
sorted_students = sorted(students, key=lambda x: x[1]) # 按成绩排序
print(sorted_students) #[('Bob', 39), ('Charlie', 71), ('Alice', 98)]

# ✅ 适合**简单、一次性**的函数  
# ❌ 不适合复杂逻辑（可读性差）

# 4. **递归函数（Recursion）**
# - 函数调用自身
# - 适合处理“分治”问题（如树遍历、阶乘、斐波那契）
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
# ⚠️ 注意：Python 有**递归深度限制**（默认 ~1000），大数据用循环更安全。

# 5. **装饰器（Decorator）** → **重要但可后续学**
# - 本质是“包装函数的函数”
# - 用于日志、权限、缓存、计时等**横切关注点**
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"函数{func.__name__} 执行时间：{time.time() - start:.2f} 秒")
        return result
    return wrapper
@timer
def slow_function():
    time.sleep(4)
    return "Done!"

print(slow_function())  # 输出：函数slow_function 执行时间：4.00 秒

# 🔸 装饰器 = 闭包 + 函数作为参数/返回值  
# 你现在已有基础，后续学起来会很快！

# 6. **生成器函数（`yield`）** → 属于“生成器”专题
# - 用 `yield` 替代 `return`，返回一个**生成器对象**
# - 节省内存，适合大数据流

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 3
for num in count_up_to(9):
    print(num) 
# 这通常和“迭代器”一起学，不属于函数基础范畴。