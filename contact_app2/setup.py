# 新增：让项目可安装
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