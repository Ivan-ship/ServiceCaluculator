from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os
from dotenv import load_dotenv
import asyncio
from sqlalchemy import text

load_dotenv()

db_url = os.getenv("POSTGRE_CONNECTION")

engine = create_async_engine(url=db_url, echo=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def check_connection():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        print("PostgreConnect")
    except Exception as ex:
        print("Connect Error!")
