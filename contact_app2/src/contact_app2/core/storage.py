# storage.py` —— 文件存储

import json
import logging
from pathlib import Path
from typing import List, Dict

logger = logging.getLogger(__name__)
DATA_FILE = Path("data/contacts.json")

def ensure_data_dir():
    """
    确保data目录存在
    """
    logger.debug(f"确保data目录存在：{DATA_FILE.parent}")
    DATA_FILE.parent.mkdir(exist_ok=True)
def save_contacts(contacts: List[Dict]):
    """
    保存联系人到json
    """
    ensure_data_dir()
    logger.debug(f"保存联系人到json：{DATA_FILE}")
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
def load_contacts() -> List[Dict]:
    """
    从json文件加载联系人
    """
    if not DATA_FILE.exists():
        return []
    logger.debug(f"从json文件加载联系人：{DATA_FILE}")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)