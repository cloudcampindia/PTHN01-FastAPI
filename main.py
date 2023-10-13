from fastapi import Depends, FastAPI
from database import session, engine
from sqlalchemy.orm import Session

import models
import crud
import schemas

app = FastAPI(
    title="ECommerce API",
    description="An API for managing Orders placed by customers",
    docs_url='/'
)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=engine)

@app.get("/suppliers", response_model=list[schemas.SuppliersData])
def read_suppliers(db: Session=Depends(get_db)):
    suppliers_data = crud.read_suppliers(db)
    return suppliers_data

@app.get("/orders/{order_id}")
def get_order(order_id: int=10248, db: Session=Depends(get_db)):
    order_data = crud.get_order(db, order_id)
    return order_data