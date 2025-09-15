from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..schemas.media import MediaCreate, MediaResponse
from ..services import media_service
from ..db import get_session

router = APIRouter()

@router.post("/upload")
def init_upload(filename: str):
    url = media_service.create_presigned_url(filename)
    return {"url": url, "filename": filename}

@router.post("/confirm", response_model=MediaResponse)
def confirm_upload(data: MediaCreate, session: Session = Depends(get_session)):
    return media_service.confirm_upload(data, session)

@router.get("/", response_model=list[MediaResponse])
def list_media(session: Session = Depends(get_session)):
    return media_service.list_media(session)
