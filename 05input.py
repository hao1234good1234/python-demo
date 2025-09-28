'''
计算年龄
'''
# 1. 获取输入
birth_year_str = input("请输入你的出生年份: ")

# 2. 转为整数
birth_year = int(birth_year_str)

# 3. 计算年龄
current_year = 2025
age = current_year - birth_year

# 4. 输出结果
print(f"你今年 {age} 岁。")

'''
安全输入整数
'''
while True:
    user_input = input("请输入一个整数: ")
    try:
        number = int(user_input)
        break  # 输入成功，跳出循环
    except ValueError:
        print("❌ 输入无效！请输入一个整数。")

print("你输入的数字是:", number)

'''
简易计算器
'''

print("=== 简易加法计算器 ===")

# 获取两个数字
num1 = float(input("请输入第一个数字: "))
num2 = float(input("请输入第二个数字: "))

# 计算
result = num1 + num2

# 输出
print(f"{num1} + {num2} = {result}")


'''
动手练习
'''
# 练习 1：问候程序
name = input("你的名字？")
print(f"Hello, {name}! 欢迎来到 Python 世界！")

# 练习 2：温度转换（摄氏 → 华氏）
celsius = float(input("请输入摄氏温度: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")

# 练习 3：安全输入年龄（带错误处理）
while True:
    age_str = input("请输入你的年龄（整数）: ")
    try:
        age = int(age_str)
        if age < 0:
            print("年龄不能为负数！")
            continue
        break
    except ValueError:
        print("请输入有效的数字！")

print(f"你输入的年龄是: {age} 岁")