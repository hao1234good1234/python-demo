"""
现在进入 **数据结构的第一站：列表（list）** ——这是 Python 中**最常用、最灵活**的容器类型，用来**存储多个数据**，并能随时增删改查！
"""
# 一、认识列表 
# 列表的特点
# - **有序**：元素有固定顺序（从 0 开始编号）
# - **可变**：可以随时添加、删除、修改元素
# - **异构**：可以混合不同类型（数字、字符串、甚至其他列表！）
#  数据可以重复
# 1、创建列表
fruits = []
scores = [90, 47, 30, 20, 50]
names = ["小明", "小红", "小刚"]
mixed = [1, 50.9, "hello", None, True, [0, 1, 4]]  # 异构
#  列表用 **方括号 `[]`** 定义，元素用 **逗号 `,`** 分隔


# 2、访问列表元素
# （1）通过索引单个访问
names = ["小明", "小红", "小刚"]
print(names[0])  # 小明（第一个）
print(names[1])  # 小红
print(names[-1])  # 小刚（最后一个，负数从后往前数）
# > ⚠️ 索引从 **0 开始**！
# > ⚠️ 超出范围会报错：`IndexError: list index out of range`

# (2) 通过切片获取子列表
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(nums[1:4])  # [1, 2, 3] （从1到3，不包含4）
print(nums[:3])  # [0, 1, 2] （从开头到2）
print(nums[2:])  # [2, 3, 4, 5, 6, 7, 8] （从2到末尾）
print(nums[::2])  # [0, 2, 4, 6, 8] （每隔一个取一个）
print(nums[::-1])  # [8, 7, 6, 5, 4, 3, 2, 1, 0] （倒序）
print(nums[-3:-1])  # [6, 7] （倒数第3到倒数第2）
print(nums[-3:])  # [6, 7, 8]    （从倒数第3个到末尾）
print(nums[:-3])  # [0, 1, 2, 3, 4, 5] （从开头到倒数第3个）
print(nums[:])  # [0, 1, 2, 3, 4, 5, 6, 7, 8] （全取）
print(nums[::-2])  # [8, 6, 4, 2, 0] （每隔一个取一个，倒序）
# 🔸 切片语法：`[start:end:step]`
# 🔸 **左闭右开**：包含 `start`，不包含 `end`

# 3、修改列表元素
colors = ["红", "绿", "蓝"]
# 修改单个元素
colors[1] = "黄"
print(colors)  # ["红", "黄", "蓝"]
# 修改切片（替换一段）
colors[1:3] = ["紫", "橙"]
print(colors)  # ["红", "紫", "橙"]

# 4、添加元素
# | 方法            | 说明                   | 示例                       |
# | --------------- | ---------------------- | -------------------------- |
# | `.append(x)`    | 在**末尾**添加一个元素 | `fruits.append("苹果")`    |
# | `.insert(i, x)` | 在**位置 i** 插入元素  | `fruits.insert(0, "香蕉")` |
# | `+` 或 `+=`     | 合并列表               | `list1 + list2`            |
tasks = ["写代码"]
tasks.append("调试")  # 在末尾添加
tasks.insert(0, "规划")  # 在开头添加
print(tasks)  # ["规划", "写代码", "调试"]

# 5、删除元素
# | 方法          | 说明                                | 示例                    |
# | ------------- | ----------------------------------- | ----------------------- |
# | `.remove(x)`  | 删除**第一个值为 x** 的元素         | `fruits.remove("苹果")` |
# | `.pop(i)`     | 删除**位置 i** 的元素，并**返回它** | `last = tasks.pop()`    |
# | `del list[i]` | 删除指定位置                        | `del tasks[0]`          |
# | `.clear()`    | 清空整个列表                        | `tasks.clear()`         |
nums = [10, 20, 30, 20]
nums.remove(20)  # 删除第一个值为 20 的元素 → [10, 30, 20]
print(nums)
# last = nums.pop()  # 删除末尾元素并返回它 →  last=20, nums=[10, 30]
index_2_num = nums.pop(2)  # 删除位置2的元素并返回它
print(index_2_num, nums)
# del nums[0:2]  # 删除位置0-1的元素
del nums[0]  # 删除第一个元素 → nums=[30]
print(nums)
# ⚠️ 注意：
# - `remove()` 删除**值**，`pop()`/`del` 删除**位置**
# - `pop()` 默认删除最后一个：`tasks.pop()`

# 6、查找和判断
# | 操作            | 说明                    | 示例                        |
# | --------------- | ----------------------- | --------------------------- |
# | `x in list`     | 判断 x 是否在列表中     | `"苹果" in fruits` → `True` |
# | `list.index(x)` | 返回 x 的**第一个索引** | `fruits.index("苹果")`      |
# | `list.count(x)` | 统计 x 出现的次数       | `nums.count(20)`            |
shooping_cart = ["纸巾", "牙膏", "辣条"]
if "牛奶" in shooping_cart:
    print("购物车已经有牛奶了")
else:
    shooping_cart.append("牛奶")
fruits = ["苹果", "香蕉", "荔枝"]
index = fruits.index("苹果")
print(index)
scores = [90, 89, 90, 99, 50]
print(scores.count(90))

# 7、列表常用操作
# | 操作             | 说明                 | 示例                         |
# | ---------------- | -------------------- | ---------------------------- |
# | `len(list)`      | 获取长度             | `len([1,2,3])` → `3`         |
# | `list.sort()`    | **原地排序**（升序） | `scores.sort()`              |
# | `sorted(list)`   | 返回**新排序列表**   | `new = sorted(scores)`       |
# | `list.reverse()` | **原地反转**         | `nums.reverse()`             |
# | `list.copy()`    | 浅拷贝               | `new_list = old_list.copy()` |

scores = [90, 89, 90, 99, 50]
print(len(scores))

scores.sort()  # 原地升序 →  [50, 89, 90, 90, 99]
scores.reverse()  # 原地反转 →  [99, 90, 90, 89, 50]
scores.sort(reverse=True)  # 原地降序
print(scores)

scores = [90, 89, 90, 99, 50]
scores_copy = scores.copy()  # 浅拷贝 new_list = old_list.copy()
print(scores_copy)

sorted_scores = sorted(scores_copy)  # 返回新排序列表  `new = sorted(scores)`
print(sorted_scores)

words = ["hello", "world", "hi", "python", "java", "vue"]
words.sort(key=len, reverse=True)  # 按字符串的长度降序-> [python, vue, java, hello, world, hi]
print(words)

scores = [85, 92, 78, 96, 88]
reversed_scores = list(reversed(scores))  # 返回反转的列表
print(reversed_scores)

# 8. 列表+循环
# （1）遍历列表 (推荐用for循环)
fruits = ["苹果", "香蕉", "荔枝"]
for fruit in fruits:
    print(fruit)

# (2) 同时获取索引和值 (用enumerate函数)
for index, fruit in enumerate(fruits, start=1):
    print(f"第{index}个水果是： {fruit}")

# (3) 列表推导式 (高超但超实用)
# 普通写法
squares = []
for i in range(5):
    squares.append(i ** 2)
print(squares)

# 列表推导式，一行代码完成
squares = [i ** 2 for i in range(5)]
print(squares)

# 带条件的列表推导式
evens = [i for i in range(20) if i % 2 == 0]
print(evens)


'''
实战项目 简单代办事项清单
'''
print("==========简单代办事项清单==========")
tasks = []
while True:
    print("\n1. 添加任务")
    print("2. 查看任务")
    print("3. 删除任务")
    print("4. 退出")

    choice = input("请选择操作：")
    if choice == "1":
        task = input("请输入你要添加的任务：")
        if task.strip():
            tasks.append(task)
            print(f"添加任务[{task}]成功！")
        else:
            print("任务不能为空！")
    elif choice == "2":
        if tasks:
            print("\n 你的任务：")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("你没有任务！")
    elif choice == "3":
        if tasks:
            print("\n你的任务：")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
            try:
                index = int(input("请输入你要删除任务的编号：")) - 1
                if 0 <= index <= len(tasks):
                    removed_task = tasks.pop(index)
                    print(f"任务[{removed_task}] 删除成功！")
                else:
                    print("无效的编号！")
            except ValueError:
                print("请输入整数！")
        else:
            print("你没有任务可删除！")
    elif choice == "4":
        print("再见！")
        break
    else:
        print("无效选项，请重试！")

# 常见错误
# | 错误              | 说明                                       | 正确做法                |
# | ----------------- | ------------------------------------------ | ----------------------- |
# | 修改列表时遍历    | `for x in list: list.remove(x)` → 跳过元素 | 用 `[:]` 复制或倒序遍历 |
# | 忘记索引从 0 开始 | 以为 `list[1]` 是第一个                    | 记住：**0 是第一个**    |
# | 直接赋值复制列表  | `new = old` → 两个变量指向同一列表         | 用 `new = old.copy()`   |
# | 对空列表取 `[-1]` | `IndexError`                               | 先判断 `if list:`       |
# (1) 获得列表中的最大、最小、平均分
scores = [85, 92, 78, 96, 88]
print(f"最高分是：{max(scores)}")
print(f"最低分是：{min(scores)}")
print(f"平均分是：{sum(scores) / len(scores) :.2f}")
# (2) 去重 (用set转换)
duplicates = [10, 20, 23, 10, 33, 20, 30, 44, 59, 69]
unique = list(set(duplicates))
print(f"去重后：{unique}")
print(f"去重排序后：{sorted(unique)}")
# (3) 列表推导式
squared = [x ** 2 for x in range(1, 6) if x % 2 == 1]
print(f"奇数的平方是：{squared}")