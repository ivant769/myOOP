from datetime import date
from projectoop.enums.gender import Gender
from projectoop.model.friend import Friend


def create_friend(name: str, surname: str, birth_date: date, gender: Gender, address: str, nickname: str, interests: str):
    return Friend(name, surname, birth_date, gender, address, nickname, interests)


def update_name(friend: Friend, name: str):
    friend.name = name


def update_surname(friend: Friend, surname: str):
    friend.surname = surname


def update_address(friend: Friend, address: str):
    friend.address = address


def update_interests(friend: Friend, interests: str):
    friend.address = interests
