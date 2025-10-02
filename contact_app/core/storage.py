# 负责 JSON 读写
import json
from pathlib import Path

DATA_FILE = Path("contacts.json")

def load_contacts():
    if not DATA_FILE.exists():
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_contacts(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)