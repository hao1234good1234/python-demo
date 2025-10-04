# storage.py` —— 文件存储

import json
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path("data/contacts.json")

def ensure_data_dir():
    """
    确保data目录存在
    """
    DATA_FILE.parent.mkdir(exist_ok=True)

def save_contacts(contacts: List[Dict]):
    """
    保存联系人到json
    """
    ensure_data_dir()
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

def load_contacts() -> List[Dict]:
    """
    从json文件加载联系人
    """
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)