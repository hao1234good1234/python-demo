# 负责业务逻辑
from .storage import load_contacts, save_contacts

def add_contact(name, phone):
    contacts = load_contacts()
    contacts[name] = phone
    save_contacts(contacts)
    print(f"✅ {name} 已添加")

def get_all_contacts():
    return load_contacts()