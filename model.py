from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("POSTGRE_CONNECTION")

engine = create_async_engine(url=db_url, echo=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("PostgreSQL подключилась успешно!")
except Exception as ex:
    print("Ошибка подключения!", ex)