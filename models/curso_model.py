from typing import Optional

from sqlmodel import SQLModel, Field

class CursoModel(SQLModel, table=True):
    __tablename__: str = 'cursos'

    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    aulas: int
    horas: int
