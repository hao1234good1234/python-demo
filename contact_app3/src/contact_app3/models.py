import json
from datetime import datetime
class Contact:
    def __init__(self, name, phone, email=None, created_at=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.created_at = created_at or datetime.now().isoformat()
    def is_valid(self):
        return bool(self.name) and len(self.phone) == 11 and self.phone.isdigit()
    def to_dict(self): 
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "created_at": self.created_at
        }
    @classmethod # 类方法
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            phone= data.get("phone"),
            email=data.get("email"),
            created_at=data.get("created_at")
        )
    def __str__(self):
        return f"{self.name} - {self.phone}"

    def __repr__(self):
        return f"Contact(name='{self.name}', phone='{self.phone}')"
        
        