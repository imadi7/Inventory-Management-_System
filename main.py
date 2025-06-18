from fastapi import FastAPI
from auth import router as auth_router
from crud import router as product_router
import uvicorn
from database import engine
import models

# Create all database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app = FastAPI(title="Inventory Management System")

@app.get("/")
def read_root():
    return {"message": "Inventory Management System API is live 🚀"}
app.include_router(auth_router)
app.include_router(product_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000, reload=True)
