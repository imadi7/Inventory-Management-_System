from pydantic import BaseModel
import os

class Settings(BaseModel):
    # Use a secure secret key from environment or fallback (for dev only)
    authjwt_secret_key: str = os.environ["JWT_SECRET_KEY"]

# Required for fastapi-jwt-auth to access settings
from fastapi_jwt_auth import AuthJWT

@AuthJWT.load_config
def get_config():
    return Settings()
