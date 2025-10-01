"""
异常处理（try / except）
"""

# 二、异常处理基本语法：`try...except`
# 基本结构
"""
try:
    # 可能出错的代码
    ...
except 错误类型1:
    # 处理错误1
    ...
except 错误类型2:
    # 处理错误2
    ...
else:
    # 没有异常时执行（可选）
    ...
finally:
    # 无论如何都执行（可选，常用于清理资源）
    ...
"""
# `try` 必须搭配至少一个 `except` 或 `finally`

#  三、常见内置异常类型（你一定会遇到！）
# | 异常类型            | 触发场景           | 示例                 |
# | ------------------- | ------------------ | -------------------- |
# | `ValueError`        | 值类型正确但值无效 | `int("abc")`         |
# | `ZeroDivisionError` | 除以零             | `10 / 0`             |
# | `FileNotFoundError` | 文件不存在         | `open("不存在.txt")` |
# | `KeyError`          | 字典键不存在       | `d["不存在的键"]`    |
# | `IndexError`        | 列表索引越界       | `lst[999]`           |
# | `TypeError`         | 类型错误           | `"a" + 1`            |
# | `AttributeError`    | 对象没有该属性     | `"hello".append()`   |

# ✅ **记住：遇到报错时，Python 会告诉你异常类型！**
#  四、实战示例
# 示例 1：安全除法函数
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "错误：除数不能为0"
print(safe_divide(10, 0))
print(safe_divide(10, 2))

# ✅ 函数内部处理异常，调用者无需担心崩溃！
# 示例 2：读取文件（处理文件不存在）
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"错误：文件{filename}不存在"
    except PermissionError:
        return f"错误：无权限读取文件{filename}"
content = read_file("日志.log")
print(content)

# 示例 3：通用异常捕获（谨慎使用！）
def risky_operation():
    raise ValueError("发生错误！")
try:
    risky_operation()
except Exception as e:
    print(f"发生异常：{e}")
    # 可记录日志：logging.error(e)

# ⚠️ **不要滥用 `except Exception`**！  
# 它会隐藏所有错误，不利于调试。**优先捕获具体异常**。


#  五、`else` 和 `finally` 的妙用
# `else`：仅在**没有异常**时执行
try:
    num = int(input("请输入一个整数："))
except ValueError:
    print("输入的不是数字")
else:
    print(f"你输入的数字是：{num}") # 只有成功转换才打印

# `finally`：**无论如何都执行**（常用于清理）
file = None
try:
    file = open("data.txt")
    data = file.read()
    # 处理数据...
except FileNotFoundError:
    print("文件不存在！")
finally:
    if file:
        file.close()  # 确保文件关闭！
    print("文件已关闭！")
    

# 💡 但更推荐用 `with open(...)` 自动管理资源（上下文管理器），后续会学！

# 六、主动抛出异常：`raise`
# 有时你想**自己制造错误**来阻止非法操作：
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("余额不足!") # 主动抛出异常
    return balance - amount

try:
    new_balance = withdraw(100, 300)
except ValueError as e:
    print("错误：", e)
# ✅ **在函数中抛出异常，让调用者决定如何处理**，这是专业做法！
# 七、自定义异常（进阶但实用）
# 你可以定义自己的错误类型：
class InvalidAgeError(Exception):
    """年龄无效的自定义异常"""
    pass
def set_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError("年龄无效！年龄必须在 0 到 150 之间！")
    return age
try:
    set_age(-22)
except InvalidAgeError as e:
    print("自定义异常：", e)
# ✅ 自定义异常让错误更清晰，便于分类处理。

#  八、异常处理最佳实践
# | 做法                      | 说明                                                 |
# | ------------------------- | ---------------------------------------------------- |
# | ✅ **捕获具体异常**        | `except ValueError` 比 `except Exception` 好         |
# | ✅ **不要忽略异常**        | 至少打印或记录日志                                   |
# | ✅ **在合适层级处理**      | 底层函数抛出，上层统一处理                           |
# | ✅ **用 `raise` 传递异常** | `except: raise` 可保留原始堆栈                       |
# | ❌ **不要用异常控制流程**  | 比如用 `try/except` 判断字典是否有键（用 `in` 更好） |

# 🎮 九、综合实战：带异常处理的计算器
def calculator():
    try:
        a = float(input("请输入第一个数字："))
        op = input("请输入运算符（+、-、*、/）：")
        b = float(input("请输入第二个数字："))
        
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("除数不能为0")
            result = a / b
        else:
            raise ValueError("无效的运算符！")
        print(f"结果是： {result}")
    except ValueError as e:
        if "could not convert" in str(e):
            print("输入的不是有效数字！")
        else:
            print(f"错误：{e}")
    except ZeroDivisionError as e:
        print(f"错误：{e}")
    except Exception as e:
        print(f"未知错误：{e}")

# 运行计算器
calculator()

# 十、异常处理 + 函数：黄金组合
# - **函数内部**：检测错误 → `raise` 异常
# - **调用处**：用 `try/except` 处理异常
def process_user_input(s):
    if not s.isdigit():
        raise ValueError("必须输入数字")
    return int(s) * 2
# 调用
user_input = input("输入数字：")
try:
    result = process_user_input(user_input)
    print(f"结果是：{result}")
except ValueError as e:
    print(f"错误：{e}")
# ✅ **职责分离**：函数专注逻辑，调用者专注交互！

