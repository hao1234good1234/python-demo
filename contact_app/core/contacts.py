# contacts.py` —— 业务逻辑

from typing import List, Dict

def create_contact(name: str, phone: str) -> Dict[str, str]:
    """
    创建联系人字典
    """
    return {"name": name, "phone": phone}

def add_contact(contacts: List[Dict], name: str, phone: str) -> List[Dict]:
    """
    添加联系人
    返回新列表
    """
    new_contact = create_contact(name, phone)
    return contacts + [new_contact]

def find_contact(contacts: List[Dict], name: str) -> Dict | None:
    """
    根据姓名查找
    """
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return None
# 使用 `if __name__ == "__main__"` 测试模块，这样就可以直接在运行该模块的时候测试功能
if __name__ == "__main__":
    # 直接运行 contacts.py 时测试
    contacts = add_contact([], "测试", "13800138000")
    print(contacts)

