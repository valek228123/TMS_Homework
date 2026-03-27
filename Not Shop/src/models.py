from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from .db_conector import session
from typing import Self
from sqlalchemy.types import String, DateTime, Boolean


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String(30))
    points: Mapped[int] = mapped_column(default=0)

    @staticmethod
    def is_exist(username: str) -> bool:
        return session.query(User).filter_by(username=username).scalar() is not None

    @staticmethod
    def get_user_by_username(username: str) -> Self | None:
        return session.query(User).filter_by(username=username).first()

    @staticmethod
    def get_user_by_id(username: str) -> Self | None:
        return session.query(User).filter_by(id=id).first()

    def check_password(self, password: str) -> bool:
        return self.password == password


class Orders(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(('users.id'), ondelete='RESTRICT', onupdate='CASCADE'))
    product_id: Mapped[int] = mapped_column(ForeignKey(('products.id'), ondelete='CASCADE', onupdate='CASCADE'))
    count: Mapped[int] = mapped_column()
    order_datetime: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    @staticmethod
    def get_orders_by_user_id(user_id) -> list[Self]:
        return session.query(Orders).filter_by(user_id=user_id).all()


class Tickets(Base):
    __tablename__ = 'tickets'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(36), unique=True)
    available: Mapped[bool] = mapped_column(Boolean, default=True)
    user: Mapped[int] = mapped_column(ForeignKey(('users.id'), ondelete='RESTRICT', onupdate='CASCADE'), nullable=True)

    @staticmethod
    def get_ticket_by_uuid(uuid: str) -> Self | None:
        return session.query(Tickets).filter_by(uuid=uuid).first()


class Products(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    cost: Mapped[int] = mapped_column()
    count: Mapped[int] = mapped_column()

    @staticmethod
    def get_product_by_id(id: int) -> Self | None:
        return session.query(Products).filter_by(id=id).first()
