from connect import session
from models import Student, Teacher, Subject, Grade, Group
from faker import Faker
import random

fake = Faker()

if __name__ == "__main__":
    groups = [Group(group_name="A-1"), Group(group_name="B-4"), Group(group_name="E-2")]

    students = []
    for i in range(30):
        students.append(Student(name=fake.name(), group_id=random.randint(1,3)))


    session.bulk_insert_mappings(Student, students)
    session.commit()
    session.close()
