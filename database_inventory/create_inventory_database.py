from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, JSON

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import sys

base_path = Path(__file__).parent
database_sqlite3_path = f"{base_path}/database.db"

'postgresql://myuser:mypassword@postgres/mydatabase'
Base = declarative_base()

def create_session():
    try:
        engine = create_engine('postgresql://myuser:mypassword@postgres/mydatabase')
        # engine = create_engine(f'sqlite:///{database_sqlite3_path}')  # engine = create_engine('sqlite:///your_database.db')
        print(
            f"Connection to the for user created successfully.")
    except Exception as e:
        print("Connection could not be made due to the following error: \n", e)
        sys.exit()

    Session = sessionmaker(bind=engine)
    session = Session()
    
    return session



class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)


class Colors(Base):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hexadecimal = Column(String, unique=True)


class Sizes(Base):
    __tablename__ = 'sizes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    size = Column(String, unique=True)


class Discounts(Base):
    __tablename__ = 'discounts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    discount_percentage = Column(Integer, unique=True)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    sku = Column(String, unique=True)
    quantity = Column(Integer)
    category_id = Column("category_id", Integer, ForeignKey("category.id"))
    color_id = Column("color_id", Integer, ForeignKey("colors.id"))
    size_id = Column("size_id", Integer, ForeignKey("sizes.id"))
    discount_id = Column("discount_id", Integer, ForeignKey("discounts.id"))
































































































# new_record = products_data(supplier_name='Example')
# session.add(new_record)
# session.commit()