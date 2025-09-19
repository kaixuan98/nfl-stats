from server.database import Base
from typing import TYPE_CHECKING, Optional
from typing import Optional, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from server.models.divisions import Divisions
    from server.models.leagues import Leagues
    from server.models.sports import Sports
    from server.models.team_player import TeamPlayer


class Teams(Base):
    __tablename__ = 'teams'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(nullable=False)
    city:Mapped[str] = mapped_column(nullable=False)
    alias:Mapped[Optional[str]] = mapped_column()
    abbreviation:Mapped[Optional[str]] = mapped_column()
    founded_year:Mapped[Optional[str]] = mapped_column()
    dissolved_year:Mapped[Optional[str]] = mapped_column()
    sport_id:Mapped[int] = mapped_column(ForeignKey('sports.id'))
    league_id:Mapped[int] = mapped_column(ForeignKey('leagues.id'))
    division_id:Mapped[Optional[int]] = mapped_column(ForeignKey('divisions.id'), nullable=True) 
    # relationships
    sport:Mapped["Sports"] = relationship(back_populates="sports")
    league: Mapped["Leagues"] = relationship(back_populates="leagues")
    division: Mapped["Divisions"] = relationship(back_populates="divisions")
    players: Mapped[List["TeamPlayer"]] = relationship(back_populates="teams")
    