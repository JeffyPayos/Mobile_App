from fastapi import FastAPI
from pydantic import BaseModel
import uuid


app = FastAPI(title="GoTo Feed – Backend", version="0.1.0")

@app.get("/")
def health():
    return {"ok": True}
# --- Router einbinden (Auth) ---
try:
    from .routers.auth import router as auth_router
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
except Exception:
    # Solange die Datei noch nicht existiert, darf der Import nicht crashen.
    pass
try:
    from .routers.media import router as media_router
    app.include_router(media_router, prefix="/media", tags=["media"])
except Exception:
    pass

from .db import init_db

@app.on_event("startup")
def on_startup():
    init_db()
