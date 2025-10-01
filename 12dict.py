"""
**字典（dict）** → 键值对存储
"""
# 特点：
# - **通过名字（key）快速访问数据**
# - **动态增删字段**
# - **天然支持结构化数据**（如 JSON）
# **键必须是不可变类型**（字符串、数字、元组）, ❌ 列表、字典不能做键（因为可变，无法哈希）
# 🔸 字典是**可变对象**，所有操作都是**原地修改**！
# ✅ **最佳实践**：通过键获取值，优先用 `.get()` 避免程序崩溃！
# ❌ 不要用 .get() 判断存在性（效率低且不直观）
# ✅ **黄金法则**：用 `key in dict` 判断键是否存在！
# 自 Python 3.7 起，字典保持插入顺序（官方语言规范保证）。


# 二、创建字典
# 1. 基本语法：**花括号 `{}` + 冒号 `:`
# 空字典
empty = {}

# 带数据的字典
student = {"name": "lisi", "score": 90, "is_pass": True}

# 键可以是字符串、数字、元组(不可变类型)
config = {"host": "localhost", 8080: "端口", (0, 0): "原点"}

# ⚠️ **键必须是不可变类型**（字符串、数字、元组）
# ❌ 列表、字典不能做键（因为可变，无法哈希）

# 2. 用 `dict()` 构造函数
# 方式1：关键字参数（键必须是合法标识符）
user = dict(name="zhangsan", age=30)
print(user)
# 方式2：键值对列表
user = dict([("name", "lisi"), ("age", 29)])
print(user)

# 方式3：zip 合并两个列表
keys = ["name", "age", "sex"]
values = ["小明", 29, "男"]
d = dict(zip(keys, values))  # 键值对列表 → { "name": "小明", "age": 29, "sex": "男"}
print(d)

# 🔍 三、访问字典的值
# 1. 通过键访问（最常用）
user = {"name": "zhangsan", "age": 25}
print(user["name"])  # zhangsan
# ❌ 如果键不存在，会报错！
# print(user["email"])  # KeyError: 'email'

# 2. 安全访问：`.get(key, default)`
email = user.get("email", "未填写")
print(email)  # 未填写
score = user.get("score")
print(score)  # None

# **最佳实践**：优先用 `.get()` 避免程序崩溃！

#  四、修改和添加键值对
user = {"name": "李白"}
user["age"] = 100  # 添加新键值对
user["name"] = "杜甫"  # 修改已有键的值
print(user)  # {'name': '杜甫', 'age': 100}
# 批量更新（合并字典）
user.update({"sex": "男", "email": "lisi@example.com"})
print(user)
# 用关键字参数更新
user.update(age=19)
print(user)
# 修改键对应的值
user.update(name="小王")
print(user)
# 🔸 `update()` 不会删除原有键，只会新增或覆盖。
# 🔸 字典是**可变对象**，所有操作都是**原地修改**！

#  五、删除键值对
# | 方法            | 说明                                             | 示例                       |
# | --------------- | ------------------------------------------------ | -------------------------- |
# | `del dict[key]` | 删除指定键（键不存在会报错）                     | `del user["age"]`          |
# | `.pop(key)`     | 删除并**返回值**（可设默认值）                   | `age = user.pop("age", 0)` |
# | `.popitem()`    | 删除并返回**最后一个**键值对（Python 3.7+ 有序） | `last = user.popitem()`    |
# | `.clear()`      | 清空整个字典                                     | `user.clear()`             |

user = {"name": "小明", "age": 20, "city": "上海"}
age = user.pop(
    "age"
)  # 删除并返回 age ,age = 20, user = {"name": "小明", "city": "上海"}
print(age)
print(user)
email = user.pop("email", "未知")  # 删除 email，city="未知"（键不存在，返回默认值）
print(email)
print(user)
last = user.popitem()
print(last)
user.clear()
print(user)
# > ✅ 推荐用 `.pop(key, default)` 安全删除！

# 六、检查键是否存在
user = {"name": "小红"}
if "age" in user:
    print("年龄已经记录")
else:
    print("请补充年龄")
# ❌ 不要用 .get() 判断存在性（效率低且不直观）
# if user.get("age"):  # 如果 age=0 或 False，会误判为不存在！
# ✅ **黄金法则**：用 `key in dict` 判断键是否存在！

#  七、字典常用方法
# | 方法        | 说明                                  | 示例            |
# | ----------- | ------------------------------------- | --------------- |
# | `.keys()`   | 返回所有键（**dict_keys** 对象）      | `user.keys()`   |
# | `.values()` | 返回所有值（**dict_values** 对象）    | `user.values()` |
# | `.items()`  | 返回所有键值对（**dict_items** 对象） | `user.items()`  |
# | `len(dict)` | 获取键值对数量                        | `len(user)`     |

# ✅ 遍历字典（推荐用 `.items()`）：
user = {"name": "小明", "age": 20, "score": 89}


# 获取字典长度
print(len(user))

# 获取所有键
print(list(user))

# 只遍历键
for key in user.keys():
    print(key)
for key in user:
    print(key)


# 只遍历值
for value in user.values():
    print(value)

# 遍历键和值
for key, value in user.items():
    print(f"{key}: {value}")

# 🔸 `.keys()`、`.values()`、`.items()` 返回的是**动态视图**，不是列表！
# 如需列表，用 `list(dict.keys())`

# 🔄 八、字典的高级操作

# 1. 字典合并（Python 3.9+）
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
# 方法1：合并操作符（推荐）
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 3, 'c': 4}
# 方法2：更新操作符（原地修改）
d1 |= d2
print(d1)  # {'a': 1, 'b': 3, 'c': 4}

# 2. **旧版本合并方式**
# Python 3.5+
merged = {**d1, **d2}
print(merged)
# 通用方法
merged = d1.copy()
merged.update(d2)
print(merged)
# Python 3.6+
merged = dict(d1, **d2)
print(merged)

# 3. **字典推导式（类似列表推导式）**
# 将列表转为字典
fruits = ["apple", "banana", "orange"]
fruit_len = {f: len(f) for f in fruits}
print(fruit_len) # {'apple': 5, 'banana': 6, 'orange': 6}

# 带条件
squares = {x: x ** 2 for x in range(1, 8) if x % 2 == 0}
print(squares) # {2: 4, 4: 16, 6: 36}

#  九、字典 vs 其他数据结构
# | 特性         | 字典（dict）       | 列表（list）       | 元组（tuple）    |
# | ------------ | ------------------ | ------------------ | ---------------- |
# | **结构**     | 键值对             | 有序序列           | 有序序列         |
# | **访问方式** | 通过键（名字）     | 通过索引（位置）   | 通过索引（位置） |
# | **可变性**   | ✅ 可变             | ✅ 可变             | ❌ 不可变         |
# | **用途**     | 存储**结构化信息** | 存储**同类型集合** | 存储**固定记录** |
# 列表：同类型数据
scores = [85, 92, 78]

# 字典：异构结构化数据
student = {
    "name": "Alice",
    "scores": [85, 92, 78],  # 字典里可以嵌套列表！
    "grade": "A"
}

'''
实战项目：简易通讯录
'''
print("======通讯录=====")
contacts = {}

while True:
    print("\n 1. 添加联系人")
    print(" 2. 查找联系人")
    print(" 3. 删除联系人")
    print(" 4. 显示所有联系人")
    print(" 5. 退出")

    choice = input("请选择操作：")
    if choice == "1":
        name = input("姓名：")
        phone = input("电话：")
        contacts[name] = phone
        print(f"添加联系人[{name}]成功！")
    elif choice == "2":
        name = input("请输入要查找的姓名：")
        phone = contacts.get(name, "未找到")
        print(f"{name} : {phone}")
    elif choice == "3":
        name = input("请输入要删除的姓名：")
        if name in contacts:
            contacts.pop(name)
            print(f"删除联系人[{name}]成功！")
        else:
            print("未找到该联系人！")
    elif choice == "4":
        if contacts: # 判断字典是否为空
            print("\n 所有联系人：")
            for name, phone in contacts.items():
                print(f"{name} : {phone}")
        else:
            print("通讯录为空！")
    elif choice == "5":
        print("再见！！")
        break
    else:
        print("无效选项，请重试！")


# 十一、常见错误 & 避坑指南

# | 错误                          | 说明        | 正确做法                                   |
# | ----------------------------- | ----------- | ------------------------------------------ |
# | 用不存在的键直接访问          | `KeyError`  | 用 `.get(key, default)`                    |
# | 用列表做键                    | `TypeError` | 键必须是不可变类型                         |
# | 修改字典时遍历                | 运行时错误  | 遍历 `.keys()` 的副本：`list(dict.keys())` |
# | 误以为字典有序（Python <3.6） | 旧版本无序  | Python 3.7+ 字典**保证插入顺序**           |


'''
动手练习
'''
# 练习1：统计字符出现的次数
text = "hello"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq) # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# 练习2：合并两个字典
d1 = { "a": 1, "b": 2}
d2 = { "b": 3, "c": 4}
merged = d1 | d2
print(merged) # {'a': 1, 'b': 3, 'c': 4}

# 练习3：字典推导式
squares = {x: x ** 2 for x in range(1, 5)}
print(squares)



