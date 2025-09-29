"""
条件语句  `if` / `elif` / `else`  控制程序分支
"""

# 1. 最简单的 `if`

# if 条件:
#     执行语句（缩进！）
age = 20 
if age >= 18:
    print("你已经成年，可以上网")

# 2. `if-else`：二选一

# if 条件:
#     条件为 True 时执行
# else:
#     条件为 False 时执行
score = 63
if score >= 60:
    print("通过考试")
else:
    print("考试不及格，需要重修")

# 3. `if-elif-else`：多选一（重点！）

# if 条件1:
#     执行A
# elif 条件2:     # elif = else if
#     执行B
# elif 条件3:
#     执行C
# else:
#     全都不满足时执行D

score = 88
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"你的成绩是：{score}, 等级是：{grade}")
# 注意：
# - 从上到下**依次判断**
# - **一旦某个条件为 True，执行对应代码块，然后跳出整个 if 结构**
# - `elif` 和 `else` 都是可选的，但 `if` 必须有


"""
条件表达式（真值判断）
"""

# 条件可以是任何**返回布尔值**的表达式

# 1. 比较运算（`==`, `!=`, `>`, `<`, `>=`, `<=`）
temperature = 40
if temperature > 30:
    print("今天天气很热！")

# 2. 逻辑运算（`and`, `or`, `not`）
age = 39
if age >= 18 and age < 60:
    print("符合劳动年龄")

is_student = True
has_discount_card = False
if is_student or has_discount_card:
    print("你可以享受折扣")

# 3. 成员判断（`in`, `not in`）
username = "admin11"
if "admin" in username:
    print("你是管理员")

char = "y"
if char not in "aeiou":
    print(f"{char} 不是元音字母")

# 4. 空值/真假判断（Python 的“真值测试”）

# Python 中以下值被视为 False，其余为 True：
# - False
# - None
# - 0, 0.0
# - 空字符串 ""
# - 空列表 []、空字典 {} 等

name = input("请输入你的名字：")
if name.strip():   # 去除前后空格后判断是否为空，等同于 if name.strip() != ""
    print(f"你好，{name}")
else:
    print("你没有输入名字")


"""
实战项目：简易登录系统
"""

print("===用户登录===")
# 预设用户名密码
correct_username = "admin"
correct_password = "123456"

# 获取用户输入
username = input("用户名：")
password = input("密码：")

# 判断登录
if username == correct_username and  password == correct_password:
    print("登录成功！欢迎回来！")
elif username == correct_username:
    print("密码错误！")
elif password == correct_password:
    print("用户名错误！")
else:
    print("用户名和密码都错误！")


"""
条件表达式（三元运算符）
"""
score = 89
result = "通过" if score >= 60 else "失败"
print(f"考试结果：{result}")

# 用在f-string中
print(f"考试结果：{'通过' if score >= 60 else '失败'}")

"""
动手练习
"""

# 练习1：判断奇偶数
num = int(input("请输入一个整数："))
if num % 2 == 0:
    print(f"{num} 是偶数")
else:
    print(f"{num} 是奇数")

# 练习2：BMI健康展示
height = float(input("身高（米）: "))
weight = float(input("体重（公斤）: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    status = "偏瘦"
elif bmi < 24:
    status = "正常"
elif bmi < 28:
    status = "超重"
else:
    status = "肥胖"

print(f"你的 BMI 是 {bmi:.1f}，属于 {status} 范围。")

# 练习3：根据月份判断季度
month = int(input("请输入月份（1-12）："))
if month in [12, 1, 2]:
    season = "冬季"
elif month in [3, 4, 5]:
    season = "春季"
elif month in [6, 7, 8]:
    season = "夏季"
elif month in [9, 10, 11]:
    season = "秋季"
else:
    season = "无效月份"
print(f"{month}月是{season}。")
