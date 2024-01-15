from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from api.models.product import ProductModel
from api.config import Session

product_router = APIRouter(tags=['Products'])

@product_router.get('/products')
def get_products():
    db = Session()
    data = db.query(ProductModel).order_by(ProductModel.description.asc()).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(data))