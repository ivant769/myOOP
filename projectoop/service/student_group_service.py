from projectoop.model.human import Human
from projectoop.model.student_group import StudentGroup


def create_student_group(specialization: str, name_group: str, curator: Human):
    return StudentGroup(specialization, name_group, curator)


def update_curator(student_group: Human, curator: str):
    student_group.curator = curator
