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


class GlobalOrder(Base):
    __tablename__ = "global_order"
    id: Mapped[int] = mapped_column(primary_key=True)
    price = mapped_column(Float)
    fk_single_orders: Mapped[List["SingleOrders"]] = relationship(
        back_populates="global_order", cascade="all"
    )
    fk_address_id = mapped_column(ForeignKey("address.id"))
    fk_user_id = mapped_column(ForeignKey("user.id"))
    fk_payment_method_id = mapped_column(ForeignKey("payment_method.id"))
    fk_discount_id = mapped_column(ForeignKey("discount.id"))
    tracking_status = mapped_column(String(30))
    tracking_number = mapped_column(String(30))


class SingleOrders(Base):
    __tablename__ = "single_order"
    id: Mapped[int] = mapped_column(primary_key=True)
    quantity = mapped_column(Integer)
    fk_product_id = mapped_column(ForeignKey("product.id"))
    fk_price_id = mapped_column(ForeignKey("product.price"))
    fk_discount_id = mapped_column(ForeignKey("discount.id"))


# class Payments(Base):
#     __tablename__ = "payment"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name = mapped_column(String(30))


class PaymentMethods(Base):
    __tablename__ = "payment_method"
    id: Mapped[int] = mapped_column(primary_key=True)
    fk_user_id = mapped_column(ForeignKey("user.id"))
    full_name  = mapped_column(ForeignKey("user.name")) + mapped_column(ForeignKey("user.surname"))
    credit_card_number = mapped_column(Integer)
    expire_date = mapped_column(String(5))
    other_info = mapped_column(String(30))

