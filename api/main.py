from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api.config import engine, SqlAlchemyBaseModel
from api.middlewares.database import DatabaseSessionMiddleware

from api.routers.product import product_router
from api.routers.stock_movement import stock_movement_router

SqlAlchemyBaseModel.metadata.create_all(bind=engine)

app = FastAPI(title='Stock tracker API',
              version='1.0.0')
app.add_middleware(DatabaseSessionMiddleware)
app.include_router(product_router)
app.include_router(stock_movement_router)

@app.get('/', response_class=JSONResponse)
def info():
    return JSONResponse(status_code=200, content={
        'app_name': 'Stock tracker API',
        'version': '1.0.0',
        'author': 'Adan Mercado',
        'email': 'adanmercado.dev@gmail.com'
    })