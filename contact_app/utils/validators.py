# validators.py` —— 输入校验

import re

def is_valid_phone(phone: str) -> bool:
    """
    简单校验手机号（中国）
    """
    return bool(re.match(r"^1[3-9]\d{9}$", phone))

def is_valid_name(name: str) -> bool:
    """
    校验姓名 （非空）
    """
    return bool(name.strip())
