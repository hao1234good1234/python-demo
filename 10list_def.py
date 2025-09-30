"""
以下是 Python **列表（list）** 最常用、最实用的 **内置方法和函数** 的全面总结，按功能分类整理，方便你快速查阅和掌握。
"""

'''
一、创建与复制
'''
# | 方法/函数     | 说明                         | 示例                          |
# | ------------- | ---------------------------- | ----------------------------- |
# | `list()`      | 创建空列表或从可迭代对象转换 | `list("abc") → ['a','b','c']` |
# | `list.copy()` | **浅拷贝**列表（推荐）       | `new = old.copy()`            |
# | `list[:]`     | 切片拷贝（等效于 `copy()`）  | `new = old[:]`                |

# ⚠️ 避免直接赋值：`new = old` → 两者指向同一对象！

'''
 二、访问与查找
'''

# | 方法/函数              | 说明                       | 示例                       |
# | ---------------------- | -------------------------- | -------------------------- |
# | `list[index]`          | 通过索引访问元素           | `nums[0]`                  |
# | `list[start:end:step]` | 切片获取子列表             | `nums[1:4]`                |
# | `len(list)`            | 获取列表长度               | `len([1,2,3]) → 3`         |
# | `x in list`            | 判断元素是否存在           | `"a" in ["a","b"] → True`  |
# | `list.index(x)`        | 返回 **第一个** `x` 的索引 | `["a","b"].index("b") → 1` |
# | `list.count(x)`        | 统计 `x` 出现的次数        | `[1,2,2].count(2) → 2`     |

# `index()` 找不到会报错：`ValueError`，建议先用 `in` 判断。

'''
三、添加元素
'''
# | 方法                    | 说明                        | 示例                       |
# | ----------------------- | --------------------------- | -------------------------- |
# | `list.append(x)`        | 在**末尾**添加一个元素      | `fruits.append("苹果")`    |
# | `list.insert(i, x)`     | 在**位置 i** 插入元素       | `fruits.insert(0, "香蕉")` |
# | `list.extend(iterable)` | 在末尾**追加多个元素**      | `a.extend([4,5])`          |
# | `list + other_list`     | 合并两个列表（返回新列表）  | `[1,2] + [3] → [1,2,3]`    |
# | `list += other_list`    | 原地扩展（等效于 `extend`） | `a += [4,5]`               |

# ✅ 对比：
a = [1, 2]
a.append([3, 4]) # → [1, 2, [3, 4]]  （嵌套！）
print(f"append: {a}")
a.extend([3, 4]) # → [1, 2, 3, 4]     （展开）
print(f"extend: {a}")

'''
四、删除元素
'''
# | 方法/函数        | 说明                                | 示例                    |
# | ---------------- | ----------------------------------- | ----------------------- |
# | `list.remove(x)` | 删除**第一个值为 x** 的元素         | `fruits.remove("苹果")` |
# | `list.pop(i)`    | 删除**位置 i** 的元素，并**返回它** | `last = tasks.pop()`    |
# | `list.pop()`     | 删除并返回**最后一个**元素          | `tasks.pop()`           |
# | `del list[i]`    | 删除指定索引的元素                  | `del nums[0]`           |
# | `del list[i:j]`  | 删除切片                            | `del nums[1:3]`         |
# | `list.clear()`   | 清空整个列表（变为空）              | `tasks.clear()`         |

# ✅ `pop()` 常用于“取出并使用”：
# last_task = todo_list.pop()
# print(f"正在处理: {last_task}")
'''
五、排序与反转
'''
# | 方法/函数                 | 说明                               | 示例                        |
# | ------------------------- | ---------------------------------- | --------------------------- |
# | `list.sort()`             | **原地排序**（默认升序）           | `scores.sort()`             |
# | `list.sort(reverse=True)` | 降序排序                           | `scores.sort(reverse=True)` |
# | `list.sort(key=func)`     | 按自定义规则排序                   | `words.sort(key=len)`       |
# | `sorted(list)`            | 返回**新排序列表**（不改变原列表） | `new = sorted(scores)`      |
# | `list.reverse()`          | **原地反转**列表                   | `nums.reverse()`            |
# | `reversed(list)`          | 返回反转的**迭代器**               | `list(reversed(nums))`      |

# ✅ 排序示例：
students = [("小明", 85), ("小红", 92)]
students.sort(key=lambda x: x[1], reverse=True)  # 按成绩降序
# → [("小红", 92), ("小明", 85)]
print(students)
'''
六、其他实用函数（全局函数）
'''
# | 函数        | 说明             | 示例                           |
# | ----------- | ---------------- | ------------------------------ |
# | `len(list)` | 长度             | `len([1,2]) → 2`               |
# | `max(list)` | 最大值           | `max([1,5,3]) → 5`             |
# | `min(list)` | 最小值           | `min([1,5,3]) → 1`             |
# | `sum(list)` | 求和（仅数字）   | `sum([1,2,3]) → 6`             |
# | `all(list)` | 所有元素为真？   | `all([1,2,"a"]) → True`        |
# | `any(list)` | 有任一元素为真？ | `any([0, "", None, 1]) → True` |

# ⚠️ `sum()` 只能用于数字列表！

'''
七、与循环/推导式结合
'''
# | 技巧                              | 说明             | 示例                           |
# | --------------------------------- | ---------------- | ------------------------------ |
# | `for item in list`                | 遍历元素         | `for name in names:`           |
# | `for i, item in enumerate(list)`  | 同时获取索引和值 | `for i, n in enumerate(nums):` |
# | `[expr for item in list]`         | 列表推导式       | `[x*2 for x in [1,2,3]]`       |
# | `[expr for item in list if cond]` | 带条件的推导式   | `[x for x in nums if x > 0]`   |

# ✅ 推导式 vs 循环：
# # 传统写法
# squares = []
# for x in range(5):
#     squares.append(x**2)

# # 推导式（更 Pythonic）
# squares = [x**2 for x in range(5)]

'''
八、速查表（建议收藏）
'''
# | 操作             | 推荐方法                                 |
# | ---------------- | ---------------------------------------- |
# | **添加到末尾**   | `.append(x)`                             |
# | **插入到中间**   | `.insert(i, x)`                          |
# | **删除已知值**   | `.remove(x)`                             |
# | **删除已知位置** | `.pop(i)` 或 `del list[i]`               |
# | **清空列表**     | `.clear()`                               |
# | **排序**         | `.sort()`（原地）或 `sorted()`（新列表） |
# | **反转**         | `.reverse()`                             |
# | **查找位置**     | `.index(x)`                              |
# | **判断存在**     | `x in list`                              |
# | **安全复制**     | `.copy()` 或 `list[:]`                   |

'''
九、注意事项
'''
# 1. **列表是可变对象**：函数内修改会影响原列表。

# 2. **避免在遍历时修改列表**：
# ❌ 危险！会跳过元素
my_list = [1, -2, 3, -4, 5]
for x in my_list:
    if x < 0:
        my_list.remove(x)

# ✅ 安全做法：遍历副本 
for x in my_list[:]:
    if x < 0:
        my_list.remove(x)
# (1): my_list[:] 是对列表 my_list 的 切片操作，从开头到结尾（默认步长为 1），相当于创建了一个 新的列表对象，内容和原列表相同。
# (2): 这个新列表是原列表的一个 浅拷贝（shallow copy），也就是说：
#       对于列表中的不可变元素（如整数、字符串），拷贝的是值；
#       对于可变元素（如嵌套列表、字典等），拷贝的是引用（即嵌套对象本身没有被复制）。
# (3): my_list[:] 等价于 list(my_list) 或 my_list.copy()（对于列表而言）。  

# 3 **`sort()` vs `sorted()`**：
# - `sort()` 改变原列表
# - `sorted()` 返回新列表，原列表不变

'''
实战练习
'''
# 1、去重并排序
data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
unique_sorted_data = sorted(set(data))
print(unique_sorted_data)

# 2、找出最大值和索引
nums = [10, 30, 20]
max_val = max(nums)
max_val_index = nums.index(max_val)
print(f"最大值为{max_val}，索引为{max_val_index}")

# 3、合并两个列表并去重
a = [1, 2, 3]
b = [3, 4, 5]
mergered_list = list(set(a + b))
print(sorted(mergered_list))

# 4.列表的浅拷贝和深拷贝
old_list = [1, 2, 3, [8,9], (3, 5, 6, 7)]
# 浅拷贝
new_list = old_list.copy()
print(new_list)
# 深拷贝（需要导入 copy 模块）
import copy
deep_copy = copy.deepcopy(old_list)
print(deep_copy)
