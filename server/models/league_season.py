from server.database import Base
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

if TYPE_CHECKING:
    from server.models.leagues import Leagues 
    from server.models.seasons import Seasons  


class LeagueSeason(Base):
    __tablename__ = 'league_season'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    season_id:Mapped[int] = mapped_column(ForeignKey('seasons.id'),nullable=False)
    league_id:Mapped[int] = mapped_column(ForeignKey('leagues.id'),nullable=False)
    league: Mapped["Leagues"]= relationship(back_populates="leagues")
    season: Mapped["Seasons"]= relationship(back_populates="seasons")
