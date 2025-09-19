from server.database import Base
from typing import TYPE_CHECKING, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

if TYPE_CHECKING:
    from server.models.conferences import Conferences
    from server.models.teams import Teams

class Divisions(Base):
    __tablename__ = 'divisions'
    id:Mapped[int]=mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(nullable=False)
    conference_id:Mapped[int]=mapped_column(ForeignKey('conferences.id'))
    conference:Mapped["Conferences"] =relationship(back_populates='conferences')
    teams: Mapped[List["Teams"]] = relationship(back_populates="divisions")