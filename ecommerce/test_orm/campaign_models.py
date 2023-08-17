from sqlalchemy import create_engine
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
# import user_models, analytics_models

class Base(DeclarativeBase):
    pass


class CampaignPerformance(Base):
    __tablename__ = "campaign_performance"
    id: Mapped[int] = mapped_column(primary_key=True)
    fk_user_id = mapped_column(ForeignKey("user.id"))
    fk_marketing_campaign_id = mapped_column(ForeignKey("marketing_campaign.id"))
    timestamp = mapped_column(String(30))
    fk_browser_id = mapped_column(ForeignKey("browser.id"))
    fk_os_id = mapped_column(ForeignKey("os.id"))


class MarketingCampaign(Base):
    __tablename__ = "marketing_campaign"
    id: Mapped[int] = mapped_column(primary_key=True)
    fk_user_id = mapped_column(ForeignKey("user.id"))
    name = mapped_column(String(30))
    status = mapped_column(String(30))
    fk_design_id = mapped_column(ForeignKey("campaign_design.id"))


class CampaignDesigns(Base):
    __tablename__ = "campaign_design"
    id: Mapped[int] = mapped_column(primary_key=True)
    html_design = mapped_column(String(30))
    plain_design = mapped_column(String(30))

