from fastapi import FastAPI
from server.database import engine, SessionLocal, Base
import server.models

app = FastAPI()
# create tables in the database
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
async def root():
    return {"message": "Hello World"}