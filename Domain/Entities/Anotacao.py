from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Anotacao(Base):
    __tablename__ = "Anotacoes"

    Id = Column(Integer, primary_key=True)
    Titulo = Column(String(100), nullable=False)
    Anotacao = Column(Text, nullable=True)