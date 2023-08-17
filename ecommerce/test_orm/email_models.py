from sqlalchemy import create_engine
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
# import user_models, campaign_models

class Base(DeclarativeBase):
    pass


class EmailsSent(Base):
    __tablename__ = "emails_sent"
    id: Mapped[int] = mapped_column(primary_key=True)
    fk_user_id = mapped_column(ForeignKey("user.id"))
    fk_marketing_campaign_id = mapped_column(ForeignKey("marketing_campaign.id"))
    fk_campaign_design_id = mapped_column(ForeignKey("campaign_design.id"))