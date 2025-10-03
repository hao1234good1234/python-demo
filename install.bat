@echo off
REM install.bat - 一键安装项目依赖（Windows）
REM 自动创建并激活虚拟环境（可选），然后安装依赖

setlocal

REM === 配置 ===
set VENV_NAME=venv
set REQUIREMENTS=requirements.txt
set MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple/

REM === 检查 Python 是否可用 ===
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] 未找到 Python，请先安装 Python 3.7+
    pause
    exit /b 1
)

REM === 创建虚拟环境（如果不存在）===
if not exist "%VENV_NAME%" (
    echo [INFO] 创建虚拟环境: %VENV_NAME%
    python -m venv %VENV_NAME%
)

REM === 激活虚拟环境并安装依赖 ===
echo [INFO] 激活虚拟环境并安装依赖...
call %VENV_NAME%\Scripts\activate.bat
pip install -r %REQUIREMENTS% -i %MIRROR%

echo.
echo [SUCCESS] 依赖安装完成！
echo 运行以下命令启动项目：
echo   %VENV_NAME%\Scripts\activate.bat ^&^& python main.py
echo.
pause