from server.database import Base
from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

# one tournament has many seasons
if TYPE_CHECKING:
    from server.models.league_season import LeagueSeason 

class Seasons(Base):
    __tablename__ = 'seasons'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    label:Mapped[str] = mapped_column(nullable=False) 
    year:Mapped[str] = mapped_column(nullable=False)
    start_date:Mapped[datetime] = mapped_column(nullable=False)
    end_date:Mapped[datetime] = mapped_column(nullable=True)
    leagues: Mapped[List["LeagueSeason"]] =relationship(back_populates='seasons') 