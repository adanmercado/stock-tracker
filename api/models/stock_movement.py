from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from api.config import SqlAlchemyBaseModel

class StockMovementModel(SqlAlchemyBaseModel):
    __tablename__ = 'stock_movement'

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship('ProductModel', back_populates='movements')
    
    last_stock = Column(Float)
    new_stock = Column(Float)
    comment = Column(String)
    modification_date = Column(DateTime)