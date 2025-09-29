"""
Python 有4种主流字符串格式化方式，但 f-string 是首选！
"""

# | 方式                      | 示例                      | 评价                     |
# | ------------------------- | ------------------------- | ------------------------ |
# | 1. f-string（推荐 ✅）    | `f"Hello {name}"`         | **简洁、高效、可读性强** |
# | 2. .format()             | `"Hello {}".format(name)` | 灵活，但稍啰嗦           |
# | 3. % 格式化               | `"Hello %s" % name`       | 老旧，不推荐             |
# | 4. 字符串拼接             | `"Hello " + name`         | 仅适合简单场景           |

# f-string 详细教程（Python 3.6+）
# 基本语法：
# f"普通文本 {变量名} 普通文本"

name = "小明"
age = 18
height = 1.75

print(f"我叫{name}，今年{age}岁，身高{height}米。")


# ✅ f-string 的强大功能
# 1. **直接写表达式**

x, y = 3, 4
print(f"{x} + {y} = {x + y}") # 直接计算表达式 

# 2. **调用函数**
name = "    ALICE   "
print(f"你好，{name.strip().title()}!") # 调用字符串函数

# 3. **格式化数字（重点！）**

# | 需求        | 语法          | 示例                                 |
# | ----------- | ------------- | ------------------------------------ |
# | 保留2位小数 | `{value:.2f}` | `f"价格: {9.876:.2f}" → "9.88"`      |
# | 百分比      | `{value:.1%}` | `f"成功率: {0.85:.1%}" → "85.0%"`    |
# | 千分位      | `{value:,}`   | `f"人口: {1234567:,}" → "1,234,567"` |
# | 对齐        | `{value:>10}` | 右对齐10字符                         |

price = 1234.5678
rate = 0.8754
population = 1234567

print(f"商品价格：{price:.2f} 元")   # 保留2位小数 1234.57
print(f"折扣率：{rate:.2%}")     # 百分比 87.54%
print(f"城市人口：{population:,}") # 千分位 1,234,567
print(f"对齐示例：|{price:>10.2f}|") # 右对齐10字符 |   1234.57|
print(f"对齐示例：|{price:<10.2f}|") # 左对齐10字符 |1234.57   |
print(f"对齐示例：|{price:^10.2f}|") # 居中对齐10字符 | 1234.57  |
print(f"对齐示例：|{price:=^10.2f}|") # 居中对齐10字符，填充= |=1234.57==|
print(f"对齐示例：|{price:*^10.2f}|") # 居中对齐10字符，填充* |*1234.57**|
print(f"对齐示例：|{price:-^10.2f}|") # 居中对齐10字符，填充- |-1234.57--|

# 4. **嵌套 f-string（Python 3.12+）**
# f-string 里还能嵌套 f-string（需要 Python 3.12+ 支持）


name = "alice"
print(f"你好，{f'{name.strip().title()}'}!") # 调用字符串函数 输出：你好，Alice!

# 5. **多行 f-string**
name = "小明"
age = 19
score = 95.5

message = f"""
考试成绩报告
--------------------
姓名：{name}
年龄：{age} 岁
等级：{"优秀" if score >= 90 else "良好"}
"""
print(message)


# 6. **调试输出（Python 3.8+）**
x = 42
print(f"{x=}, {x*2=}, {x**2=}") # 输出变量名和值 x=42, x*2=84, x**2=1764

# 7. **避免转义**
path = r"C:\Users\Alice\Documents"
print(f"文件路径：{path}") # 输出：文件路径：C:\Users\Alice\Documents


# 8. **嵌入 Unicode 字符**
heart = "\u2764"
print(f"我{heart}Python!") # 输出：我❤️Python!

# 9. **结合三引号实现复杂格式**
name = "小红"
age = 20
bio = f"""个人简介
姓名：{name}
年龄：{age} 岁
爱好：编程、阅读、旅行
"""
print(bio)

# 10. **与字典结合使用**
user = {"name": "小刚", "age": 22}
print(f"用户信息：姓名 - {user['name']}, 年龄 - {user['age']} 岁")

# 11. **与列表结合使用**
fruits = ["苹果", "香蕉", "橘子"]
print(f"我喜欢的水果有：{', '.join(fruits)}") # 输出：我喜欢的水果有：苹果, 香蕉, 橘子

# 12. **与枚举结合使用**
colors = ["红色", "绿色", "蓝色"]
for i, color in enumerate(colors, 1):
    print(f"颜色 {i}: {color}")
# 输出：
# 颜色 1: 红色
# 颜色 2: 绿色
# 颜色 3: 蓝色

# 13. **与日期时间结合使用**
from datetime import datetime
now = datetime.now()
print(f"当前时间：{now:%Y-%m-%d %H:%M:%S}") # 输出：当前时间：2024-06-27 12:34:56

# 14. **与自定义类结合使用**
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  
    def __str__(self):
        return f"姓名：{self.name}, 年龄：{self.age} 岁"
p = Person("小李", 25)
print(f"个人信息：{p}") # 输出：个人信息：小李, 25 岁

# 15. **嵌套数据结构**
data = {"user": {"name": "小王", "age": 30}, "scores": [95, 88, 76]}
print(f"用户：{data['user']['name']}，年龄：{data['user']['age']} 岁，成绩：{data['scores']}")
# 输出：用户：小王，年龄：30 岁，成绩：[95, 88, 76]

# 16. **条件表达式**
score = 85
grade = "优秀" if score >= 90 else "良好" if score >= 75 else "及格" if score >= 60 else "不及格"
print(f"成绩：{score}，等级：{grade}") # 输出：成绩：85，等级：良好

# 17. **复杂表达式**
a, b = 5, 10
print(f"{a} 的平方是 {a**2}，{b} 的平方是 {b**2}，它们的和是 {a**2 + b**2}")
# 输出：5 的平方是 25，10 的平方是 100，它们的和是 125

# 18. **嵌套函数调用**
def greet(name):
    return f"Hello, {name}!"
print(f"{greet('小明')} 欢迎来到 Python 世界！") # 输出：Hello, 小明! 欢迎来到 Python 世界！

# 19. **使用 f-string 构建 SQL 查询**
table = "users"
column = "name"
value = "小张"
query = f"SELECT * FROM {table} WHERE {column} = '{value}'"
print(query) # 输出：SELECT * FROM users WHERE name = '小张' 

# 20. **动态生成 HTML 代码**
title = "欢迎"
body = "这是一个使用 f-string 生成的 HTML 页面。"
html = f"""
<html>
<head><title>{title}</title></head>
<body><h1>{title}</h1><p>{body}</p></body>
</html>
"""
print(html)
# 输出：
# <html>
# <head><title>欢迎</title></head>
# <body><h1>欢迎</h1><p>这是一个使用 f-string 生成的 HTML 页面。</p></body>
# </html>

# 21. **生成配置文件内容**
host = "localhost"
port = 8080
config = f"""
[server]
host = {host}
port = {port}
"""
print(config)
# 输出：
# [server]
# host = localhost
# port = 8080

# 22. **调试复杂数据结构**
data = {"users": [{"name": "小明", "age": 18}, {"name": "小红", "age": 19}]}
print(f"用户数据：{data=}") # 输出：用户数据：data={'users': [{'name': '小明', 'age': 18}, {'name': '小红', 'age': 19}]}

# 23. **与正则表达式结合使用**
import re
pattern = r"\b\w{3}\b"
text = "The cat sat on the mat."
matches = re.findall(pattern, text)
print(f"三字母单词：{', '.join(matches)}") # 输出：三字母单词：The, cat, sat, the, mat

# 24. **与枚举类结合使用**
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
favorite = Color.GREEN
print(f"我最喜欢的颜色是 {favorite.name}，值为 {favorite.value}") # 输出：我最喜欢的颜色是 GREEN，值为 2

# 25. **与数据分析结合使用**
# import pandas as pd
# data = {'Name': ['小明', '小红', '小刚'], 'Score': [95, 88, 76]}
# df = pd.DataFrame(data)
# print(f"数据表内容：\n{df}")
# # 输出：
# # 数据表内容：
# #   Name  Score
# # 0  小明     95
# # 1  小红     88
# # 2  小刚     76

# 26. **与 JSON 数据结合使用**
import json
data = {"name": "小明", "age": 18, "scores": [95, 88, 76]}
json_str = json.dumps(data, ensure_ascii=False, indent=2)   
print(f"JSON 数据：\n{json_str}")
# 输出：    
# JSON 数据：
# { 
#   "name": "小明",
#   "age": 18,
#   "scores": [95, 88, 76]
# }

# 27. **与文件操作结合使用**
# filename = "data.txt"
# with open(filename, "w", encoding="utf-8") as f:
#     content = f"文件名：{filename}\n创建时间：{datetime.now():%Y-%m-%d %H:%M:%S}\n"
#     f.write(content)
# print(f"已写入文件 {filename} 的内容：\n{content}")
# # 输出：
# # 已写入文件 data.txt 的内容：
# # 文件名：data.txt
# # 创建时间：2024-06-27 12:34:56


# 28.截取长字符串
long_text = "Hello World"
print(f"{long_text:.5}")  # Hello (最多5个字符)

# 29.花括号转义
name = "Alice"
print(f"{{name}} 的值是{name}")  # {name} 的值是Alice

# 30.安全输出 （带转义）
key = "password"
value = "123456"
print(f"{{'{key}' : '{value}'}}")  # {'password' : '123456'}

