from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import joinedload

from api.schemas.stock_movement import StockMovement
from api.models.stock_movement import StockMovementModel

from api.config import db_session

stock_movement_router = APIRouter(tags=['Stock'])

@stock_movement_router.get('/stock', response_model=list[StockMovement])
def get_all_stock_movements(db: Session = Depends(db_session)):
    movements = db.query(StockMovementModel).options(joinedload(StockMovementModel.product)).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(movements))

@stock_movement_router.post('/stock', response_model=StockMovement)
def create_stock_movement(movement: StockMovement, db: Session = Depends(db_session)):
    stock_movement = StockMovementModel(**movement.model_dump())
    db.add(stock_movement)
    db.commit()
    db.refresh(stock_movement)

    return JSONResponse(status_code=201, content=jsonable_encoder(stock_movement))