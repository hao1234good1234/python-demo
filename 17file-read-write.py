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
    print(content)
except FileNotFoundError as e:
    print(f"文件不存在：{e}")
# 3. 追加内容（不覆盖）
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("2025-10-10 19:40:30 用户登录\n")

# 🔸 `"a"` 模式：在文件末尾追加，常用于日志！