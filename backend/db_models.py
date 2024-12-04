from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Competitor(Base):
    __tablename__ = "competitors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    sector = Column(String)
    description = Column(Text)

print("db_models.py loaded successfully")
