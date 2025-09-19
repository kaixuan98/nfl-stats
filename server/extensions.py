#intialize sqlalchemy 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase): 
   createdAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)
   updatedAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)
   deletedAt: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

db = SQLAlchemy(model_class=Base)