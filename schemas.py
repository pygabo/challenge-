import datetime as _dt

import pydantic as _pydantic


class _UserBase(_pydantic.BaseModel):
    email: str


class UserCreate(_UserBase):
    password: str

    class Config:
        orm_mode = True


class User(_UserBase):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True


class _OrdersBase(_pydantic.BaseModel):
    price: int
    order_date: _dt.datetime


class OrderCreate(_OrdersBase):
    pass


class Orders(_OrdersBase):
    id: int
    customer_id: int
    order_date: _dt.datetime
    price: int
    status: bool

    class Config:
        orm_mode = True
