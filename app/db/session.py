from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
)


async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
)


SessionLocal = sessionmaker(sync_engine)
AsyncSessionLocal = async_sessionmaker(async_engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_async_db():
    async with AsyncSessionLocal() as db:
        yield db
