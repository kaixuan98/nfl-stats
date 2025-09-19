from server.database import Base
from typing import TYPE_CHECKING
from datetime import datetime 
from typing import Optional
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING: 
    from server.models.teams import Teams
    from server.models.players import Players

class TeamPlayer(Base):
    __tablename__ = 'team_player'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    player_id:Mapped[int] = mapped_column(ForeignKey('players.id'))
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.id'))
    start_date: Mapped[datetime] = mapped_column(DateTime)
    end_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    player_no: Mapped[Optional[int]] = mapped_column()
    position: Mapped[Optional[str]] = mapped_column()
    # relationship
    team: Mapped["Teams"] = relationship(back_populates='teams')
    player: Mapped["Players"] = relationship(back_populates='players')
