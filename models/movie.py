from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float



class Movie(Base):
    
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    overview= Column(String(255), nullable=False)
    year = Column(Integer(255), nullable=False)
    rating = Column(Float(255), nullable=False)
    category = Column(String(255), nullable=False)
    