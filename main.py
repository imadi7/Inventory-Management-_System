from fastapi import FastAPI
from auth import router as auth_router
from crud import router as product_router
import uvicorn

app = FastAPI(title="Inventory Management System")

app.include_router(auth_router)
app.include_router(product_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
