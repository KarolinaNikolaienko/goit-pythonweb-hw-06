from datetime import datetime, date

from sqlalchemy import select

from connect import session
from models import Student, Teacher, Subject, Group, Grade
from faker import Faker
import random

fake = Faker()

GROUPS = ["A-1", "B-4", "E-2"]
SUBJECTS = ["English", "Math", "Art", "History", "Physics", "Chemistry", "PE", "IT"]
AMOUNT_TEACHERS = 5
AMOUNT_STUDENTS = 30

def make_groups(groups_list: []):
    for group in groups_list:
        group_obj = Group(group_name=group)
        session.add(group_obj)
    session.commit()

def make_teachers(amount):
    for i in range(amount):
        teacher_obj = Teacher(name=fake.name())
        session.add(teacher_obj)
    session.commit()

def make_subjects(subjects_list: []):
    for subject in subjects_list:
        subject_obj = Subject(title=subject, teacher_id=random.randint(1,AMOUNT_TEACHERS))
        session.add(subject_obj)
    session.commit()

def make_students(amount):
    for i in range(amount):
        student_obj = Student(name=fake.name(), group_id=random.randint(1, len(GROUPS)))
        session.add(student_obj)
    session.commit()

def make_grades(students_list: [], subjects_list: []):
    for student in students_list: # для кожного студента
        for subject in subjects_list: # з усіх предметів
            for i in range(random.randint(10,20)): # додати по 10-20 оцінок
                grade_date = fake.date_between_dates(date(2025, 1, 6), date.today())
                grade_obj = Grade(grade=random.randint(0, 100), date=grade_date, student_id=student.id, subject_id=subject.id)
                session.add(grade_obj)
    session.commit()

if __name__ == "__main__":
    make_groups(GROUPS)
    make_teachers(AMOUNT_TEACHERS)
    make_subjects(SUBJECTS)
    make_students(AMOUNT_STUDENTS)

    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    make_grades(students, subjects) # помилка з id = null під час вставки у таблицю Grade

    session.close()

