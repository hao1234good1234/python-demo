"""
类型转换（int(), str(), float()）→ 在不同数据类型间切换
"""

# | 函数      | 作用       | 示例                                        | 说明                         |
# | --------- | ---------- | ------------------------------------------ | -----------------------------|
# | `int()`   | 转为整数   | `int("42") → 42`   `int(3.9) → 3`           | 小数直接截断（非四舍五入）     |
# | `float()` | 转为浮点数 | `float("3.14") → 3.14`     `float(5) → 5.0` | 字符串必须是合法数字           |
# | `str()`   | 转为字符串 | `str(100) → "100"`     `str(True) → "True"` | 万能！任何类型都能转           |

"""
1. int() —— 转整数
"""
print(int("123"))  # 123
print(int(45.9))  # 45
print(int(-3.7))  # -3
print(int(True))  # 1
print(int(False))  # 0

# ❌ 会报错的情况：
# int("3.14")   → ValueError（不能直接转带小数点的字符串）
# int("abc")    → ValueError

print(int(float("3.14159")))  # 3，先转 float 再转 int

"""
2. float() —— 转小数
"""
print(float("3.14159"))  # 3.14159
print(float("10"))  # 10.0
print(float(5))  # 5.0
print(float(-2))  # -2.0
print(float(True))  # 1.0
print(float(False))  # 0.0

# ❌ 报错：
# float("hello") → ValueError

"""
3. str() —— 转字符串（最安全！）
"""

print(str(100))  # "100"
print(str(3.14))  # "3.14"
print(str(True))  # "True"
print(str(None))  # "None"
print(str([1, 2, 3]))  # "[1, 2, 3]"
print(str({"a": 1}))  # "{'a': 1}"
print(str((4, 5)))  # "(4, 5)"
print(str({"name": "Alice", "age": 30}))  # "{'name': 'Alice', 'age': 30}"
print(str({1, 2, 3}))  # "{1, 2, 3}"
print(str(len))  # "<built-in function len>"
print(str(print))  # "<built-in function print>"
print(str(int))  # "<class 'int'>"
print(str(float))  # "<class 'float'>"
print(str(str))  # "<class 'str'>"
print(str(type(123)))  # "<class 'int'>"
print(str(type("abc")))  # "<class 'str'>"
print(str(type(3.14)))  # "<class 'float'>"
print(str(type(True)))  # "<class 'bool'>"
print(str(type(None)))  # "<class 'NoneType'>"
print(str(type([1, 2, 3])))  # "<class 'list'>"
print(str(type({"a": 1})))  # "<class 'dict'>"
print(str(type((4, 5))))  # "<class 'tuple'>"
print(str(type({1, 2, 3})))  # "<class 'set'>"
print(str(type(len)))  # "<class 'builtin_function_or_method'>"
print(str(type(print)))  # "<class 'builtin_function_or_method'>"
print(str(type(int)))  # "<class 'type'>"
print(str(type(float)))  # "<class 'type'>"
print(str(type(str)))  # "<class 'type'>"
print(str(type(type)))  # "<class 'type'>"
# ✅ 几乎不会报错！任何对象都能转成字符串


"""
三、自动类型转换（隐式转换）
"""
# Python 有时会自动转换类型，但规则有限：
# ✅ 只在数字类型间发生：
# ❌ 不会自动转字符串和数字：
# 📌 记住：字符串和数字之间的转换必须手动！

print(5 + 3.2)  # 8.2，int + float → float
print(True + 10)  # 11，bool + int → int


"""
错误场景
"""
# | 错误场景         | 报错信息                                | 解决方案                                      |
# | ---------------- | --------------------------------------- | --------------------------------------------- |
# | `int("3.14")`    | `ValueError: invalid literal for int()` | 先 `float()` 再 `int()`                       |
# | `int(" 42 ")`    | ❌（带空格）                             | 先 `.strip()`：`int(" 42 ".strip())`          |
# | `float("1,000")` | ❌（千分位逗号）                         | 先去掉逗号：`float("1,000".replace(",", ""))` |
# | `str(123) + 456` | ❌                                       | 先全转字符串，或全转数字                      |

print(int(float("3.25")))  # 3，先转 float 再转 int
print(int("34.14".strip().split(".")[0]))  # 34，先去空格再取整数部分
print(int("  69  ".strip()))  # 69
print(float("1,345.69".replace(",", "")))  # 1345.69
print(str(123) + str(456))  # "123456"


# 实际开发中，用户输入通常是字符串，需转换类型
# 安全转换：用 try-except 捕获异常
user_input = input("请输入一个数字：")  # input() 总是返回字符串！

# 安全转整数
try:
    num = int(user_input)
    print(f"你输入的数字是{num}")
except ValueError:
    print("输入无效， 请输入合法数字")

"""
实战：计算 BMI（身体质量指数）
"""
# 1. 获取用户输入
height_str = input("请输入你的身高（米）：")  # 例如 1.75
weight_str = input("请输入你的体重（公斤）：")  # 例如 68

# 2. 转换为浮点数
height = float(height_str)
weight = float(weight_str)

# 3. 计算 BMI
bmi = weight / (height**2)

# 4. 输出结果
print("您的 BMI 是:", round(bmi, 2))  # 保留两位小数
# 或用 f-string（更推荐）：
print(f"您的 BMI 是：{bmi:.2f}")  # 保留两位小数


'''
动手练习
'''

# 1. 字符串转数字计算
price = "99.9"
quantity = "5"
total_cost = float(price) * int(quantity)
print(f"总价是：{total_cost}")

# 2. 数字转字符串拼接
year = 2025
message = "新年快乐，欢迎来到 " + str(year) + " 年！"
print(message)

# 3.安全输入整数
user_age = input("请输入你的年龄：")
try:
    age = int(user_age)
    print("5年后你", age + 5, "岁")
except ValueError:
    print("请输入合法的整数年龄")