from projectoop.enums.gender import Gender
from projectoop.model.human import Human
from projectoop.enums.performnce import Performance
from datetime import date


class Student(Human):
    def __init__(self, name: str, surname: str, birth_date: date, gender: Gender, address: str,
                 performance: Performance, date_admission: date):
        super().__init__(name, surname, birth_date, gender, address)
        self._performance = Performance(performance).value
        self._dateAdmission = date_admission

    def __repr__(self):
        return "{}, {}, {}, {}, {}, {}, {}".format(self._name, self._surname, self._birth_date, self._gender,
                                                   self._address, self._performance, self._dateAdmission)
