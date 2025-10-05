# storage.py` —— 文件存储

import json
import logging
from pathlib import Path
from typing import List, Dict
import os
from dotenv import load_dotenv
from contact_app3.models import Contact

logger = logging.getLogger(__name__)
# DATA_FILE = Path("data/contacts.json")

load_dotenv()
DATA_DIR = Path(os.getenv("DATA_DIR", "data"))
CONTACTS_FILE_NAME = os.getenv("CONTACTS_FILE_NAME", "contacts_data.json")
CONTACTS_FILE = DATA_DIR / CONTACTS_FILE_NAME

def save_contacts(contacts: List[Contact]):  # 传入的是Contact对象列表
    """
    保存联系人到json
    """
    logger.debug(f"保存联系人到json：{CONTACTS_FILE}")

    DATA_DIR.mkdir(exist_ok=True)
    data=[contact.to_dict() for contact in contacts] # 将对象列表转换为字典列表存到json文件中
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_contacts() -> List[Contact]:  # 返回的是Contact对象列表
    """
    从json文件加载联系人
    """
    logger.debug(f"从json文件加载联系人：{CONTACTS_FILE}")
    if not CONTACTS_FILE.exists():
        return []
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Contact.from_dict(item) for item in data]