from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm.session import Session

from api.models.product import ProductModel
from api.schemas.product import Product
from api.config import db_session

product_router = APIRouter(tags=['Products'])

@product_router.get('/products', response_model=list[Product])
def get_products(db: Session = Depends(db_session)):
    data = db.query(ProductModel).order_by(ProductModel.description.asc()).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@product_router.get('/products/{barcode}', response_model=Product)
def get_product(barcode: str, db: Session = Depends(db_session)):
    product = db.query(ProductModel).filter(ProductModel.barcode == barcode).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found.')
    return JSONResponse(status_code=200, content=jsonable_encoder(product))

@product_router.post('/products', response_model=Product)
def create_product(product: Product, db: Session = Depends(db_session)):
    if db.query(ProductModel).filter(ProductModel.barcode == product.barcode).first():
        raise HTTPException(status_code=400, detail='Product already registered.')
    
    new_product = ProductModel(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return JSONResponse(status_code=201, content=jsonable_encoder(new_product))

@product_router.put('/products/{barcode}', response_model=Product)
def update_product(barcode: str, product: Product, db: Session = Depends(db_session)):
    current_product = db.query(ProductModel).filter(ProductModel.barcode == barcode).first()
    if not current_product:
        raise HTTPException(status_code=404, detail='Product not found.')
    
    if product.barcode != current_product.barcode and db.query(ProductModel).filter(ProductModel.barcode == product.barcode).first():
        raise HTTPException(status_code=409, detail=f'The barcode {product.barcode} is already assigned to another product.')
    
    current_product.barcode = product.barcode
    current_product.description = product.description
    current_product.price = product.price
    current_product.min_stock = product.min_stock
    current_product.max_stock = product.max_stock
    current_product.current_stock = product.current_stock

    db.add(current_product)
    db.commit()
    db.refresh(current_product)

    return JSONResponse(status_code=200, content=jsonable_encoder(current_product))