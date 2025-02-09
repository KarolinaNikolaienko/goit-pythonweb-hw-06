from sqlalchemy import ForeignKey, Table, Column, Integer, String, Date, PrimaryKeyConstraint, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

grades = Table(
    "grades",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id", ondelete="CASCADE")),
    Column("subject_id", Integer, ForeignKey("subjects.id", ondelete="CASCADE")),
    Column("grade", Integer()),
    Column("date", Date()),
    PrimaryKeyConstraint("student_id", "subject_id"),
)

class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    group_id: Mapped[int] = mapped_column(Integer(), ForeignKey('groups.id'))
    subjects: Mapped[list["Subject"]] = relationship(
        secondary=grades, back_populates="students"
    )

class Group(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    group_name: Mapped[str] = mapped_column(String(5), nullable=False, unique=True)

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
    students: Mapped[list["Student"]] = relationship(
        secondary=grades, back_populates="subjects"
    )

# class Grade(Base):
#     __tablename__ = "grades"
#     student_id: Mapped[int] = mapped_column(Integer(), ForeignKey('students.id', ondelete="CASCADE"))
#     subject_id: Mapped[int] = mapped_column(Integer(), ForeignKey('subjects.id', ondelete="CASCADE"))
#     grade: Mapped[int] = mapped_column(Integer(), nullable=False)
#     date: Mapped[Date] = mapped_column(Date(), nullable=False)
#     PrimaryKeyConstraint("student_id", "subject_id")
