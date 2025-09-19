from server.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ScrapeSources(Base):
    __tablename__="scrape_sources"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    

