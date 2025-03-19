from projectoop.service.human_service import create_human
from projectoop.enums.gender import Gender


def loading_in_file_human(lifh):
    try:
        human_base = r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\interaction_with_storage\human_base.txt'
        with open(human_base, 'r', encoding="utf-8") as file:
            lines = file.readlines()
        with open(human_base, 'r', encoding="utf-8") as file:
            line = len(file.readlines())
    except:
        line = 0
    finally:
        human_base = open(r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\interaction_with_storage\human_base.txt',
                          'w', encoding="utf-8")
        try:
            if line > 0:
                human_base.writelines(lines)
                human_base.write("\n")
            human_base.write(str(lifh))
        finally:
            human_base.close()


def delete_string(json_array):
    del_position = json_array
    try:
        with open(r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\interaction_with_storage\human_base.txt',
                  'r', encoding="utf-8") as file:
            lines = file.readlines()
            ptr = 1
            with open(r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\interaction_with_storage\human_base.txt',
                      'w', encoding="utf-8") as files:
                for line in lines:
                    if ptr != int(del_position):
                        files.write(line)
                    ptr += 1
        return f"Строка {del_position} была удалена"
    except:
        return "Строки не существует"


def unload_string(json_array):
    row = json_array
    try:
        with open(r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\interaction_with_storage\human_base.txt',
                  'r', encoding="utf-8") as human_base:
            line = human_base.readlines()
            result = line[int(row) - 1]
            return result
    except:
        return "Строки не существует"


def unload_human():
    try:
        with open(r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\interaction_with_storage\human_base.txt',
                  'r', encoding="utf-8") as human_base:
            return human_base.read()
    except:
        return "Файловой базы не существуют"


def unload_lines():
    try:
        with open(r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\interaction_with_storage\human_base.txt',
                  'r', encoding="utf-8") as human_base:
            line = human_base.readlines()
            return line
    except:
        return "Файловой базы не существуют"


def unloading_in_file_human(json_array): # устарело
    un_human = unload_string(json_array)
    try:
        name = un_human.split(',')[0].strip()
        surname = un_human.split(',')[1].strip()
        birth_date = un_human.split(',')[2].strip()
        gender = Gender(un_human.split(',')[3].strip()).value
        address = un_human.split(',')[4].strip()
        un_human = create_human(name, surname, birth_date, gender, address)
        return un_human
    except:
        return un_human


def transfer_from_file():
    with open(r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\file_to_read.txt', 'r',
              encoding="utf-8") as transfer:
        array = list(transfer)
    with open(r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\file_to_read.txt', 'r',
              encoding="utf-8") as transfer:
        array_line = len(transfer.readlines())
    try:
        with open(r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\interaction_with_storage\human_base.txt', 'r',
                  encoding="utf-8") as file:
            lines = file.readlines()
            line = 1
    except:
        line = 0
    finally:
        with open(r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\interaction_with_storage\human_base.txt', 'w',
                  encoding="utf-8") as human_base:
            if line != 0:
                human_base.writelines(lines)
                human_base.write("\n")
        for i in range(array_line):
            with open(r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\interaction_with_storage\human_base.txt',
                      'r',
                      encoding="utf-8") as file:
                lines = file.readlines()
            with open(r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\interaction_with_storage\human_base.txt',
                      'w',
                      encoding="utf-8") as human_base:
                human_base.writelines(lines)
                human_base.write(array[i])
        return "Файлы были перенесены"


def before_editing(json_array):
    try:
        redact_line = json_array["redact_line"]
        with open(r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\interaction_with_storage\human_base.txt',
                  'r', encoding="utf-8") as file:
            lines = file.readlines()
            ptr = 1
            redact = lines[int(redact_line) - 1]
            with open(r'C:\Users\User\PycharmProjects\WebProjectOOP\projectoop\interaction_with_storage\human_base.txt',
                      'w', encoding="utf-8") as files:
                for line in lines:
                    if ptr != int(redact_line):
                        files.write(line)
                    ptr += 1
            return redact
    except:
        return "Данной строки не существует"


def edit(editable):
    try:
        name = editable.split(',')[0].strip()
        surname = editable.split(',')[1].strip()
        birth_date = editable.split(',')[2].strip()
        gender = Gender(editable.split(',')[3].strip()).value
        address = editable.split(',')[4].strip()
        un_human = create_human(name, surname, birth_date, gender, address)
        return un_human
    except:
        return editable
