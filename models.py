import datetime as _dt

import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as _hash

import database as _database


class User(_database.Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    password = _sql.Column(_sql.String)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    orders = _orm.relationship("Orders", back_populates="customer")

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.password)


class Orders(_database.Base):
    __tablename__ = "orders"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    price = _sql.Column(_sql.String, index=True)
    order_date = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    customer_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    customer = _orm.relationship("User", back_populates="orders")


class OrderDetails(_database.Base):
    __tablename__ = "order_details"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)


class Product(_database.Base):
    __tablename__ = "product"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String(200))
    brand = _sql.Column(_sql.String(200))
    price = _sql.Column(_sql.Integer)
    inventory = _sql.Column(_sql.Integer)
