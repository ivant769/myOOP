from datetime import date
from projectoop.enums.gender import Gender
from projectoop.model.human import Human


def create_human(name: str, surname: str, birth_date: date, gender: Gender, address: str):
    return Human(name, surname, birth_date, gender, address)


def update_name(human: Human, name: str):
    human.name = name
    return human


def update_surname(human: Human, surname: str):
    human.surname = surname
    return human


def update_address(human: Human, address: str):
    human.address = address
    return human
