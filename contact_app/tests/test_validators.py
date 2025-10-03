# 单元测试
import pytest
from utils.validators import is_valid_phone, is_valid_name

# def test_valid_phone():
#     """
#     测试有效手机号
#     """
#     assert is_valid_phone("13899993333") == True
#     assert is_valid_phone("15912345678") == True

# def test_invalid_phone():
#     assert is_valid_phone("125") == False         # 太短
#     assert is_valid_phone("23819392910") == False # 不以1开头
#     assert is_valid_phone("135902203a0") == False # 含字母
#     assert is_valid_phone("") == False              # 空字符串

# 1. **参数化测试**（避免重复代码）
@pytest.mark.parametrize("phone, expected",
                         [("13899993333", True),
                          ("15912345678", True),
                          ("125", False),
                          ("23819392910", False),
                          ("135902203a0", False),
                          ("", False)])
def test_valid_phone(phone, expected):
    assert is_valid_phone(phone) == expected

def test_valid_name():
    assert is_valid_name("张三") == True
    assert is_valid_name("") == False