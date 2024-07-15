import sqlalchemy
import random
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update, delete
from score_table import add_default_scores
from score_table import delete_scores_by_name
from score_table import delete_scores_by_ID


base = declarative_base()
meta = base.metadata

class Students(base):
    __tablename__ = 'students'
    id = Column(String(9), primary_key=True, unique=True)
    name = Column(String(32), nullable=False)
    age = Column(Integer)
    gender = Column(String(1))
    major = Column(String(32))
    phone = Column(String(32))

    def __init__(self, id, name, age, gender, major, phone):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.major = major
        self.phone = phone

    def __str__(self):
        return f'id:{self.id}, name:{self.name}, age:{self.age}, gender:{self.gender}, major:{self.major}, phone:{self.phone}'

    def __repr__(self):
        return f'Students({self.id!r}, {self.name!r}, {self.age!r}, {self.gender!r}, {self.major!r}, {self.phone!r}'

def create_db():
    engine = sqlalchemy.create_engine('sqlite:///students.db')
    # meta.create_all(engine) # run this statement only once to create databse
    return engine

def init_db():
    pass

s_session = sessionmaker(bind=create_db())()

def show_all_students():
    result = s_session.execute(select(Students)).scalars().all()
    if result == []:
        print("\t \u274C No student existing")
    else:
        print("===================================Show Student====================================")
        print(f'{"ID":<20}{"Name":<20}{"Age":<10}{"Gender":<10}{"Major":<10}{"Phone":<10}')
        for i in result:
            print(f"{i.id:<20}{i.name:<20}{i.age:<10}{i.gender:<10}{i.major:<10}{i.phone:<10}")

def show_students_by_name(n):
    result = s_session.execute(select(Students).filter_by(name=n)).scalars().all()
    if result == []:
        print("\t \u274C No records found!")
    else:
        print("===================================Show Student====================================")
        print(f'{"ID":<20}{"Name":<20}{"Age":<10}{"Gender":<10}{"Major":<10}{"Phone":<10}')
        for i in result:
            print(f"{i.id:<20}{i.name:<20}{i.age:<10}{i.gender:<10}{i.major:<10}{i.phone:<10}")

def show_students_by_id(x):
    result = s_session.query(Students).filter(Students.id == x)
    if result == []:
        print("\t \u274C No records found!")
    else:
        print("===================================Show Student====================================")
        print(f'{"ID":<20}{"Name":<20}{"Age":<10}{"Gender":<10}{"Major":<10}{"Phone":<10}')
        for i in result:
            print(f"{i.id:<20}{i.name:<20}{i.age:<10}{i.gender:<10}{i.major:<10}{i.phone:<10}")

def delete_student_by_name(n):
    result = s_session.execute(delete(Students).filter_by(name=n))
    if result is not None:
        delete_scores_by_name(n)
        s_session.commit()
        s_session.close()
        print("\t \u2714 Record deleted successfully")
    else:
        print("\t \u274C No record found")

def delete_student_by_id(x):
    result = s_session.execute(delete(Students).filter_by(id=x))
    if result is not None:
        delete_scores_by_ID(x)
        s_session.commit()
        s_session.close()
        print("\t \u2714 Record deleted successfully")
    else:
        print("\t \u274C No record found")

def generate_student_id():
    return f'70030{random.randint(1000, 9999)}'

def add_student(name, age, gender, major, phone):
    student_id = generate_student_id()
    new_student = Students(id=student_id, name=name, age=age, gender=gender, major=major, phone=phone)
    s_session.add(new_student)
    add_default_scores(student_id, name)
    s_session.commit()
    print("\t \u2714 Record added successfully")
    s_session.close()


if __name__ == '__main__':
    init_db()
