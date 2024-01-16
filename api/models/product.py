from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from api.config import SqlAlchemyBaseModel

class ProductModel(SqlAlchemyBaseModel):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    barcode = Column(String, unique=True)
    description = Column(String)
    price = Column(Float)
    min_stock = Column(Float)
    max_stock = Column(Float)
    current_stock = Column(Float)

    movements = relationship('StockMovementModel', back_populates='product')