"""
配置管理（.env）
这是现代 Python 项目管理敏感信息（如 API 密钥、数据库密码）和环境变量的**标准做法**。
"""

# 🎯 为什么需要 `.env`？
# | 问题         | 直接写死在代码中            | 使用 `.env`              |
# | ------------ | --------------------------- | ------------------------ |
# | 密钥泄露风险 | ❌ 高（提交到 Git 就公开了） | ✅ 低（`.env` 不提交）    |
# | 多环境切换   | ❌ 难（要改代码）            | ✅ 容易（换 `.env` 文件） |
# | 团队协作     | ❌ 每个人都要改代码          | ✅ 每人有自己的 `.env`    |
# | 云部署       | ❌ 不安全                    | ✅ 与平台环境变量兼容     |
# 💡 **原则：代码公开，配置私有。**

# ✅ 第一步：安装 `python-dotenv`
# pip install python-dotenv
# 🔧 这个库能自动加载 `.env` 文件中的变量到 `os.environ`。


# ✅ 第二步：创建 `.env` 文件（项目根目录）
# .env
# APP_NAME=ContactApp2
# LOG_LEVEL=INFO
# DATA_DIR=./data
# DATABASE_URL=sqlite:///contacts.db

# 示例：API 密钥（实际项目中会有）
# SMS_API_KEY=sk-xxxxx
# EMAIL_PASSWORD=your_password

# ⚠️ **重要：把 `.env` 加入 `.gitignore`！**
# .gitignore
# .env
# ✅ 第三步：在代码中加载配置
# 方式 1：在程序入口加载（推荐）
# cli.py
import os
from dotenv import load_dotenv

# 🔑 加载 .env 文件（只做一次！）
load_dotenv()

# 现在可以用 os.getenv() 读取
APP_NAME = os.getenv("APP_NAME", "ContactApp")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DATA_DIR = os.getenv("DATA_DIR", "./data")

print(f"应用名称: {APP_NAME}")
print(f"日志级别: {LOG_LEVEL}")


# 方式 2：封装成配置模块（更专业）
# src/contact_app/config.py
import os
from dotenv import load_dotenv

# 加载 .env（只加载一次）
load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "ContactApp")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    DATA_DIR: str = os.getenv("DATA_DIR", "./data")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///contacts.db")

    # 类型转换示例
    @property
    def debug(self) -> bool:
        return os.getenv("DEBUG", "false").lower() in ("true", "1", "yes")

settings = Settings()

# 然后在其他文件中使用：
# core/storage.py
from contact_app.config import settings

def get_data_path():
    return settings.DATA_DIR

# ✅ 第四步：在 `contact_app2` 中实践
# 场景：把日志文件路径、数据目录改成可配置

# 1. 修改 `.env`
# LOG_FILE=contact_app.log
# DATA_DIR=./contacts_data
# LOG_LEVEL=DEBUG

# 2. 修改 `cli.py` 的日志配置
# cli.py
import logging
import os
from dotenv import load_dotenv

load_dotenv()  # 加载 .env

# 从环境变量读取配置
LOG_FILE = os.getenv("LOG_FILE", "contact_app.log") 
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# 配置日志
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)


# 3. 修改数据存储路径
# core/storage.py
# import os
# from dotenv import load_dotenv

# load_dotenv()
# DATA_DIR = os.getenv("DATA_DIR", "./data")
# CONTACTS_FILE = os.path.join(DATA_DIR, "contacts.json")

# def save_contacts(contacts):
#     os.makedirs(DATA_DIR, exist_ok=True)  # 自动创建目录
#     with open(CONTACTS_FILE, "w") as f:
#         json.dump(contacts, f, ensure_ascii=False, indent=2)

# ✅ 第五步：团队协作 & 部署

# 1. 提供 `.env.example`（提交到 Git）
# .env.example
# APP_NAME=ContactApp2
# LOG_LEVEL=INFO
# LOG_FILE=contact_app.log
# DATA_DIR=./data
# SMS_API_KEY=your_api_key_here
# ✅ 新成员复制 `.env.example` 为 `.env`，填入自己的值。

# 2. 生产环境用系统环境变量
# 在服务器上，可以直接设置环境变量，**不需要 `.env` 文件**：
# export LOG_LEVEL=WARNING
# export DATA_DIR=/var/lib/contact_app
# contact_app2 add Alice 13800138000
# ✅ `python-dotenv` 会优先使用系统环境变量，其次才是 `.env` 文件。


# ✅ 第六步：安全最佳实践
# | 建议                      | 说明                                             |
# | ------------------------- | ------------------------------------------------ |
# | **永远不要提交 `.env`**   | 加入 `.gitignore`                                |
# | **不要在代码中写死密钥**  | 全部通过 `os.getenv()` 读取                      |
# | **提供 `.env.example`**   | 帮助团队成员快速上手                             |
# | **敏感信息用 vault 管理** | 大型项目用 HashiCorp Vault / AWS Secrets Manager |
# | **验证配置是否存在**      | 启动时检查必填项                                 |

# 启动时验证配置（可选）
# cli.py
required_vars = ["DATABASE_URL"]
for var in required_vars:
    if not os.getenv(var):
        raise RuntimeError(f"缺少环境变量: {var}")
    
# ✅ 总结：你应该怎么做？
# 1. ✅ 安装 `python-dotenv`
# 2. ✅ 创建 `.env` 文件（**不提交**）
# 3. ✅ 创建 `.env.example`（**提交**）
# 4. ✅ 在 `cli.py` 开头 `load_dotenv()`
# 5. ✅ 用 `os.getenv("KEY", "default")` 读取配置
# 6. ✅ 把路径、密钥、开关等都移到 `.env`

## 🎁 附：完整 `.env` + `.gitignore` 示例

### `.env`

# DEBUG=false
# LOG_LEVEL=INFO
# LOG_FILE=app.log
# DATA_DIR=./data
# SMS_API_KEY=sk-xxxxx

### `.gitignore`

# .env
# __pycache__/
# *.pyc
# venv/
# *.log
# contact_app2.egg-info/

### `.env.example`

# DEBUG=false
# LOG_LEVEL=INFO
# LOG_FILE=app.log
# DATA_DIR=./data
# SMS_API_KEY=your_sms_api_key_here


# 现在你的项目已经具备 **专业级配置管理能力**！