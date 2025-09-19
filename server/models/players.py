from server.database import Base
from typing import Optional, List
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING: 
    from server.models.team_player import TeamPlayer

class Players(Base):
    __tablename__ = 'players'  
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name:Mapped[str] = mapped_column(nullable=False)
    last_name:Mapped[str] = mapped_column(nullable=False)
    dob: Mapped[Optional[str]] = mapped_column()
    gender: Mapped[str] = mapped_column() 
    nationality: Mapped[Optional[str]] = mapped_column()
    height: Mapped[Optional[int]] = mapped_column()
    heightUnit: Mapped[str] = mapped_column(default='cm')
    weight: Mapped[Optional[int]] = mapped_column()
    weightUnit: Mapped[str] = mapped_column(default="kg")
    teams: Mapped[List["TeamPlayer"]] = relationship(back_populates="players")

