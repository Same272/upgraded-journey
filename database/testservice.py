from database import get_db
from database.models import *


def get_top5_db(level, ):
    with next(get_db()) as db:
        top5 = db.query(Rating).filter_by(level=level).order_by(Rating.correct_answers.desc()).all
        return top5[:5]

def get_20_questions_db(level):
    with next(get_db()) as db:
        questions_20 = db.query(Question).filter_by(level=level).all()
        return questions_20