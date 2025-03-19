from projectoop.enums.gender import Gender
from projectoop.interaction_with_storage.interaction_with_human_storage import loading_in_file_human, unload_string, \
    unload_lines, edit, transfer_from_file, delete_string, unload_human, before_editing
from projectoop.service.human_service import create_human, update_name, update_surname, update_address


def interation_human(json_array):
    additional = json_array["additional"]
    if additional == "Создать":
        human = json_array["human"]
        name = human["name"]
        surname = human["surname"]
        birth_date = human["birth_date"]
        gender = Gender(human["gender"]).value
        address = human["address"]
        human = create_human(name, surname, birth_date, gender, address)
        loading_in_file_human(human)
        return "Человек внесён в файл список"
    elif additional == "Перенести с файла":
        return transfer_from_file()
    elif additional == "Удалить строку":
        del_position = json_array["delete_line"]
        return delete_string(del_position)
    else:
        return "Такая возможность не реализована либо в разработке"


def create_humans(json_array):
    name = json_array["name"]
    surname = json_array["surname"]
    birth_date = json_array["birth_date"]
    gender = Gender(json_array["gender"]).value
    address = json_array["address"]
    human = create_human(name, surname, birth_date, gender, address)
    loading_in_file_human(human)
    return "Человек внесён в файл список"


def form_finding(json_array):
    un_human = unload_string(json_array)
    try:
        name = un_human.split(',')[0].strip()
        surname = un_human.split(',')[1].strip()
        birth_date = un_human.split(',')[2].strip()
        gender = un_human.split(',')[3].strip()
        address = un_human.split(',')[4].strip()
        return {
            "name": name,
            "surname": surname,
            "birth_date": birth_date,
            "gender": gender,
            "address": address
        }
    except:
        return un_human


def full():
    un_human = unload_human()
    try:
        un_human = un_human.replace('\n', ' ')
        line = len(unload_lines())
        storage = {}
        a, b, c, d, e = 0, 1, 2, 3, 4
        for i in range(int(line)):
            name = un_human.split(',')[a].strip()
            surname = un_human.split(',')[b].strip()
            birth_date = un_human.split(',')[c].strip()
            gender = un_human.split(',')[d].strip()
            address = un_human.split(',')[e].strip()
            storage.update({"id: {}".format(i+1): {
                "name": name,
                "surname": surname,
                "birth_date": birth_date,
                "gender": gender,
                "address": address
            }})
            a, b, c, d, e = a + 5, b + 5, c + 5, d + 5, e + 5
        return storage
    except:
        return un_human


def redact(json_array):
    human = edit(before_editing(json_array))
    if human == "Данной строки не существует":
        return human
    elif list(json_array.keys())[0] == "name":
        name = json_array["name"]
        loading_in_file_human(update_name(human, name))
        return "Имя изменено на {}".format(name)
    elif list(json_array.keys())[0] == "surname":
        surname = json_array["surname"]
        loading_in_file_human(update_surname(human, surname))
        return "Фамилия изменена на {}".format(surname)
    elif list(json_array.keys())[0] == "address":
        address = json_array["address"]
        loading_in_file_human(update_address(human, address))
        return "Адрес изменён на {}".format(address)
    else:
        loading_in_file_human(str(human))
        return "По данной конфигурации изменить нельзя"
