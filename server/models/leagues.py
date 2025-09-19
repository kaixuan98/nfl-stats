from server.database import Base
from typing import TYPE_CHECKING, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

if TYPE_CHECKING:
    from server.models.sports import Sports
    from server.models.league_season import LeagueSeason
    from server.models.conferences import Conferences
    from server.models.teams import Teams


class Leagues(Base):
    __tablename__ = 'leagues'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    alias: Mapped[str] = mapped_column(nullable=False)
    sports_id: Mapped[int] = mapped_column(ForeignKey("sports.id"), nullable=False)
    sport: Mapped["Sports"] = relationship(back_populates="leagues")
    seasons: Mapped[List["LeagueSeason"]] = relationship(back_populates="leagues")
    conferences: Mapped[List['Conferences']] = relationship()
    teams: Mapped[List["Teams"]] = relationship(back_populates="leagues")