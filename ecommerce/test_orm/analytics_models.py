from sqlalchemy import create_engine
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
# import user_models


class Base(DeclarativeBase):
    pass


class Analytics(Base):
    __tablename__ = "analytics"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ip = mapped_column(String(30))
    timestamp = mapped_column(String(30))
    page_request = mapped_column(String(30))
    fk_user_id = mapped_column(ForeignKey("user.id"))
    fk_click_id = mapped_column(ForeignKey("click.id"))
    fk_browser_id = mapped_column(ForeignKey("browser.id"))
    fk_os_id = mapped_column(ForeignKey("os.id"))


class Pages(Base):
    __tablename__ = "page"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(30))



class Clicks(Base):
    __tablename__ = "click"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    fk_page_id = mapped_column(ForeignKey("page.id"))
    action = mapped_column(String(30))


class OS(Base):
    __tablename__ = "os"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(30))


class Browsers(Base):
    __tablename__ = "browser"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(30))