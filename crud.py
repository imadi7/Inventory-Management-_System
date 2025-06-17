from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from database import SessionLocal
from schemas import ProductCreate, ProductUpdateQty
from models import Product
from sqlalchemy.orm import Session

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=201)
def add_product(data: ProductCreate, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    product = Product(**data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return {"product_id": product.id}

@router.put("/{product_id}/quantity")
def update_quantity(product_id: int, qty: ProductUpdateQty, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    product = db.query(Product).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.quantity = qty.quantity
    db.commit()
    return {"quantity": product.quantity}

@router.get("/")
def get_products(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    return db.query(Product).all()
