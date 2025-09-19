from server.database import Base
from typing import TYPE_CHECKING, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

if TYPE_CHECKING:
    from server.models.leagues import Leagues
    from server.models.divisions import Divisions

class Conferences(Base):
    __tablename__ = 'conferences'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[int] = mapped_column(nullable=False)
    league_id:Mapped[int] = mapped_column(ForeignKey("leagues.id"), nullable=False)
    league: Mapped["Leagues"] =relationship(back_populates='leagues') 
    divisions: Mapped[List["Divisions"]] = relationship()