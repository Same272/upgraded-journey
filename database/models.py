from database import Base
from sqlalchemy import (Column, Integer, String, BigInteger, DateTime, Boolean, ForeignKey)
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    phone_number = Column(String, unique=True)
    reg_date = Column(DateTime, default=datetime.now())

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    main_question = Column(String, nullable=False)
    v1 = Column(String, nullable=False)
    v2 = Column(String, nullable=False)
    v3 = Column(String, nullable=True)
    v4 = Column(String, nullable=True)
    correct_answer = Column(Integer)
    level = Column(String, defolt='Beginner')

class UserAnswer(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    user_answer = Column(Integer, nullable=True)
    correctness = Column(Boolean, default=False)
    level = Column(String)
    user_fk = relationship(User, lazy='subquery')
    question_fk = relationship(Question, lazy='subquery')

class Rating(Base):
    __tablename__ = "rating"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    level = Column(String, ForeignKey("questions.level"))
    correct_answers = Column(Integer, default=0 )
    user_fk = relationship(User, lazy="subquery")
    question_fk = relationship(Question, lazy="subquery")
