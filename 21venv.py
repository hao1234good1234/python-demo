# # 1. 进入项目目录
# cd contact_app

# # 2. 创建虚拟环境
# python -m venv venv

# # 3. 激活
# venv\Scripts\activate   # Windows

# # 4. 安装依赖（假设你用了 json，其实不需要第三方库，但演示流程）
# pip install  # （这里其实可以跳过，因为没用第三方库） 会报错，可以不执行这一步
# pip install requests   #下载安装 requests库
# # 验证是否安装成功
# pip list | findstr requests

# # 5. 生成依赖清单 requirements.txt（即使为空也建议保留）（重要！）
# pip freeze > requirements.txt

# # 6. 运行项目
# python -m contact_app.main

# # 7. 退出
# deactivate

# # 8. .gitignore 忽略 venv/
# venv/
# ENV/
# env/

# # 9. git拉取项目
# cd contact_app_clone

# # 10. 创建虚拟环境
# python -m venv venv

# # 11. 激活虚拟环境
# venv\Scripts\activate 

# # 12. 从依赖清单安装依赖库
# pip install -r requirements.txt


# 注意：
# ⚠️ 如果windows powershell 报错“无法加载脚本”，先运行：
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser