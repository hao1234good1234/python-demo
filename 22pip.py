"""
pip 与包管理（始终在虚拟环境中使用 `pip`！）
"""

# 🧱 一、什么是 `pip`？

# ✅ **`pip` = Python 的“应用商店客户端”**  

# - 从 [PyPI（Python Package Index）](https://pypi.org/) 下载安装包
# - 自动处理依赖关系（比如装 `requests` 会自动装 `urllib3`）
# - 支持安装、升级、卸载、查看包

# 🛠️ 二、常用 `pip` 命令速查表
# | 命令                              | 作用                                        | 示例                              |
# | --------------------------------- | ------------------------------------------- | --------------------------------- |
# | `pip install 包名`                | 安装包                                      | `pip install requests`            |
# | `pip install 包名==版本号`        | 安装指定版本                                | `pip install requests==2.25.1`    |
# | `pip install -r requirements.txt` | 批量安装依赖                                | `pip install -r requirements.txt` |
# | `pip list`                        | 列出已安装的包                              | `pip list`                        |
# | `pip show 包名`                   | 查看包详情（版本、位置、依赖）              | `pip show requests`               |
# | `pip uninstall 包名`              | 卸载包                                      | `pip uninstall requests`          |
# | `pip freeze`                      | 输出精确依赖列表（用于 `requirements.txt`） | `pip freeze > requirements.txt`   |
# | `pip search 关键词`               | 搜索包（⚠️ 2023 年后已禁用）                 | ❌ 不可用                          |
# | `pip install --upgrade pip`       | 升级 pip 自身                               | `pip install --upgrade pip`       |

## 🌰 三、实战：安装并使用 `requests`（最常用 HTTP 库）

### 场景：从网络获取数据（比如天气、API）

#### 步骤 1：激活虚拟环境

# cd your-project
# venv\Scripts\activate   # Windows

#### 步骤 2：安装 `requests`

# pip install requests

# ✅ 成功输出：

# Collecting requests
#   Downloading requests-2.31.0-py2.py3-none-any.whl (63 kB)
# Installing collected packages: requests
# Successfully installed requests-2.31.0

#### 步骤 3：在代码中使用
import requests
response = requests.get("https://httpbin.org/json")
data = response.json()
print(data["slideshow"]["title"]) # 输出：Sample Slide Show

# ✅ 这就是 **“安装即用”** 的魅力！

## 📦 四、`requirements.txt` —— 项目的“依赖清单”

### 为什么需要它？

# - 让别人（或未来的你）能**一键复现相同环境**
# - 避免“在我电脑上能跑”的问题

### 生成依赖清单

# pip freeze > requirements.txt

# 📄 `requirements.txt` 内容示例：

# certifi==2024.8.30
# charset-normalizer==3.3.2
# idna==3.7
# requests==2.31.0
# urllib3==2.2.2

### 别人如何复现你的环境？

# 1. 创建虚拟环境
# python -m venv venv

# 2. 激活
# venv\Scripts\activate

# 3. 安装所有依赖
# pip install -r requirements.txt

# ✅ 完美复现！

# 🔒 五、版本控制策略（重要！）
# | 写法                  | 含义           | 适用场景                         |
# | --------------------- | -------------- | -------------------------------- |
# | `requests`            | 安装最新版     | 个人小项目、快速原型             |
# | `requests==2.31.0`    | 锁定精确版本   | **生产项目、团队协作** ✅         |
# | `requests>=2.25,<3.0` | 允许小版本更新 | 希望自动修复 bug，但不破坏兼容性 |

# ✅ **最佳实践：生产项目用 `==` 锁定版本！**



# 🧪 六、常见问题 & 解决方案

# ❌ 问题 1：`pip install` 太慢（国内网络）

# ✅ 解决：使用国内镜像源（如清华、阿里云）

# 临时使用清华源
# pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 永久配置（推荐）
# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/

# > 🌐 常用镜像：
# >
# > - 清华：`https://pypi.tuna.tsinghua.edu.cn/simple/`
# > - 阿里云：`https://mirrors.aliyun.com/pypi/simple/`
# > - 豆瓣：`https://pypi.douban.com/simple/`


### ❌ 问题 2：权限错误（Windows/macOS/Linux）

# ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied

# ✅ 原因：没用虚拟环境，试图修改系统 Python  
# ✅ 解决：**始终在虚拟环境中使用 `pip`！**


### ❌ 问题 3：包找不到（拼写错误）

# ERROR: Could not find a version that satisfies the requirement requets

# ✅ 检查拼写：`requets` → `requests`  
# ✅ 去 [PyPI](https://pypi.org/) 搜索正确包名

#  七、探索 PyPI —— 发现好用的库
# 推荐几个初学者友好库：
# | 库名            | 用途           | 安装命令                    |
# | --------------- | -------------- | --------------------------- |
# | `requests`      | 发送 HTTP 请求 | `pip install requests`      |
# | `click`         | 创建命令行工具 | `pip install click`         |
# | `python-dotenv` | 管理环境变量   | `pip install python-dotenv` |
# | `rich`          | 彩色终端输出   | `pip install rich`          |
# | `black`         | 自动格式化代码 | `pip install black`         |

# 🎯 试试这个彩蛋：
from rich import print
print("[bold red]Hello[/bold red], [green]World[/green]!")

# 📌 八、最佳实践总结

# 1. **永远在虚拟环境中使用 `pip`**
# 2. **安装后立即生成 `requirements.txt`**
# 3. **生产项目锁定精确版本（`==`）**
# 4. **国内用户配置镜像源提速**
# 5. **不要用 `sudo pip`（Linux/macOS）**

# 🎯 九、小练习
# 1. 安装 requests 和 rich
# 2. 用 rich 打印彩色文本
# 3. 生成 requirements.txt
# 4. 卸载 rich
# pip install requests rich

# test.py
from rich import print
print("[bold blue]安装成功！[/bold blue]")

# pip freeze > requirements.txt
# pip uninstall rich