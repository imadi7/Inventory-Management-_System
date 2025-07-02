from pydantic import BaseModel, constr, PositiveInt, PositiveFloat

class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ProductCreate(BaseModel):
    name: constr(max_length=100)
    type: constr(max_length=50)
    sku: constr(max_length=20, regex=r'^[A-Z0-9-]+$')
    image_url: str
    description: str
    quantity: int
    price: float

class ProductUpdateQty(BaseModel):
    quantity: int
