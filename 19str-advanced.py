"""
字符串高级操作 切片、方法（.split(), .join(), .replace()）

- ✂️ **切片（Slicing）**：精准提取子串
- 🔀 **`.split()` / `.join()`**：文本 ↔ 列表的双向转换
- 🔄 **`.replace()` / `.strip()` / `.format()`**：替换、清洗、格式化
"""

# 🧱 一、字符串切片（Slicing）—— 精准“切蛋糕”
# 基础语法：
# s[start:end:step]
# | 参数    | 说明               | 默认值     |
# | ------- | ------------------ | ---------- |
# | `start` | 起始索引（包含）   | 0          |
# | `end`   | 结束索引（不包含） | 字符串长度 |
# | `step`  | 步长（可负数）     | 1          |

# 实战示例：
text = "Python编程很有趣"
# 1.基本切片
print(text[0:6])  # 输出：Python
print(text[:6])  # 输出：Python
print(text[6:])  # 输出：编程很有趣

# 2. 负索引（从后往前）
print(text[-3:])  # 输出：很有趣
print(text[:-3])  # 输出：Python编程

# 3. 步长（每隔一个字符）
print(text[::2])  # 输出：Pto编很趣

# 4. 逆序（经典！）
print(text[::-1])  # 输出：趣有很程编nohtyP

# 5.切片不会报错，只会返回空字符串
print("["+text[30:]+"]")  # 输出：空字符串
# ✅ **技巧：**  
# `s[::-1]` 是 Python 中**最简洁的字符串反转方法**  
# 切片不会报错！`"abc"[10:]` 返回空字符串，而不是异常

# 二、`.split()` 和 `.join()` —— 文本与列表的“双向门”
# 1. `.split(sep)`：**字符串 → 列表**
# 默认分割（按空白）
# "apple banana cherry".split()
# → ['apple', 'banana', 'cherry']

# 按逗号分割
# "张三,李四,王五".split(",")
# → ['张三', '李四', '王五']

# 限制分割次数
# "a=b=c=d".split("=", 2)
# → ['a', 'b', 'c=d']

# 实战示例：
# 1.默认分割
str = "apple banana cherry"
L_str = str.split()
print(L_str)  # ['apple', 'banana', 'cherry']

# 2. 按照逗号分割
str = "Alice, Bob, Charlie"
L_str = str.split(",")
print(L_str)  # ['Alice', ' Bob', ' Charlie']

# 3.限制分割次数
str = "a=b=c=d"
L_str = str.split("=", 2)
print(L_str)  # ['a', 'b', 'c=d']
# ⚠️ 注意：`split()` 会**自动去除空字符串**吗？  
# ❌ 不会！`"a,,b".split(",")` → `['a', '', 'b']`  
# ✅ 如果要去掉空项：`[x for x in s.split(",") if x]`


# 2. `.join(iterable)`：**列表 → 字符串**
# - **必须用字符串调用**！
# - 效率远高于 `+` 拼接（尤其大数据量）

# 用空格连接
words = ["Python", "is", "awesome"]
print(" ".join(words))  #  Python is awesome

# 用其他符号连接
words = ["138", "0000", "1111"]
print(",".join(words))  # 138,0000,1111

# 甚至可以“无分隔符”连接
words = ['h','e','l','l','o']
print(''.join(words))  # hello

# ✅ **黄金法则：**  
# **“用分隔符去 join 列表”**，而不是“用 + 拼接字符串”

# 🔄 三、常用字符串方法（高频实战）

# | 方法                            | 作用                          | 示例                                    |
# | ------------------------------- | ----------------------------- | --------------------------------------- |
# | `.replace(old, new)`            | 替换子串                      | `"abc".replace("a", "A")` → `"Abc"`     |
# | `.strip()`                      | 去除首尾空白                  | `"  hello  ".strip()` → `"hello"`       |
# | `.lstrip()` / `.rstrip()`       | 去左/右空白                   | `"!!hello!!".rstrip("!")` → `"!!hello"` |
# | `.upper()` / `.lower()`         | 大小写转换                    | `"Hello".lower()` → `"hello"`           |
# | `.startswith()` / `.endswith()` | 判断开头/结尾                 | `"file.txt".endswith(".txt")` → `True`  |
# | `.find(sub)`                    | 查找子串位置（找不到返回 -1） | `"hello".find("e")` → `1`               |
# | `.index(sub)`                   | 同 `find`，但找不到会报错     | `"hello".index("x")` → `ValueError`     |

print("abc".replace("a", "A"))  # Abc

print("    hello    ".strip())  # hello
print("!!hello!!".rstrip("!"))  # !!hello
print("!!hello!!".lstrip("!"))  # hello!!

print("hello".upper())  # HELLO
print("HELLO".lower())  # hello
print("Hello".lower())  # hello

print("file.txt".endswith(".txt"))  # True
print("application.properties".startswith("application"))  # True

print("hello".find("e"))  # 1
print("hello".find("w"))  # -1

print("hello".index("e"))  # 1
# print("hello".index("w"))  # ValueError

# 🧪 四、实战场景：日志清洗 & 数据提取
# 场景：处理一行日志
# 2025-10-02 14:30:00 [INFO] User login: 张三 (ID:1001)

# 目标：提取用户名和 ID
log = "2025-10-02 14:30:00 [INFO] User login: 张三 (ID:1001)"

# 方法1：用 split 逐步拆解
str1 = log.split(": ")
str2 = str1[1].split(" (")
print(str2[0])  #   张三

# 方法2：用 replace + split
clean = log.replace(" (ID:", ",").replace(")", "")
# → "2025-10-02 14:30:00 [INFO] User login: 张三,1001"
name, user_id = clean.split(",")[0][-2:], clean.split(",")[1]
print(name)
print(user_id)
# ✅ 这就是真实项目中的字符串处理！

# 五、格式化字符串（Bonus）
# 虽然你还没学 f-string，但这里提一下更现代的方式：
name = "小明"
age = 18

# 旧方式（不推荐）
"{} 今年 {} 岁".format(name, age)

# 新方式（推荐！）
f"{name} 今年 {age} 岁"
# **f-string 更快、更简洁、更易读！**  
# 你可以在学完字符串方法后，立刻用它！

# 📌 六、最佳实践总结
# | 场景              | 推荐做法                                                     |
# | ----------------- | ------------------------------------------------------------ |
# | **分割文本**      | 用 `.split(sep)`，明确分隔符                                 |
# | **拼接字符串**    | 用 `"分隔符".join(list)`，不用 `+`                           |
# | **去除空白**      | 用 `.strip()`，别手写循环                                    |
# | **替换内容**      | 用 `.replace()`，支持链式调用：<br>`s.replace("a", "A").replace("b", "B")` |
# | **反转字符串**    | 用 `s[::-1]`                                                 |
# | **检查前缀/后缀** | 用 `.startswith()` / `.endswith()`，比切片更清晰             |


