from sqlalchemy import Column, Integer, String, Float, Text
from .database import Base

class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True)
    content = Column(Text)
    source_score = Column(Float)
    bias_score = Column(Float)
    fake_score = Column(Float)
    final_score = Column(Float)
    conclusion = Column(String)
