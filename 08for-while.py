"""
循环  for循环、while 循环、break/continue
"""

# | 循环类型         | 适用场景                                           | 特点                   |
# | ---------------- | -------------------------------------------------- | ---------------------- |
# | **`for` 循环**   | **已知循环次数** 或 **遍历序列**（如列表、字符串） | 安全、简洁、不易死循环 |
# | **`while` 循环** | **未知循环次数**，根据条件决定是否继续             | 灵活，但需小心死循环   |

'''
一、for循环详解
'''
# 基本语法：
# for 变量 in 可迭代对象:
#   循环体（缩进！）

# 1. 遍历 `range()`（最常用！）
# 打印 0 到 4
for i in range(5):
    print(i)
print("======================")
# 打印 1 到 5
for i in range(1, 6):
    print(i)
print("======================")
# 步长为2 打印 0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print(i)
print("======================")

# 🔸 `range(start, stop, step)`：
# - `start`：起始值（默认 0）
# - `stop`：结束值（**不包含**）
# - `step`：步长（默认 1）

# 2. 遍历字符串
for char in "python":
    print(char)
print("======================")

# 3. 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}!")
print("======================")

# 4. 遍历字典（三种方式）
scores = {"小明": 90, "小红": 85}
# 遍历键
for name in scores:
    print(name)
print("======================")

# 遍历键（显式）
for name in scores.keys():
    print(name)
print("======================")
# 遍历值
for score in scores.values():
    print(score)
print("======================")
# 同时遍历键和值
for name, score in scores.items():
    print(f"{name}: {score}分")
print("======================")

'''
二、`while` 循环详解
'''
# 基本语法：
# while 条件:
#     循环体

# 1. 计数器（类似 for）
i = 0
while i < 5:
    print(i)
    i += 1
print("======================")
