from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = Field(default=None, exclude=True)
    barcode: str = Field(min_length=3, max_length=30)
    description: str = Field(min_length=10, max_length=250)
    price: float = Field(ge=0, default=0.0)
    min_stock: float = Field(ge=0, default=0.0)
    max_stock: float = Field(ge=0, default=0.0)
    current_stock: float = Field(ge=0, default=0.0)