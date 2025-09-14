import uuid
from typing import Dict

# super-einfacher In-Memory-Store (später ersetzen wir das durch DB/JWT)
USERS: Dict[str, dict] = {}

def login(email: str) -> dict:
    token = str(uuid.uuid4())
    USERS[token] = {"id": str(uuid.uuid4()), "email": email}
    return {"token": token, "user_id": USERS[token]["id"]}
