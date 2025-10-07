from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Session

async def get_session() -> Generator:  #generator fica esperando a utilização, terminou de utilizar vai para o finally
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()