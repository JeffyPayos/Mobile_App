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