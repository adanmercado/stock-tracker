from pydantic import BaseModel, Field
from typing import Optional

class StockMovement(BaseModel):
    id: Optional[int] = Field(default=None, exclude=True)
    product_id: int
    last_stock: float = Field(default=0.0)
    new_stock: float = Field(default=0.0)
    comment: Optional[str] = Field(max_length=250)