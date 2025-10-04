# contacts.py` —— 业务逻辑
import logging
from typing import List, Dict
logger = logging.getLogger(__name__)

def create_contact(name: str, phone: str) -> Dict[str, str]:
    """
    创建联系人字典
    """
    logger.info(f"成功创建联系人字典：{{'name': {name}, 'phone': {phone}}}")
    return {"name": name, "phone": phone}

def add_contact(contacts: List[Dict], name: str, phone: str) -> List[Dict]:
    """
    添加联系人
    返回新列表
    """
    new_contact = create_contact(name, phone)
    logger.info(f"成功添加联系人：{name} - {phone}")
    return contacts + [new_contact]

def find_contact(contacts: List[Dict], name: str) -> Dict | None:
    """
    根据姓名查找
    """
    for contact in contacts:
        if contact["name"] == name:
            logger.info(f"成功找到联系人：{name} - {contact['phone']}")
            return contact
    logger.info(f"未找到联系人：{name}")
    return None

def delete_contact(contacts: List[Dict], name: str) -> List[Dict]:
    """
    删除联系人
    返回新列表
    """
    # contacts = contacts.copy()
    # for i, contacts in enumerate(contacts):
    #     if contacts["name"] == name:
    #         contacts.pop(i)
    #         logger.info(f"成功删除联系人：{name}")
    #         return contacts # 返回新列表
    # logger.info(f"未找到联系人：{name}")
    # return contacts # 返回原列表

    # 以上是复杂的业务逻辑，下面是简单的业务逻辑
    return [contact for contact in contacts if contact["name"] != name] # 过滤掉 name 相同的联系人，返回新列表
    
# 使用 `if __name__ == "__main__"` 测试模块，这样就可以直接在运行该模块的时候测试功能
# if __name__ == "__main__":
#     # 直接运行 contacts.py 时测试
#     contacts = add_contact([], "测试", "13800138000")
#     print(contacts)

