"""
命令行工具（click）
现在要让项目**真正可用**——变成一个像 `git`、`pip` 一样的命令行工具！
"""

# ✅ 学完这节课，你就能在终端输入：  

# contact add Alice 13800138000
# contact list
# contact find Alice

# 而不是只能 `python main.py`！


# 🎯 本课目标：用 `click` 把你的通讯录变成专业 CLI 工具

# ✅ 学完你能：

# - 用 `click` 快速构建命令行接口
# - 支持子命令（`add` / `list` / `find`）
# - 自动处理参数、类型校验、帮助文档
# - 全局安装自己的工具（`pip install -e .`）

# 🔧 一、为什么选 `click`？
# | 对比项   | 手写 `sys.argv` | `argparse`（标准库） | `click`（推荐）              |
# | -------- | --------------- | -------------------- | ---------------------------- |
# | 代码量   | 多、易错        | 中等                 | **极少**                     |
# | 子命令   | 难实现          | 复杂                 | **天然支持**                 |
# | 类型校验 | 手动写          | 部分支持             | **自动**（如 `--count INT`） |
# | 帮助文档 | 手动写          | 自动生成             | **自动生成 + 彩色**          |
# | 开发体验 | 痛苦            | 一般                 | **愉悦**                     |
# ✅ **行业标准**：Flask、Black、Poetry 等知名工具都用 `click`

# 📦 二、安装 click

# 在你的虚拟环境中运行：

#退出当前的虚拟环境
# deactivate

# 切换到你的新的项目目录
# cd contact_app

# 创建虚拟环境
# python -m venv venv

# 激活虚拟环境
# venv\Scripts\activate

# 安装 click
# pip install click

# 更新依赖清单
# pip freeze > requirements.txt

# 📂 三、项目结构更新
# contact_app/
# ├── venv/                   ← ✅ 虚拟环境放这里（推荐！）
# ├── contact_app/            ← 重命名核心代码为包（重要！）
# │   ├── __init__.py
# │   ├── core/
# │   │   ├── __init__.py
# │   │   ├── contacts.py
# │   │   └── storage.py
# │   └── utils/
# │       ├── __init__.py
# │       └── validators.py
# ├── tests/                  ← 测试保持不变
# ├── cli.py                  ← 新增：命令行入口
# ├── setup.py                ← 新增：让项目可安装
# ├── requirements.txt
# └── .gitignore

# 💡 **关键变化**：  

# - 把原来的 `core/`、`utils/` 移入 `contact_app/` 包  
# - 这样才能通过 `pip install -e .` 全局安装

# 🧩 四、实战：用 click 构建 CLI
# 步骤 1：创建 `cli.py`（命令行入口）

# ✅ **click 的魔法**：
# - `@click.group()`：定义主命令 `contact`
# - `@cli.command()`：定义子命令 `add` / `list` / `find`
# - `@click.argument()`：位置参数（必填）
# - `click.echo()`：带颜色的输出（自动适配终端）

# cli.py
# import click
# from contact_app.core.contacts import add_contact, find_contact
# from contact_app.core.storage import load_contacts, save_contacts
# from contact_app.utils.validators import is_valid_name, is_valid_phone

# @click.group()
# def cli():
#     """通讯录管理工具"""
#     pass

# @cli.command()
# @click.argument('name')
# @click.argument('phone')
# def add(name, phone):
#     """添加联系人: contact add Alice 13800138000"""
#     if not is_valid_name(name):
#         click.echo("❌ 姓名不能为空", err=True)
#         raise click.Abort()
#     if not is_valid_phone(phone):
#         click.echo("❌ 电话格式无效（应为11位手机号）", err=True)
#         raise click.Abort()
    
#     contacts = load_contacts()
#     contacts = add_contact(contacts, name, phone)
#     save_contacts(contacts)
#     click.echo(f"✅ 已添加: {name} - {phone}")

# @cli.command()
# def list():
#     """列出所有联系人"""
#     contacts = load_contacts()
#     if not contacts:
#         click.echo("📭 通讯录为空")
#         return
    
#     for i, contact in enumerate(contacts, 1):
#         click.echo(f"{i}. {contact['name']} - {contact['phone']}")

# @cli.command()
# @click.argument('name')
# def find(name):
#     """查找联系人: contact find Alice"""
#     contacts = load_contacts()
#     found = find_contact(contacts, name)
#     if found:
#         click.echo(f"🔍 找到: {found['name']} - {found['phone']}")
#     else:
#         click.echo(f"❌ 未找到联系人: {name}", err=True)

# if __name__ == '__main__':
#     cli()

# 步骤 2：创建 `setup.py`（让项目可安装）

# setup.py
# from setuptools import setup, find_packages

# setup(
#     name="contact-app",
#     version="0.1.0",
#     packages=find_packages(),
#     install_requires=[
#         "click",
#     ],
#     entry_points={
#         'console_scripts': [
#             'contact=cli:cli',  # 命令名=模块:函数
#         ],
#     },
#     python_requires=">=3.7",
# )

# 🔑 **关键行**：  
# 'contact=cli:cli'
# 表示：  
# 终端输入 `contact` → 执行 `cli.py` 中的 `cli()` 函数

# 步骤 3：重命名核心代码为包
# 把原来的：
# core/ → contact_app/core/
# utils/ → contact_app/utils/
# 并确保 `contact_app/__init__.py` 存在（可为空）。
# 💡 **为什么？**  
# `setup.py` 会把 `contact_app/` 作为可安装包，`cli.py` 在顶层调用它。

# 🚀 五、安装并测试你的 CLI 工具
# 在项目根目录运行（`contact_app/` 的父目录）：

# 激活虚拟环境
# venv\Scripts\activate

# 以“开发模式”安装（`-e` 模式已自动更新，无需重装！修改代码立即生效）
# pip install -e .

# 现在可以全局使用 contact 命令！
# contact --help

# 如果出现问题，可以尝试卸载安装的包

# pip uninstall contact-app --yes 





# ✅ 预期输出：

# Usage: contact [OPTIONS] COMMAND [ARGS]...

#   通讯录管理工具

# Options:
#   --help  Show this message and exit.

# Commands:
#   add    添加联系人: contact add Alice 13800138000
#   find   查找联系人: contact find Alice
#   list   列出所有联系人

# 🧪 测试命令：
# 添加联系人
# contact add Alice 13800138000

# 列出
# contact list

# 查找
# contact find Alice

#  📝 六、常见问题解决

# ❌ 问题 1：`contact : 无法识别命令`

# 原因：没安装，或不在虚拟环境中

# ✅ 解决：

# 确保在虚拟环境中
# venv\Scripts\activate

# 确保已安装
# pip install -e .

# ❌ 问题 2：`ModuleNotFoundError: No module named 'contact_app'`

# 原因：`contact_app/` 包结构不对

# ✅ 检查：

# - 项目根目录有 `setup.py`
# - `contact_app/` 目录下有 `__init__.py`
# - `cli.py` 在项目根目录（和 `setup.py` 同级）

# ❌ 问题 3：修改代码后命令没更新

# ✅ 解决：`-e` 模式已自动更新，**无需重装**！


# 🎨 七、进阶技巧（可选）

# 1. **添加选项（Options）**

# @click.option('--verbose', '-v', is_flag=True, help="显示详细信息")
# def list(verbose):
#     if verbose:
#         click.echo("正在加载联系人...")

# 2. **自动补全**（bash/zsh）

# 在 cli.py 末尾添加
# cli.add_command(click.shell_completion)
# 然后运行：contact --show-completion bash >> ~/.bashrc

# 3. **彩色输出**

# click.echo(click.style("✅ 成功", fg="green"))
# click.echo(click.style("❌ 错误", fg="red", bold=True))


# 📦 八、项目结构最终版

# your-project-root/          ← 在这里运行 pip install -e .
# ├── contact_app/            ← 可安装的 Python 包
# │   ├── __init__.py
# │   ├── core/
# │   └── utils/
# ├── tests/
# ├── cli.py                  ← CLI 入口
# ├── setup.py                ← 安装配置
# ├── requirements.txt
# └── .gitignore

# > ✅ **现在你的项目符合 Python 打包标准！**

# 可选增强：`click` 默认不支持 `-h`，只支持 `--help`，修改 `cli.py` 使之支持 `-h`
# 在 `@click.group()` 中启用 `-h`
# 修改你的 `cli.py`：
# import click

# @click.group(context_settings=dict(help_option_names=['-h', '--help']))
# def cli():
#     """通讯录管理工具"""
#     pass

# 🔥 这样就同时支持了 `-h` 和 `--help`！


# ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ 
# 输入contact --help 出现问题：No module named 'cli'

# ✅ 核心原因分析
# ⚠️ 你的项目结构可能有问题！
# 你现在的文件结构很可能是这样：
# contact_app2/
# ├── setup.py
# ├── cli.py
# └── contact_app/
#     ├── __init__.py
#     └── ...

# 但是！你在 `setup.py` 中写了：
# packages=find_packages(),
# 👉 `find_packages()` 会自动发现所有包（以 `__init__.py` 存在的目录）——它只找“包”，不会把顶层 `.py` 文件当作模块。
# 所以当你运行 `pip install -e .` 后，`pip` 只会安装 `contact_app` 包，而 **不会安装 `cli.py` 作为可导入的模块**！


# 🧨 关键问题：`cli.py` 没有被正确打包进 `site-packages`
# 即使你写了 `entry_points = {"console_scripts": ["contact_app2=cli:cli"]}`，但如果 `cli.py` 不在 `sys.path` 中，Python 就无法导入它。

# ✅ 正确做法：确保 `cli.py` 被识别为模块
# ✅ 方法一：将 `cli.py` 放在根目录，并使用 `package_dir` 明确指定
# 修改 `setup.py`
from setuptools import setup, find_packages

setup(
    name="contact_app2",
    version="0.1.0",
    packages=find_packages(where="src"),  # 如果你用 src 结构
    package_dir={"": "src"},  # 如果你用 src
    # 或者如果你不用 src，直接：
    # packages=["contact_app"],  # 只打包 contact_app 包
    entry_points={
        "console_scripts": [
            "contact_app2=cli:cli",  # 从 cli.py 导入 cli 函数
        ],
    },
    install_requires=[
        "click==8.3.0",
        "colorama==0.4.6",
    ],
)

# ❌ 但这里有个矛盾：`find_packages()` 找不到 `cli.py`，因为它不是包！

# ✅ 推荐方案：使用 `src` 目录结构 + `package_dir`
# 这是最标准、最推荐的方式。
# ✅ 步骤1：重构项目结构
# contact_app2/
# ├── src/           # 新增，src目录结构
# │   ├── contact_app2/
# │   │   ├── __init__.py    # 必须加，将contact_app2作为包将 `cli.py` 打包进去
# │   │   └── cli.py           ← 放在这里！
# │   └── contact_app/
# │       ├── __init__.py
# │       ├── core/
# │       └── utils/
# ├── setup.py   
# ├── requirements.txt  
# └── venv/                   ← 现在的虚拟环境放这里（推荐！）

# ✅ 现在 `cli.py` 是 `contact_app2.cli` 模块的一部分

# ✅ 步骤2：修改 `setup.py`

from setuptools import setup, find_packages

setup(
    name="contact_app2",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "contact_app2=contact_app2.cli:cli",  # 从 contact_app2.cli 导入 cli
        ],
    },
    install_requires=[
        "click==8.3.0",
        "colorama==0.4.6",
    ],
)
# ✅ 注意：现在是 `contact_app2.cli:cli`，不是 `cli:cli`

# ✅ 步骤3：修改 `src/contact_app2/cli.py`
# src/contact_app2/cli.py
import click
from contact_app.core.contacts import add_contact, find_contact
from contact_app.core.storage import load_contacts, save_contacts
from contact_app.utils.validators import is_valid_name, is_valid_phone

@click.group()
def cli():
    """通讯录管理工具"""
    pass

@click.command()
@click.argument("name")
@click.argument("phone")
def add(name, phone):
    """添加联系人"""
    if not is_valid_name(name):
        click.echo("姓名不能为空", err=True)
        raise click.Abort()
    if not is_valid_phone(phone):
        click.echo("手机号不对（应该为11位）", err=True)
        raise click.Abort()
    contacts = load_contacts()
    contacts = add_contact(contacts, name, phone)
    save_contacts(contacts)
    click.echo(f"添加成功: {name} - {phone}")

@cli.command()
def list():
    """列出所有联系人"""
    contacts = load_contacts()
    if not contacts:
        click.echo("通讯录为空")
        return
    
    for i, contact in enumerate(contacts, start=1):
        click.echo(f"{i}. {contact['name']} - {contact['phone']}")

@cli.command()
@click.argument("name")
def find(name):
    """查找联系人"""
    contacts = load_contacts()
    found = find_contact(contacts, name)
    if found:
        click.echo(f"找到: {found['name']} - {found['0']}")  # 修正 typo
    else:
        click.echo(f"未找到: {name}")

if __name__ == "__main__":
    cli()

# ✅ 步骤4：重新安装
# pip uninstall contact_app2
# pip install -e .

# ✅ 步骤5：测试
# contact_app2 --help
# contact_app2 add Alice 13800138000
# contact_app2 list
# contact_app2 find Alice

# ✅ 应该一切正常！

# 二、click在实际项目中的使用

#  🔹 `click` 在实际项目中会用到吗？
# 答案是：非常常用，尤其是在 Python 的 CLI 工具开发中。
# - `pip`（虽然底层是 `setuptools`，但很多工具用 `click`）
# - `poetry`, `black`, `flake8`, `pytest`, `mypy` 等都用了 `click`
# 💡 比如：`black .` → 就是基于 `click` 构建的


#  🔹 `click` 的优势
# 1. **简单直观**：一行代码定义参数
#    @click.option("--verbose", "-v", is_flag=True)
# 2. **自动帮助**：运行 `--help` 自动显示
# 3. **支持嵌套子命令**：像 `git add`, `git commit`
# 4. **可扩展性强**：支持自定义类型、回调函数
# 5. **社区活跃**：被广泛使用，文档齐全

# 🔹 实际项目例子
# 示例 1：`flask` 命令行
# flask run
# flask db migrate
# flask shell
# → 全部基于 `click` 构建！

# 示例 2：`black` 格式化工具
# black src/
# black --check .
# → 也是 `click` 写的。

# 示例 3：你自己写的 `contact_app2`
# contact_app2 add Alice 123456789
# contact_app2 list
# contact_app2 find Alice
# → 完全可以作为真实项目的一部分！

# 🔹 什么时候不用 `click`？
# - 如果你需要极简的脚本（比如只用 `sys.argv`）
# - 如果你在写 Web 后端（用 Flask/FastAPI），不需要 CLI
# - 如果你对性能要求极高（但 `click` 性能已经很好）