import boto3
from sqlmodel import Session, select
from ..models.media import Media
from ..schemas.media import MediaCreate
from ..config import settings

# S3 Client vorbereiten
def get_s3_client():
    return boto3.client(
        "s3",
        endpoint_url=settings.s3_endpoint,
        aws_access_key_id=settings.s3_access_key,
        aws_secret_access_key=settings.s3_secret_key,
        region_name=settings.s3_region,
    )

def create_presigned_url(filename: str) -> str:
    s3 = get_s3_client()
    return s3.generate_presigned_url(
        "put_object",
        Params={"Bucket": settings.s3_bucket, "Key": filename},
        ExpiresIn=3600,
    )

def confirm_upload(data: MediaCreate, session: Session) -> Media:
    url = f"{settings.s3_endpoint}/{settings.s3_bucket}/{data.filename}"
    media = Media(filename=data.filename, url=url, user_id=data.user_id)
    session.add(media)
    session.commit()
    session.refresh(media)
    return media

def list_media(session: Session):
    return session.exec(select(Media)).all()
