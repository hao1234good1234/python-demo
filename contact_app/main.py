# main.py —— 程序入口

from core import add_contact, find_contact
from core import load_contacts, save_contacts
from utils.validators import is_valid_name, is_valid_phone

def main():
    contacts = load_contacts()

    # 添加联系人
    name = "zhangsan"
    phone = "13829899843"

    if not is_valid_name(name):
        print("姓名无效")
        return
    if not is_valid_phone(phone):
        print("手机号无效")
        return
    contacts = add_contact(contacts, name, phone)
    save_contacts(contacts)

    # 查找联系人
    founded_contact = find_contact(contacts, name)
    print(f"查找到的联系人: {founded_contact}")

if __name__ == "__main__": # 这句代码的意思是：只有在当前模块为主模块时才会执行
    main()