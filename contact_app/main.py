# 程序入口
from .core import add_contact, get_all_contacts
# from contact_app.core import add_contact, get_all_contacts

add_contact("小明", "15639281983")
for name, phone in get_all_contacts().items():
    print(f"{name}: {phone}")