from datetime import date
from projectoop.enums.gender import Gender
from projectoop.enums.performnce import Performance
from projectoop.model.student import Student


def create_student(name: str, surname: str, birth_date: date, gender: Gender,
                   address: str, performance: Performance, date_admission: date):
    return Student(name, surname, birth_date, gender, address, performance, date_admission)


def update_name(student: Student, name: str):
    student.name = name


def update_surname(student: Student, surname: str):
    student.surname = surname


def update_performance(student: Student, address: str):
    student.address = address


def update_address(student: Student, performance: str):
    student.performance = performance
