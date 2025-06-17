# Inventory Management System (FastAPI)

## Features
- User login (JWT)
- Add, update, get products
- Postman collection included
- Ready for deployment on Render

## Setup
```bash
pip install -r requirements.txt
python
>>> from database import Base, engine
>>> import models
>>> Base.metadata.create_all(bind=engine)
exit()
uvicorn main:app --reload
```
