from sqlalchemy import ForeignKey, Table, Column, Integer, String, Date, PrimaryKeyConstraint, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    group: Mapped[int] = mapped_column(Integer(), ForeignKey('groups.id'))

class Group(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    group: Mapped[str] = mapped_column(String(5), nullable=False)

class Teacher(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    subjects:Mapped[list['Subject']] = relationship(back_populates='teacher')

class Subject(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    teacher: Mapped['Teacher'] = relationship(back_populates='subjects')

class Grade(Base):
    __tablename__ = "grades"
    student_id: Mapped[int] = mapped_column(Integer(), ForeignKey('students.id'))
    subject_id: Mapped[int] = mapped_column(Integer(), ForeignKey('subjects.id'))
    grade: Mapped[int] = mapped_column(Integer(), nullable=False)
    date: Mapped[Date] = mapped_column(Date(), nullable=False)
    PrimaryKeyConstraint("student_id", "subject_id")
