"""
循环  for循环、while 循环、break/continue
"""

# | 循环类型         | 适用场景                                           | 特点                   |
# | ---------------- | -------------------------------------------------- | ---------------------- |
# | **`for` 循环**   | **已知循环次数** 或 **遍历序列**（如列表、字符串） | 安全、简洁、不易死循环 |
# | **`while` 循环** | **未知循环次数**，根据条件决定是否继续             | 灵活，但需小心死循环   |



## `for` vs `while` 使用建议

# | 场景                         | 推荐循环                 |
# | ---------------------------- | ------------------------ |
# | 遍历列表、字符串、字典       | ✅ `for`                  |
# | 已知循环次数（如 10 次）     | ✅ `for` + `range()`      |
# | 未知次数，依赖用户输入或条件 | ✅ `while`                |
# | 实现“菜单”或“重试”逻辑       | ✅ `while True` + `break` |


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
# `range()` 理解错误`range(5)` 是 0~4，不是 1~5记住：**左闭右开**


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

# 2. 用户输入直到有效
password = ""
while password != "123456":
    password = input("请输入密码：")
print("登录成功！")
print("======================")

# 3. 猜数字游戏
# import random
# target = random.randint(1, 100) 
# guess = 0
# while guess != target:
#     guess = int(input("请猜一个1-100的数字："))
#     if guess < target:
#         print("太小了")
#     elif guess > target:
#         print("太大了")
# print("恭喜你，你猜中了！")
# print("======================")

# ⚠️ 致命陷阱：忘记更新循环条件 → 死循环！

# 💡 建议：while 循环中一定要有改变条件的语句（如 i += 1 或 input()）

'''
三、循环控制：`break` 和 `continue`
'''
# 1. break：立即退出整个循环
for i in range(10):
    if i == 5:
        break
    print(i)
print("======================")
#  用途：提前结束循环（如找到目标就停止搜索）

# 2. continue：跳过本次循环，进入下一次
for i in range(5):
    if i == 2:
        continue
    print(i)
print("======================")

'''
用户菜单
'''
money = 1000.0
while True:
    print("===主菜单===")
    print("1. 查看金额")
    print("2. 存款")
    print("3. 退出")

    choice = input("请选择操作：")
    if choice == '1':
        print(f"余额：{money}元")
    elif choice == '2':
        amount = float(input("请输入存款的金额："))
        money += amount
        print(f"已存入{amount} 元")
    elif choice == '3':
        print("再见")
        break
    else:
        print("无效选项，请重试！")
        continue
print("======================")

'''
实战项目 九九乘法表
'''
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j} x {i} = {i*j}", end="\t")
    print()
print("======================")

'''
动手练习
'''

# 练习1:  计算 1 到 100的和（用for）
total = 0
for i in range(1, 101):
    total += i
print(f"1-100的和是：{total}")
print("======================")

# 练习 2：打印所有偶数（用 while）
print("打印0-20的偶数")
num = 0
while num < 20:
    if num % 2 == 0:
        print(num)
    num += 1
print("======================")

# 练习 3：安全退出循环（用 break）
while True:
    user_input = input("输入 quit 退出：")
    if user_input.lower() == 'quit':
        print("程序结束")
        break
    print(f"你输入了：{user_input}")



