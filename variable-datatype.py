"""
现在进入**变量与数据类型**
下面我为你**系统、清晰、零基础友好**地讲解这一节，包含：
✅ 什么是变量
✅ 常见数据类型（`int`, `float`, `str`, `bool`, `None`）
✅ 如何查看类型
✅ 命名规则与最佳实践
✅ 常见错误避坑
✅ VS Code 小技巧 + 练习题
"""

# | 类型    | 中文名         | 示例                           | 说明                                   |
# | ------- | -------------- | ------------------------------ | -------------------------------------- |
# | `int`   | 整数           | `42`, `-5`, `0`                | 没有小数点                             |
# | `float` | 浮点数（小数） | `3.14`, `-0.5`, `2.0`          | 有小数点，哪怕 `.0`                    |
# | `str`   | 字符串         | `"Hello"`, `'Python'`, `"123"` | **用引号包裹**，可以是字母、数字、符号 |
# | `bool`  | 布尔值         | `True`, `False`                | **只有两个值**，首字母大写！           |
# | `None`  | 空值           | `None`                         | 表示“什么都没有”，常用于初始化         |

"""
常见数据类型
"""
# 1. int（整数） ✅ 支持任意大小整数（不像其他语言有溢出限制）
score = 100
temperature = -10
count = 0

# 2. float（小数） ⚠️ 注意：`2` 是 `int`，`2.0` 是 `float`！
price = 9.99
pi = 3.1415926
rate = -0.05

# 3. str（字符串）✅ 引号可以用单引号 `'` 或双引号 `"`，但**不能混用**
name = "Alice"
message = "Hello, World!"
number_as_str = "123"

# 4. bool（布尔值）✅ **必须大写**：`True` / `False`（不是 `true` / `false`！）
is_raining = True
has_permission = False

# 5. None（空值）✅ 常用于函数没有返回值时，或初始化变量
result = None
user_input = None  # 表示“用户还没输入”

"""
如何查看变量的类型
💡 小技巧：在 VS Code 调试时，鼠标悬停变量也能看到类型！
"""
print(type(score))  # <class 'int'>
print(type(price))  # <class 'float'>
print(type(name))  # <class 'str'>
print(type(is_raining))  # <class 'bool'>
print(type(result))  # <class 'NoneType'>

print(type(58))
print(type(3.15))
print(type("Hello"))
print(type(True))
print(type(None))


"""
命名规则与最佳实践
"""
# ✅ 合法命名：
# 只能包含：字母（a-z, A-Z）、数字（0-9）、下划线 _
# 不能以数字开头
# 区分大小写（name 和 Name 是两个变量）
# 不能是关键字（如 if, for, True 等）

# 📌 命名风格建议（PEP8 规范）：
# 变量名用小写 + 下划线：student_name, total_price
# 不要用中文变量名（虽然 Python 3 支持，但不推荐）
# 名字要有意义：用 user_age 而不是 a
# 常量用全大写：MAX_SIZE, DEFAULT_COLOR


user_name = "Tom"
age2 = 25
_is_valid = True
PI = 3.14159  # 常量用全大写

"""
类型提示
💡 可选，但推荐使用，能提升代码可读性和维护性
"""
name: str = "Alice"
age: int = 30
is_active: bool = True
height: float = 5.9
data: None = None  # 这种写法不常见

"""
动手练习
"""
# 1、创建不同类型的变量
name = "小明"
age = 18
height = 1.72
is_student = True
favorite_subject = None

# 2、打印变量和类型
print("姓名：", name, type(name))
print("年龄：", age, type(age))
print("身高：", height, type(height))
print("是否学生：", is_student, type(is_student))
print("喜欢的科目：", favorite_subject, type(favorite_subject))

# 3、尝试一些非法命名，观察错误信息
# print("年龄是：" + age)  # 错误：不能把 str 和 int 直接拼接
print("年龄是：" + str(age))  # 错误：不能把 str 和 int 直接拼接

num1: str = "14"
num2: int = 5
print(int(num1) + num2)  # 正确：先把 int 转 str，再拼接


# 变量重命名：  
# 选中变量名 → 按 `F2` → 输入新名字 → 自动修改所有引用！