from projectoop.database.db_human import get_all, save, update
from projectoop.human_body import unpacking


def receive_all():
    humans = list(get_all())
    if not humans:
        return "Ничего не найдено"
    else:
        return humans


def create(json_array):
    human = unpacking(json_array)
    return save(human)


def refresh(dict_array, id):
    human = unpacking(dict_array)
    return update(human, id)
