import sqlalchemy
from sqlalchemy import select, delete
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


base = declarative_base()
meta = base.metadata

class Scores(base):
    __tablename__ = 'scores'
    id = Column(String(9), primary_key=True, unique=True)
    name = Column(String(32), nullable=False)
    CS1030 = Column(Integer)
    CS1100 = Column(Integer)
    CS2030 = Column(Integer)


    def __init__(self, id, name, CS1030, CS1100, CS2030):
        self.id = id
        self.name = name
        self.CS1030 = CS1030
        self.CS1100 = CS1100
        self.CS2030 = CS2030

    def __str__(self):
        return f'id:{self.id}, name:{self.name}, CS1030:{self.CS1030}, CS1100:{self.CS1100}, CS2030:{self.CS2030}'

    def __repr__(self):
        return f'Scores({self.id!r}, {self.name!r}, {self.CS1030!r}, {self.CS1100!r}, {self.CS2030!r}'

def create_db():
    engine = sqlalchemy.create_engine('sqlite:///scores.db')
    # meta.create_all(engine) # run this statement only once to create databse
    return engine

def init_db():
    pass

c_session = sessionmaker(bind=create_db())()

def display_student_score_by_name(n):
    result = c_session.execute(select(Scores).filter_by(name=n)).scalars().all()
    print("===================================Student Score====================================")
    print(f'{"ID":<10}{"Name":<15}{"CS1030":<10}{"CS1100":<10}{"CS2030":<10}')
    for i in result:
        print(f"{i.id:<10}{i.name:<15}{i.CS1030:<10}{i.CS1100:<10}{i.CS2030:<10}")

def update_student_score_by_ID(x):
    student = c_session.query(Scores).filter(Scores.id == x).first()
    if student is None:
        print("\t \u274C No record found")
        return

    new_CS1030 = input(f"New Grade for CS1030 (press Enter without modification): ")
    if new_CS1030.strip():
        student.CS1030 = int(new_CS1030)

    new_CS1100 = input(f"New Grade for CS1100 (press Enter without modification): ")
    if new_CS1100.strip():
        student.CS1100 = int(new_CS1100)

    new_CS2030 = input(f"New Grade for CS2030 (press Enter without modification): ")
    if new_CS2030.strip():
        student.CS2030 = int(new_CS2030)

    c_session.commit()
    print("\t \u2714 Record updated successfully")

def add_default_scores(student_id, student_name):
    new_score = Scores(id=student_id, name=student_name, CS1030=0, CS1100=0, CS2030=0)
    c_session.add(new_score)
    c_session.commit()
    c_session.close()

def delete_scores_by_name(n):
    c_session.execute(delete(Scores).filter_by(name=n))
    c_session.commit()
    c_session.close()

def delete_scores_by_ID(x):
    c_session.execute(delete(Scores).filter_by(id=x))
    c_session.commit()
    c_session.close()


if __name__ == '__main__':
    init_db()
