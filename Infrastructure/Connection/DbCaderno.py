from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Domain.Entities.Anotacao import Base

DATABASE_URL = "sqlite:///caderno_digital.db"
engine = create_engine(DATABASE_URL, echo=False)

### Migration
Base.metadata.create_all(bind=engine)

DbCaderno = sessionmaker(autocommit=False, autoflush=False, bind=engine)