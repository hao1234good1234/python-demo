"""
#  Python 字典（dict）常用函数与方法速查手册

> ✅ 字典是 **键值对（key-value）** 的无序（Python 3.7+ 有序）可变容器  
> ✅ 键必须是 **不可变类型**（如 `str`, `int`, `tuple`）  
> ✅ 值可以是 **任意类型**
"""


# 📌 一、创建字典
# | 方法                                | 说明                                                         | 示例                                                         |
# | ----------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
# | `{}`                                | 创建空字典                                                   | `d = {}`                                                     |
# | `{'key': value, ...}`               | 直接初始化                                                   | `person = {"name": "张三", "age": 25}`                       |
# | `dict()`                            | 构造函数                                                     | `d = dict(name="李四", age=30)`                              |
# | `dict([(k, v), ...])`               | 从键值对列表创建                                             | `d = dict([("a", 1), ("b", 2)])`                             |
# | `dict(zip(keys, values))`           | 从两个列表合并                                               | `d = dict(zip(['x','y'], [1,2]))`                            |
# | dict.fromkeys(iterable, value=None) | 这是一个**类方法**，用于**批量创建字典**，所有键来自一个可迭代对象（如列表、元组、字符串等），并且**所有键对应的值都相同**（默认为 `None`） | keys = ['name', 'age', 'city']    换行 d = dict.fromkeys(keys)    换行  d2 = dict.fromkeys(keys, 0) |

keys = ["name", "age", "city"]
d = dict.fromkeys(keys)
print(d)

# 指定默认值
d2 = dict.fromkeys(keys, 0)
print(d2)



# 🔍 二、访问值
# | 方法                  | 说明                               | 示例                           |
# | --------------------- | ---------------------------------- | ------------------------------ |
# | `d[key]`              | 通过键获取值（**键不存在会报错**） | `name = user["name"]`          |
# | `d.get(key)`          | 安全获取值，不存在返回 `None`      | `email = user.get("email")`    |
# | `d.get(key, default)` | 指定默认值                         | `score = user.get("score", 0)` |

# > ✅ **最佳实践：优先使用 `.get()` 避免 `KeyError`**

# ✏️ 三、添加 / 修改键值对
# | 方法                                 | 说明                                                         | 示例                                        |
# | ------------------------------------ | ------------------------------------------------------------ | ------------------------------------------- |
# | `d[key] = value`                     | 添加新键或修改已有键                                         | `user["city"] = "北京"`                     |
# | `d.update(other_dict)`               | 批量更新（合并字典）                                         | `user.update({"age": 26, "job": "工程师"})` |
# | `d.update(key=value)`                | 用关键字参数更新                                             | `user.update(age=27)`                       |
# | `dict.setdefault(key, default=None)` | 如果 `key` **存在**，返回它的值； 如果 `key` **不存在**，则**插入**这个键，并把值设为 `default`，然后返回 `default`。 | city = d.setdefault('city', 'Beijing')      |

d = {"name": "小明"}
# key存在，返回原值
value = d.setdefault("name", "小红")
print(value)
print(d)

# key不存在，插入新值
value = d.setdefault("age", 20)
print(value)
print(d)

# 常见用途：分组统计（比如按类别收集数据）
data = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "carrot")]
groups = {}
for category, item in data:
    groups.setdefault(category, []).append(item) # 等价于 groups[category] = groups.get(category, []) + [item]
print(groups)



# > 🔸 `update()` 不会删除原有键，只会新增或覆盖。

# ➖ 四、删除键值对
# | 方法                  | 说明                                        | 示例                       |
# | --------------------- | ------------------------------------------- | -------------------------- |
# | `del d[key]`          | 删除指定键（**键不存在报错**）              | `del user["age"]`          |
# | `d.pop(key)`          | 删除并返回值（**键不存在报错**）            | `age = user.pop("age")`    |
# | `d.pop(key, default)` | 安全删除，指定默认返回值                    | `age = user.pop("age", 0)` |
# | `d.popitem()`         | 删除并返回**最后一个**键值对（Python 3.7+） | `last = user.popitem()`    |
# | `d.clear()`           | 清空整个字典                                | `user.clear()`             |

# > ✅ 推荐用 `.pop(key, default)` 安全删除！

# 🔎 五、检查键/值是否存在
# | 表达式                | 说明                         | 示例                      |
# | --------------------- | ---------------------------- | ------------------------- |
# | `key in d`            | 检查**键**是否存在（✅ 推荐） | `"name" in user`          |
# | `key not in d`        | 检查键不存在                 | `"email" not in user`     |
# | `value in d.values()` | 检查**值**是否存在（较慢）   | `"张三" in user.values()` |
# ⚠️ **不要用 `d.get(key)` 判断存在性**！  
# 原因：如果值是 `0`、`False`、`""`，会被误判为“不存在”。

# 📊 六、获取键、值、键值对
## 六、获取键、值、键值对

# | 方法         | 返回类型      | 说明                   | 示例                            |
# | ------------ | ------------- | ---------------------- | ------------------------------- |
# | `d.keys()`   | `dict_keys`   | 所有键的动态视图       | `list(user.keys())`             |
# | `d.values()` | `dict_values` | 所有值的动态视图       | `list(user.values())`           |
# | `d.items()`  | `dict_items`  | 所有 `(key, value)` 对 | `for k, v in user.items(): ...` |

# dict.keys()、dict.values()、dict.items() 返回的是动态视图对象，不是列表。如果需要列表，可使用 list(dict.keys())。

# ✅ 遍历字典（最常用）：
# for key, value in user.items():
#     print(f"{key}: {value}")
# 🔸 这些视图是**动态的**：字典变了，视图也变！

# 📏 七、其他实用函数（全局函数）
# | 函数      | 说明                                  | 示例                      |
# | --------- | ------------------------------------- | ------------------------- |
# | `len(d)`  | 获取键值对数量                        | `len({"a":1, "b":2}) → 2` |
# | `dict()`  | 转换或创建字典                        | `dict(a=1, b=2)`          |
# | `list(d)` | 获取所有键（等价于 `list(d.keys())`） | `list({"x":1}) → ['x']`   |

# 🔄 八、字典合并（Python 3.9+）

# | 操作       | 说明                                    | 示例                                 |
# | ---------- | --------------------------------------- | ------------------------------------ |
# | `d1 | d2`  | 合并两个字典（返回新字典）              | `{"a":1} | {"b":2} → {"a":1, "b":2}` |
# | `d1 |= d2` | 原地更新 `d1`（等价于 `d1.update(d2)`） | `d1 |= {"c":3}`                      |

# 兼容旧版本的合并方式：
d1 = {"a": 1}
d2 = {"b": 2}

# Python 3.5+
merged = {**d1, **d2}

# 通用方法
merged = d1.copy()
merged.update(d2)

# 🧩 九、字典推导式（Dict Comprehension）
# | 语法                                   | 说明                                                         | 示例                                                         |
# | -------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
# | `{k: v for ...}`                       | 从可迭代对象构建字典                                         | `{x: x**2 for x in range(3)}` → `{0:0, 1:1, 2:4}`            |
# | `{k: v for ... if ...}`                | 带条件过滤                                                   | `{k: v for k, v in d.items() if v > 0}`                      |
# | `{k: v for k, v in zip(keys, values)}` | 这是一种**简洁、高效**地从两个可迭代对象（如两个列表）构建字典的方式，`zip(keys, values)` 把两个列表“配对”成元组序列； 等价写法（使用 `dict()` + `zip()`） | keys = ['a', 'b', 'c'] values = [1, 2, 3]  d = {k: v for k, v in zip(keys, values)} |

# 反转字典（键值互换）
original = {"a": 1, "b": 2}
reversed_d = {v: k for k, v in original.items()}  # {1: 'a', 2: 'b'}

keys = ["a", "b", "c"]
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)  # {'a': 1, 'b': 2, 'c': 3}
d = dict(zip(keys, values))
print(d)
# 🌟 但字典推导式的真正优势在于可以加条件或转换：
# 只保留大于0 的项
keys = ["a", "b", "c"]
values = [1, -2, 3]
d = {k: v for k, v in zip(keys,values) if v > 0}
print(d)

# 键转大写，值平方
d2 = {k.upper(): v ** 2 for k, v in zip(keys, values)}
print(d2)


# 🧪 十、实战技巧 & 最佳实践
# 1. **安全初始化嵌套字典**
# ❌ 容易出错
# data = {}
# data["user"]["name"] = "zhangsan"

# ✅ 用 defaultdict（需导入）
from collections import defaultdict
data = defaultdict(dict)
data["user"]["name"] = "zhangsan"
data["user"]["age"] = 18
print(data)

# ✅ 或手动初始化
data = {}
data.setdefault("user", {})["name"] = "lisi"
data.setdefault("user", {})["age"] = 20
print(data)

# 2. **统计频率（经典用法）**
text = "hello world"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq) 

# 3. **字典作为函数返回值**
def get_user_info(uid):
    return {
        "id": uid,
        "name": "用户" + str(uid),
        "status": "active"
    }
user = get_user_info(29)
print(user)


# 十一、常见错误 & 注意事项
# | 问题                       | 原因             | 解决方案                                              |
# | -------------------------- | ---------------- | ----------------------------------------------------- |
# | `KeyError`                 | 访问不存在的键   | 用 `.get(key, default)`                               |
# | 键是列表/字典              | 键必须不可变     | 改用元组或字符串                                      |
# | 遍历时修改字典             | RuntimeError     | 遍历 `list(d.keys())` 副本                            |
# | 误以为旧版 Python 字典有序 | Python <3.7 无序 | 如需有序，用 `collections.OrderedDict`（Python <3.7） |

# ✅ **Python 3.7+ 字典默认保持插入顺序！**

# 📋 十二、速查表（建议收藏）
# | 操作           | 推荐方法                                  |
# | -------------- | ----------------------------------------- |
# | **安全取值**   | `.get(key, default)`                      |
# | **判断键存在** | `key in dict`                             |
# | **遍历键值对** | `for k, v in dict.items():`               |
# | **添加/修改**  | `dict[key] = value`                       |
# | **批量更新**   | `dict.update(other)`                      |
# | **安全删除**   | `.pop(key, default)`                      |
# | **合并字典**   | `d1 | d2`（Python 3.9+）或 `{**d1, **d2}` |
# | **清空字典**   | `.clear()`                                |

# ✅ 十三、综合练习
# 1. 合并两个字典，d2 优先
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
result = d1 | d2  # Python 3.9+
# result = {**d1, **d2}  # 兼容写法
print(result)

# 2.找出值最大的键
scores = {"Alice": 92, "Bob": 85, "Charlie": 96}
top_student  = max(scores, key=scores.get) 
print(top_student)

# 3. 过滤字典（只保留值大于 0 的）
data = {"x": -1, "y": 2, "z": 0}
positive = {k: v for k, v in data.items() if v > 0}
print(positive)
