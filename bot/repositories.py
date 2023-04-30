from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from bot.settings import DB_URI
from bot.models import Base

engine = create_engine(DB_URI)
Base.metadata.create_all(engine)


def save_feedback(feedback):
    with Session(engine) as session:
        session.add(feedback)
        session.commit()

