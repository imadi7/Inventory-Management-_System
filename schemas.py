from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ProductCreate(BaseModel):
    name: str
    type: str
    sku: str
    image_url: str
    description: str
    quantity: int
    price: float

class ProductUpdateQty(BaseModel):
    quantity: int
