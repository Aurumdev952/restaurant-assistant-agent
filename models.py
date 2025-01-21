from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime


class Menu(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    ingredients: str
    ratings: float
    description: str
    target_age_group: str

    orders: List["Order"] = Relationship(back_populates="menu")


class Order(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    menu_id: int = Field(foreign_key="menu.id")
    quantity: int
    order_date: datetime = Field(default_factory=datetime.utcnow)

    menu: Optional[Menu] = Relationship(back_populates="orders")
