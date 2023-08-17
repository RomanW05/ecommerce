from sqlalchemy import create_engine
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(Integer)
    password = mapped_column(String(30))
    name = mapped_column(String(30))
    surname = mapped_column(String(30))
    phone = mapped_column(String(30))
    email = mapped_column(String(30))
    fk_address_id = mapped_column(ForeignKey("address.id"))


class User(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    stree_name = mapped_column(String(30))
    block_number = mapped_column(String(30))
    floor_number = mapped_column(String(30))
    street_number = mapped_column(String(30))
    fk_zip_code_id = mapped_column(ForeignKey("zip_code.id"))
    fk_province_id = mapped_column(ForeignKey("province.id"))
    fk_country_id = mapped_column(ForeignKey("country.id"))


class Country(Base):
    __tablename__ = "country"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(30))
    code = mapped_column(String(2))


class Province(Base):
    __tablename__ = "province"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(30))
    code = mapped_column(String(2))
    fk_country_id = mapped_column(ForeignKey("country.id"))


class Zip_code(Base):
    __tablename__ = "zip_code"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code = mapped_column(String(2))
    fk_province_id = mapped_column(ForeignKey("province.id"))
    fk_country_id = mapped_column(ForeignKey("country.id"))