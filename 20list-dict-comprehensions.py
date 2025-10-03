"""
列表/字典推导式

💡 它们能让你用 **1 行代码** 完成原本需要 **3~5 行循环 + 条件判断** 的任务！
"""
# 二、列表推导式（List Comprehension）

# 基本语法：
# [表达式 for 变量 in 可迭代对象]

# 示例：
# 1. 平方数
squares = [x ** 2 for x in range(1, 6)]
print(squares)  #  [1, 4, 9, 16, 25]

# 2. 提取名字长度
names = ["Alice", "Bob", "Charlie"]
lengths = [len(name) for name in names]
print(lengths)  # [5, 3, 7]

# 3. 字符串转大写
upper_names = [name.upper() for name in names]
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

# 🔸 加条件过滤（if）
# [表达式 for 变量 in 可迭代对象 if 条件]

# 示例
# 只取偶数
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

#名字长度大于4的转大写
long_upper_names = [name.upper() for name in names if len(name) > 4]
print(long_upper_names)  # ['ALICE', 'CHARLIE']

# ⚠️ 注意：`if` 写在 **最后**，用于**过滤输入**。

#  多层循环（嵌套）
# 生成所有 (x, y) 组合，x∈[1,2], y∈[a,b]
points = [(x, y) for x in [1, 2] for y in ['a', 'b']]
print(points)  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# 三、字典推导式（Dict Comprehension）
# 基本语法：
# {key_expr: value_expr for 变量 in 可迭代对象}

# 示例：
# 1. 数字 → 平方
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2. 反转字典（key ↔ value）
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {value: key for key, value in original.items()}
print(reversed_dict)  # {1: 'a', 2: 'b', 3: 'c'}

# 3. 过滤 + 转换
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
high_scores = {name: score for name, score in scores.items() if score >= 80}
print(high_scores)  # {'Alice': 85, 'Bob': 92} 

#  四、实战场景（你马上能用！）
# 场景 1：从文件读取行，去掉空白行
# 传统写法
lines = []
with open("hello.txt", "r", encoding="utf-8") as f:
    for line in f:
        stripped = line.strip()
        if stripped:
            lines.append(stripped)
print(lines)

# 列表推导式
with open("hello.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]
print(lines)

# 场景 2：生成配置映射
# 从列表生成 {name: id} 映射
users = ["Alice", "Bob", "Charlie"]
user_name_ids = {name: index for index, name in enumerate(users, start=1)}
print(user_name_ids)  # {'Alice': 1, 'Bob': 2, 'Charlie': 3}
# - 💡 **`enumerate()` 把一个可迭代对象（如列表）变成「索引 + 元素」的组合。**
# - 📌 **口诀：`enumerate` 返回 `(索引, 值)`，所以 `for 索引, 值 in enumerate(...)`**


# 场景 3：数据清洗（结合字符串方法）
raw_emails = [" Alice@EXAMPLE.com ", "bob@gmail.com\n", "  "]
clean_emails = [email.strip().lower() for email in raw_emails if email.strip()]
print(clean_emails)  # ['alice@example.com', 'bob@gmail.com']

#  五、什么时候**不要用**推导式？
# 虽然推导式很强大，但**可读性优先**！

# ### ❌ 避免复杂逻辑：
# 太复杂！难读
# result = [transform(x) for x in data if x > 0 and x % 2 == 0 and not is_special(x)]


# ✅ 改用普通循环：
# result = []
# for x in data:
#     if x > 0 and x % 2 == 0 and not is_special(x):
#         result.append(transform(x))

# ✅ **经验法则：**  
# - 如果一行超过 80 个字符，或包含多个 `and/or`  
# - 或者需要调试（打 `print`）  
#   → 用普通 `for` 循环！

# 🧩 六、其他推导式（扩展）
# 1. 集合推导式（Set Comprehension）
unique_lengths = {len(name) for name in names}
print(unique_lengths)
# → {3, 5, 7}

# 2. 生成器表达式（Generator Expression）
# 括号 () 而不是 []
gen = (x**2 for x in range(10))
print(type(gen))
# 节省内存！适合大数据

# 七、最佳实践总结
# | 场景        | 推荐写法                            |
# | ----------- | ----------------------------------- |
# | 简单映射    | `[x*2 for x in nums]`               |
# | 过滤 + 映射 | `[x for x in nums if x > 0]`        |
# | 字典构建    | `{k: v*2 for k, v in data.items()}` |
# | 复杂逻辑    | 用普通 `for` 循环                   |
# | 大数据处理  | 用生成器 `(x for x in big_data)`    |

# 🎯 八、小练习（试试看！）
# 1. 生成 [1, 4, 9, 16, 25]（1~5 的平方）
# 2. 从 ['apple', 'banana', 'cherry'] 提取首字母 → ['a', 'b', 'c']
# 3. 过滤出偶数并平方：[0, 1, 2, 3, 4, 5] → [0, 4, 16]
# 4. 字典推导：{'a': 1, 'b': 2} → {'A': 1, 'B': 2}
# 5. 反转字典：{'x': 10, 'y': 20} → {10: 'x', 20: 'y'}

# 1
[x**2 for x in range(1, 6)]

# 2
[word[0] for word in ['apple', 'banana', 'cherry']]

# 3
[x**2 for x in range(6) if x % 2 == 0]

# 4
{k.upper(): v for k, v in {'a': 1, 'b': 2}.items()}

# 5
{v: k for k, v in {'x': 10, 'y': 20}.items()}