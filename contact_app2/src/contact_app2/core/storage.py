# storage.py` —— 文件存储

import json
import logging
from pathlib import Path
from typing import List, Dict
import os
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
# DATA_FILE = Path("data/contacts.json")

load_dotenv()
DATA_DIR = os.getenv("DATA_DIR", "./data")
CONTACTS_FILE = os.path.join(DATA_DIR, "contacts.json")

def ensure_data_dir():
    """
    确保data目录存在
    """
    # logger.debug(f"确保data目录存在：{DATA_FILE.parent}")
    # DATA_FILE.parent.mkdir(exist_ok=True)

    logger.debug(f"确保data目录存在：{DATA_DIR}")
    os.makedirs(DATA_DIR, exist_ok=True) # 自动创建目录

def save_contacts(contacts: List[Dict]):
    """
    保存联系人到json
    """
    ensure_data_dir()
    # logger.debug(f"保存联系人到json：{DATA_FILE}")
    # with open(DATA_FILE, "w", encoding="utf-8") as f:
    #     json.dump(contacts, f, ensure_ascii=False, indent=2)

    logger.debug(f"保存联系人到json：{CONTACTS_FILE}")
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)


def load_contacts() -> List[Dict]:
    """
    从json文件加载联系人
    """
    # if not DATA_FILE.exists():
    #     return []
    # logger.debug(f"从json文件加载联系人：{DATA_FILE}")
    # with open(DATA_FILE, "r", encoding="utf-8") as f:
    #     return json.load(f)

    logger.debug(f"从json文件加载联系人：{CONTACTS_FILE}")
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)