"""
集合（set） → 去重、交集、并集、差集
"""
# 特点：
# - **元素唯一**（自动去重）
# - **无序**（不能索引）
# - **支持交集、并集、差集等运算**

# 一、什么是集合（set）？
# - **无序**：元素没有固定顺序（不能用 `s[0]` 访问）
# - **唯一**：自动去除重复元素
# - **可变**：可以添加/删除元素（但元素本身必须**不可变**）
# - **元素必须是可哈希的**（如 `int`, `str`, `tuple`，不能是 `list`/`dict`）
# ✅ **典型用途**：
# - 去重（如从列表中去除重复项）
# - 快速成员判断（比列表快得多！）
# - 数学集合运算：交集、并集、差集、对称差集

#  二、创建集合
# 1. 基本语法：**花括号 `{}`（但不能空！）**
# ❌ 空花括号是字典！
empty_dict = {}  # 这是 dict！
# 创建空集合
empty_set = set()
# 创建非空集合
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 2, 1}  # 自动去重
print(numbers)  # {1, 2, 3}

# 2. 用 `set()` 构造函数（推荐用于去重）
# 从列表去重
lst = [1, 2, 2, 3, 3, 3]
unique = set(lst)
print(unique)  # {1, 2, 3}

# 从字符串去重
letters = set("hello")
print(letters)  # {'h', 'e', 'l', 'o'}

# 从元组去重
tup = (1, 2, 2, 3, 3, 3)
unique = set(tup)
print(unique)  # {1, 2, 3}

# ⚠️ **注意**：

# - `{}` 是空字典，**不是空集合**！
# - 空集合必须写成 `set()`

#  三、集合的基本操作
# 1. 添加元素
s = {1, 2}
s.add(3)  # 添加元素 3
s.add(2)  # 重复元素会被忽略
print(s)  # {1, 2, 3}

# 2. 删除元素
# | 方法           | 说明                               | 示例           |
# | -------------- | ---------------------------------- | -------------- |
# | `s.remove(x)`  | 删除元素（不存在会报错）           | `s.remove(2)`  |
# | `s.discard(x)` | 安全删除（不存在也不报错）         | `s.discard(5)` |
# | `s.pop()`      | 随机删除并返回一个元素（因为无序） | `x = s.pop()`  |
# | `s.clear()`    | 清空集合                           | `s.clear()`    |
s = {1, 2, 3}
s.discard(4)  # 不存在不会报错
# s.remove(5)  # 不存在会报错

# 🔎 四、成员判断（超快！）
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("有苹果")  # 有苹果 O(1) 平均时间复杂度

# 比列表快得多
# lst = ["apple", "banana", ...] → "apple" in lst 是 O(n)
# ✅ **集合的成员判断是常数时间 O(1)**，适合大量数据去重和查找！

# 🧮 五、集合的数学运算（核心功能！）
# 假设有两个集合：
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# | 运算         | 含义                     | 运算符   | 方法                        | 结果                 |
# | ------------ | ------------------------ | -------- | --------------------------- | -------------------- |
# | **交集**     | 同时在 A 和 B 中         | `A & B`  | `A.intersection(B)`         | `{3, 4}`             |
# | **并集**     | 在 A 或 B 中             | `A \| B` | `A.union(B)`                | `{1, 2, 3, 4, 5, 6}` |
# | **差集**     | 在 A 但不在 B 中         | `A - B`  | `A.difference(B)`           | `{1, 2}`             |
# | **对称差集** | 在 A 或 B 中，但不同时在 | `A ^ B`  | `A.symmetric_difference(B)` | `{1, 2, 5, 6}`       |

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A & B)  # {3, 4}
print(A | B)  # {1, 2, 3, 4, 5, 6}
print(A - B)  # {1, 2}
print(A ^ B)  # {1, 2, 5, 6}

# 🔄 六、集合的更新操作（原地修改）

# | 方法                               | 说明       | 等价运算 |
# | ---------------------------------- | ---------- | -------- |
# | `A.update(B)`                      | A = A \| B | `A |= B` |
# | `A.intersection_update(B)`         | A = A & B  | `A &= B` |
# | `A.difference_update(B)`           | A = A - B  | `A -= B` |
# | `A.symmetric_difference_update(B)` | A = A ^ B  | `A ^= B` |

A = {1, 2, 3}
B = {3, 4}
A.update(B)  # A = A | B , A = {1, 2, 3, 4}
A.intersection_update(B)  # A = A & B , A = {3}
A.difference_update(B)  # A = A - B , A = {1, 2}
A.symmetric_difference_update(B)  # A = A ^ B , A = {1, 2, 4}

#  七、集合的其他方法
# | 方法                  | 说明           | 示例                               |
# | --------------------- | -------------- | ---------------------------------- |
# | `len(s)`              | 元素个数       | `len({1,2,3}) → 3`                 |
# | `s.copy()`            | 浅拷贝         | `new_set = s.copy()`               |
# | `s.isdisjoint(other)` | 是否**无交集** | `{1,2}.isdisjoint({3,4}) → True`   |
# | `s.issubset(other)`   | 是否是子集     | `{1,2}.issubset({1,2,3}) → True`   |
# | `s.issuperset(other)` | 是否是超集     | `{1,2,3}.issuperset({1,2}) → True` |
s = {1, 2, 3}
print(len(s))
p = s.copy()
print(p)
required_skills = {"Python", "Sql"}
candidate_skills = {"Python", "Sql", "Flask"}
if required_skills.issubset(candidate_skills):
    print("满足要求")

print("是否无交集", required_skills.isdisjoint(candidate_skills))
print("是否是子集", required_skills.issubset(candidate_skills))
print("是否是超集", required_skills.issuperset(candidate_skills))

# 🎮 八、实战场景
# 场景 1：列表去重（最常用！）
data = [1, 2, 2, 3, 3, 4]
unique_data = set(data)  # [1, 2, 3, 4]（顺序可能变！）
print(unique_data)

# 如果需要保持顺序（Python 3.7+）
unique_data = list(dict.fromkeys(data))  # [1, 2, 3, 4] 
print(unique_data)
# 场景 2：找共同好友
user1_friends = {"Alice", "Bob", "Charlie"}
user2_friends = {"Bob", "David", "Eve"}
common = user1_friends & user2_friends
print(common)  # {'Bob'}

# 场景 3：权限检查
user_roles = {"admin", "editor"}
required_roles = {"admin", "viewer"}
if required_roles & user_roles:
    print("有权限访问")

# 九、注意事项 & 常见误区
# | 误区               | 正确理解                                               |
# | ------------------ | ------------------------------------------------------ |
# | “集合有序”         | ❌ 集合**无序**（不能索引、切片）                       |
# | `{}` 是空集合      | ❌ `{}` 是空字典，空集合是 `set()`                      |
# | 集合元素可以是列表 | ❌ 元素必须**不可变**（不能是 list/dict）               |
# | 去重后顺序不变     | ❌ `set()` 会打乱顺序（如需保序，用 `dict.fromkeys()`） |

# ❌ 错误：列表不可哈希
# s = {[1, 2], [3, 4]}  # TypeError!

# ✅ 正确：用元组
s = {(1, 2), (3, 4)}

# ✅ 十、动手练习
# 练习1 去重
nums = {1, 2, 2, 3, 4, 4, 5}
uinque_nums = set(nums)
print(uinque_nums)  # {1, 2, 3, 4, 5}

# 练习2 交集
A = {1, 2, 3}
B = {3, 4}
print(A & B)

# 练习3 子集判断
allowed = {"read", "write"}
user_perms = {"read"}
if user_perms.issubset(allowed):
    print("权限合法")

#  十一、集合 vs 其他数据结构
# | 特性         | 集合（set）    | 列表（list） | 元组（tuple） | 字典（dict）          |
# | ------------ | -------------- | ------------ | ------------- | --------------------- |
# | **是否有序** | ❌ 无序         | ✅ 有序       | ✅ 有序        | ✅ 有序（Python 3.7+） |
# | **是否唯一** | ✅ 唯一         | ❌ 可重复     | ❌ 可重复      | ✅ 键唯一              |
# | **是否可变** | ✅ 可变         | ✅ 可变       | ❌ 不可变      | ✅ 可变                |
# | **主要用途** | 去重、集合运算 | 动态序列     | 固定记录      | 键值映射              |


# 十二、  集合的“延伸知识”（进阶但非必需）
# 1. **不可变集合：`frozenset`**
# 类似元组之于列表，`frozenset` 是**不可变版本的 set**，可作为字典的键或集合的元素。
# 普通 set 不能做字典键
# d = {{1, 2}: "value"}  # ❌ TypeError

# frozenset 可以！
fs = frozenset([1, 2, 3])
# fs = frozenset({1, 2, 3})
d = {fs: "a set as key"}
print(d)  # {frozenset({1, 2, 3}): 'a set as key'}

# frozenset 也支持集合运算
A = frozenset([1, 2])
B = frozenset([2, 3])
print(A & B)  # frozenset({2})
# ✅ 用途：  
# - 需要“集合的集合”时（如分类标签组合）  
# - 作为缓存键（如函数参数是集合时）