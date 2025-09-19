
from server.database import Base
from typing import List, TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

if TYPE_CHECKING:
    from server.models.leagues import Leagues
    from server.models.teams import Teams

class Sports(Base):
    __tablename__ = "sports"
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    label: Mapped[str] = mapped_column(nullable=False) # for front end labeling
    type:Mapped[str] = mapped_column(String(50), nullable=True) # individual or team
    leagues:Mapped[List["Leagues"]] = relationship(back_populates="sports")
    teams: Mapped[List["Teams"]] = relationship(back_populates="sports")