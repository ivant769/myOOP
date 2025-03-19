from projectoop.enums.gender import Gender
from datetime import date


class Human:
    def __init__(self, name: str, surname: str, birth_date: date, gender: Gender, address: str):
        self._name = name
        self._surname = surname
        self._birth_date = birth_date
        self._gender = Gender(gender).value
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def gender(self):
        return self._gender

    @property
    def address(self):
        return self._address

    @name.setter
    def name(self, name):
        self._name = name

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @address.setter
    def address(self, address):
        self._address = address

    def __str__(self):
        return "{}, {}, {}, {}, {},".format(self._name, self._surname, self._birth_date,
                                            self._gender, self._address)
