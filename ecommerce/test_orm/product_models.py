from sqlalchemy import create_engine
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(30))
    sku = mapped_column(String(30))
    quantity = mapped_column(Integer)
    price = mapped_column(Float)
    fk_pictures_id: Mapped[List["Pictures"]] = relationship(
        back_populates="product", cascade="all"
    )


class Categories(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(30))


class Sizes(Base):
    __tablename__ = "size"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    size = mapped_column(String(30))


class Colors(Base):
    __tablename__ = "color"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(30))
    hexadecimal = mapped_column(String(6))


class Discounts(Base):
    __tablename__ = "discount"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(30))


class Genders(Base):
    __tablename__ = "gender"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(30))


class Pictures(Base):
    __tablename__ = "picture"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    dimentions = mapped_column(String(30))