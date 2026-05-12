from fastapi import FastAPI
from model import engine
from sqlalchemy import text


app = FastAPI()

@app.on_event("startup")
async def startup():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        print("PostgreSQL connected!")
    except Exception as ex:
        print("DB error:", ex)

@app.get("/")
def read_root():
    return{"message": "First Start"}
