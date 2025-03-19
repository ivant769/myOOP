from datetime import date
from projectoop.enums.gender import Gender
from projectoop.model.human import Human


class Friend(Human):
    def __init__(self, name: str, surname: str, birth_date: date, gender: Gender, address: str, nickname: str,
                 interests: str):
        super().__init__(name, surname, birth_date, gender, address)
        self._nickname = nickname
        self._interests = interests

    def __repr__(self):
        return "{}, {}, {}, {}, {}, {}, {}".format(self._name, self._surname, self._birth_date,
                                                   self._gender, self._address, self._nickname, self._interests)