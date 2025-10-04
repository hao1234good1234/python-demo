"""
**专业项目中，`print()` 是“临时草稿”，`logging` 是“正式文档”。**
"""

# ✅ 第一步：基础用法（5 行上手）

# 在任意 Python 文件中：


import logging

# 1. 配置日志（只需一次）
logging.basicConfig(level=logging.INFO)

# 2. 获取日志器
logger = logging.getLogger(__name__)

# 3. 使用
logger.info("程序启动")
logger.warning("用户名为空")
logger.error("保存失败")

# 输出：
# INFO:__main__:程序启动
# WARNING:__main__:用户名为空
# ERROR:__main__:保存失败

# ✅ 第二步：为 `contact_app2` 添加日志

# 1️⃣ 修改 `cli.py`：添加日志配置


# cli.py
import logging
import click

# 🔧 配置日志：同时输出到控制台和文件
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("contact_app.log", encoding="utf-8"),  # 写入文件
        logging.StreamHandler()  # 输出到终端
    ]
)

# 获取当前模块的日志器
logger = logging.getLogger(__name__)


# > ✅ 这样所有日志会同时出现在终端和 `contact_app.log` 文件中。



# 2️⃣ 在命令中使用日志（替代 `print`）


# @cli.command()
# @click.argument("name")
# @click.argument("phone")
# def add(name, phone):
#     """添加联系人"""
#     # ✅ 记录用户操作
#     logger.info(f"收到添加请求: name={name}, phone={phone}")
    
#     # 验证
#     if not is_valid_name(name):
#         logger.warning(f"姓名无效: '{name}'")  # ⚠️ 警告
#         click.echo("❌ 姓名不能为空", err=True)
#         raise click.Abort()
    
#     if not is_valid_phone(phone):
#         logger.warning(f"手机号无效: '{phone}'")
#         click.echo("❌ 手机号应为11位数字", err=True)
#         raise click.Abort()
    
#     try:
#         contacts = load_contacts()
#         contacts = add_contact(contacts, name, phone)
#         save_contacts(contacts)
#         logger.info(f"✅ 成功添加联系人: {name} - {phone}")  # ✅ 成功记录
#         click.echo(f"✅ 添加成功: {name} - {phone}")
#     except Exception as e:
#         # ❌ 记录错误 + 完整堆栈
#         logger.error(f"保存联系人失败: {e}", exc_info=True)
#         click.echo("❌ 系统错误，请查看日志", err=True)
#         raise click.Abort()

# ✅ 第三步：理解日志级别（5 级）

# | 级别       | 用途         | 何时用                       |
# | ---------- | ------------ | ---------------------------- |
# | `DEBUG`    | 详细调试信息 | 开发时追踪流程               |
# | `INFO`     | 一般信息     | 记录关键操作（如“添加成功”） |
# | `WARNING`  | 警告         | 异常输入但程序可继续         |
# | `ERROR`    | 错误         | 功能失败（如文件写入失败）   |
# | `CRITICAL` | 严重错误     | 系统崩溃（极少用）           |

# 控制显示级别：
# 开发时：显示所有
logging.basicConfig(level=logging.DEBUG)

# 生产时：只显示 WARNING 以上
logging.basicConfig(level=logging.WARNING)

# ✅ 第四步：记录错误堆栈（关键！） 
# 当程序出错时，你不仅想知道“哪里错了”，还要知道“**为什么错**”。
# try:
#     save_contacts(contacts)
# except IOError as e:
#     # ✅ exc_info=True 会自动打印完整 traceback
#     logger.error("无法保存联系人", exc_info=True)

# 日志中会包含：
# ERROR - 无法保存联系人
# Traceback (most recent call last):
#   File "cli.py", line 45, in add
#     save_contacts(contacts)
#   File ".../storage.py", line 10, in save_contacts
#     with open("contacts.json", "w") as f:
# PermissionError: [Errno 13] Permission denied
# 🔍 这对排查生产问题 **至关重要**！

# ✅ 第五步：最佳实践总结
# | 原则                        | 说明                               |
# | --------------------------- | ---------------------------------- |
# | **用户反馈用 `click.echo`** | 用户看到的是友好提示               |
# | **系统行为用 `logging`**    | 开发者看日志排查问题               |
# | **错误必须记录堆栈**        | `logger.error(..., exc_info=True)` |
# | **日志写入文件**            | 方便事后分析                       |
# | **不要用 `print()`**        | 除非临时调试（记得删）             |


# ✅ 第六步：进阶（可选）
# 添加 `--debug` 选项
@click.group()
@click.option('--debug', is_flag=True, help="启用调试日志")
def cli(debug):
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("调试模式已开启")
# 使用：
# contact_app2 --debug add Alice 13800138000

# 📁 你的项目现在会生成：
# contact_app2/
# ├── contact_app.log   ← 所有操作记录在这里！
# ├── cli.py
# └── ...