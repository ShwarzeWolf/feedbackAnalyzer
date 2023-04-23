from sqlalchemy import String, Column, Integer, Text
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Feedback(Base):
    __tablename__ = 'students_feedbacks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    course = Column(String(256), nullable=False)
    content = Column(Text)
