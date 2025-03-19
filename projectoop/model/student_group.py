from projectoop.model.human import Human


class StudentGroup:
    def __init__(self, specialization: str, name_group: str, curator: Human):
        self._specialization = specialization
        self._name_group = name_group
        self._curator = curator

    def __repr__(self):
        return '{} {} {}'.format(self._specialization, self._name_group, self._curator)