from projectoop.model.human import Human
from projectoop.custom_errors.human_exception.key import HumanKeyException
from projectoop.custom_errors.human_exception.value import HumanValueException


def unpacking(json_array):
    try:
        name = json_array["name"]
        surname = json_array["surname"]
        birth_date = json_array["birth_date"]
        gender = json_array["gender"]
        address = json_array["address"]
        human = Human(name, surname, birth_date, gender, address)
        return human
    except KeyError:
        raise HumanKeyException
    except ValueError:
        raise HumanValueException
