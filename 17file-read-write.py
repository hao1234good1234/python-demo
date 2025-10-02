"""
文件操作 = 让程序“记住”数据
"""

#  一、为什么需要文件操作？
# - 用户输入的数据不能每次重新输 → **存到文件**
# - 程序配置（如主题、语言） → **读取配置文件**
# - 爬虫抓取的数据 → **保存为 CSV/JSON**
# - 错误日志 → **写入日志文件**

# ✅ **核心目标：持久化存储（Persistence）**

# 📝 二、基础：读写文本文件
# 1. 写入文件（覆盖写）
# 写入内容到文件（会覆盖原有内容）
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("Hello, Python!\n")
    f.write("你好，世界！\n")
# 2. 读取文件
try:
    with open("hello.txt", "r", encoding="utf-8") as f:
        content = f.read()  # 读取全部内容
    # print(content)
except FileNotFoundError as e:
    print(f"文件不存在：{e}")
# 3. 追加内容（不覆盖）
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("2025-10-10 19:40:30 用户登录\n")

# 🔸 `"a"` 模式：在文件末尾追加，常用于日志！
#  三、关键概念解析
# ✅ 为什么用 `with open(...) as f`？

# - **自动关闭文件**！即使出错也会关闭
# - 避免忘记 `f.close()` 导致资源泄漏

# ✅ 编码（encoding）为什么重要？

# - 中文、表情等非 ASCII 字符必须指定编码
# - **强烈建议始终写 `encoding="utf-8"`**

# 正确
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("😊 你好")

#  四、读取文件的多种方式
# | 方法            | 说明                         | 适用场景           |
# | --------------- | ---------------------------- | ------------------ |
# | `f.read()`      | 读取**整个文件**为一个字符串 | 小文件，一次性处理 |
# | `f.readline()`  | 读取**一行**                 | 逐行处理大文件     |
# | `f.readlines()` | 读取所有行，返回**列表**     | 需要按行索引       |
# | `for line in f` | **迭代器方式**逐行读取       | 推荐！内存友好     |
# 示例：逐行读取（推荐！）
try:
    with open("hello.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())  # strip() 去掉换行符
except FileNotFoundError as e:
    print(f"文件不存在：{e}")


# 五、实战项目 1：简易记事本
def save_note(filename, content):
    """保存笔记到文件"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content + "\n")
        print(f"笔记保存到{filename}")
    except Exception as e:
        print(f"保存失败：{e}")


def load_note(filename):
    """从文件加载笔记"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"文件不存在：{e}")
        return ""
    except Exception as e:
        print(f"加载失败：{e}")
        return ""


# 使用
filename = "my_note.txt"
note = load_note(filename)
print("当前笔记：\n", note)

new_note = input("请输入新的笔记内容(回车保存)：")
save_note(filename, new_note)

#  六、读写结构化数据：JSON
# JSON 是**最常用的配置/数据交换格式**，Python 原生支持！
# 1. 写入 JSON
import json

data = {"name": "小明", "age": 39, "hobbies": ["读书", "编程"]}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# ✅ `data`：要保存的数据， 必须是 JSON 支持的类型：dict, list, str, int, float, bool, None
# ✅ `f`：文件对象（file），这是你用 open() 打开的文件
# ✅ `ensure_ascii=False`：默认是True,所有非 ASCII 字符（如中文、表情）会被转成 \uXXXX 形式, 设置为False：让中文正常显示
# ✅ `indent=2`： 让 JSON 格式美观（带缩进）,默认行为（indent=None）,所有内容挤在一行,设置为indent=2：每层缩进 2 个空格，其他设置：indent=4 → 缩进 4 空格（也常见），indent="\t" → 用 tab 缩进（不推荐，空格更通用）
# 2. 读取 JSON
import json

try:
    with open("user.json", "r", encoding="utf-8") as f:
        user = json.load(f)
    print(f"用户信息：姓名 - {user['name']}, 年龄 - {user['age']} 岁")
except FileNotFoundError as e:
    print("文件不存在：", e)
except json.JSONDecodeError as e:
    print("Json 格式错误：", e)
# `json.load()` 读文件 → Python 对象（dict/list）
# `json.dump()` 写 Python 对象 → 文件

#  七、实战项目 2：通讯录（用 JSON）
import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        # 如果路径不存在，则创建一个空文件
        open(CONTACTS_FILE, "w", encoding="utf-8").close()
    try:
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ 读取通讯录失败: {e}")
        return {}


def save_contacts(contacts):
    try:
        with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
            json.dump(contacts, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"❌ 保存通讯录失败: {e}")


def add_contact(name, phone):
    contacts = load_contacts()
    contacts[name] = phone
    save_contacts(contacts)
    print(f"✅ {name} 已添加")


def show_contacts():
    contacts = load_contacts()
    if not contacts:
        print("📭 通讯录为空")
        return
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


# 使用
add_contact("李四", "13800138000")
show_contacts()

# 八、常见错误 & 避坑指南

# | 错误                 | 原因                           | 解决方案                              |
# | -------------------- | ------------------------------ | ------------------------------------- |
# | `UnicodeDecodeError` | 未指定 `encoding="utf-8"`      | 始终显式指定编码                      |
# | 文件没保存           | 忘记 `f.write()` 或没用 `with` | 用 `with` + 检查写入逻辑              |
# | 路径错误             | 文件在子目录但没写路径         | 用 `os.path.join("data", "file.txt")` |
# | 权限错误             | 无写入权限                     | 捕获 `PermissionError`                |


#  九、文件操作模式速查表

# | 模式  | 说明                            |
# | ----- | ------------------------------- |
# | `"r"` | 只读（默认）                    |
# | `"w"` | 写入（**覆盖**原文件）          |
# | `"a"` | 追加（在末尾写）                |
# | `"x"` | 创建新文件（若存在则报错）      |
# | `"b"` | 二进制模式（如 `"rb"`, `"wb"`） |
# | `"+"` | 读写（如 `"r+"`）               |

# ✅ 文本文件：用 `"r"`, `"w"`, `"a"`
# ✅ 二进制文件（图片、音频）：用 `"rb"`, `"wb"`


# 十、进阶知识点
# 1. **二进制文件操作（图片、音频、视频）**
# - 模式：`"rb"`（读二进制）、`"wb"`（写二进制）
# - 用于处理非文本文件
# 复制图片
with open("photo.jpeg", "rb") as src:
    with open("copy.jpeg", "wb") as dst:
        dst.write(src.read())
#   ✅ 适用于：文件备份、网络传输、加密等场景
# 2. **路径操作：`pathlib`（现代推荐） vs `os.path`（传统）**
# 旧方式（`os.path`）：
import os

filename = os.path.join("user.json")
if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    data = json.loads(content)
    print(data)
else:
    print("文件不存在")

# 新方式（`pathlib`，Python 3.4+ 推荐）：
from pathlib import Path

# filepath = Path("data") / "user.json"
filepath = Path.cwd() / "user.json"  # 当前工作目录（cwd） （Python 3.9+ 推荐）
if filepath.exists():
    content = filepath.read_text(encoding="utf-8")
    data = json.loads(content)
    print(data)
else:
    print("文件不存在")
# ✅ `pathlib` 更面向对象、更简洁、跨平台兼容性更好！

# 3. **文件元信息：获取大小、修改时间等**
from pathlib import Path
import time

p = Path("user.json")
print(f"文件大小：{p.stat().st_size} 字节")
print(f"修改时间: {time.ctime(p.stat().st_mtime)}")

# 4. **临时文件（`tempfile` 模块）**
# - 安全创建临时文件/目录，用完自动清理
# - 常用于测试、缓存、中间处理
import tempfile

with tempfile.NamedTemporaryFile(mode="w+", delete=True) as tmp:
    tmp.write("hello world")
    tmp.write("临时数据")
    print(f"临时文件路径：{tmp.name}")
# 文件不会自动删除（delete=False），可后续处理, 设置为`delete=True`：自动删除

# 5. **CSV 文件操作（结构化表格数据）**
# 比 JSON 更适合表格（如 Excel 导出）
# Python 内置 `csv` 模块
import csv

# 写csv
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "班级", "成绩"])
    writer.writerow(["zhangsan", "高一3班", 89])
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['姓名']}, {row['班级']},  {row['成绩']}")
# ✅ 适合：数据分析、报表生成、与 Excel 交互

# 6. **文件监控（高级）**
# 监听文件变化（如日志更新）
# 需要第三方库如 `watchdog`
# 伪代码：监听目录变化
# from watchdog.observers import Observer
# ...（较复杂，一般用于后台服务）
# ⚠️ 属于特定场景，初学可跳过


# 7. **压缩文件操作（zip/tar）**
# Python 内置 `zipfile`, `tarfile` 模块
import zipfile

# 创建zip
with zipfile.ZipFile("archive.zip", "w") as zf:
    zf.write("user.json")

# 解压zip
with zipfile.ZipFile("archive.zip", "r") as zf:
    zf.extractall("output/")