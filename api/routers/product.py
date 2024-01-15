from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm.session import Session

from api.models.product import ProductModel
from api.config import db_session

product_router = APIRouter(tags=['Products'])

@product_router.get('/products')
def get_products(db: Session = Depends(db_session)):
    data = db.query(ProductModel).order_by(ProductModel.description.asc()).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(data))