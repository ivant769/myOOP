from peewee import *
from projectoop.custom_errors.human_exception.dao_date import HumanDAODateException
from projectoop.custom_errors.human_exception.dao_attribute import HumanDAOAttributeException
from projectoop.custom_errors.human_exception.does_not_exist import HumanDAODoesNotExistException

conn = PostgresqlDatabase("projectoop", dbname='projectoop', user='postgres', password='12345678', host='localhost',
                          port='5432')


class HumanBase(Model):
    id_human = BigIntegerField(primary_key=True, null=False)
    name = CharField(null=False, max_length=100)
    surname = CharField(null=False, max_length=100)
    birth_date = DateField(null=False)
    gender = CharField(null=False)  # Придумать как сделать поле в виде enum
    address = CharField(null=False, max_length=100)

    class Meta:
        database = conn
        db_table = 'humans'


def get(id):
    try:
        return HumanBase.select().where(HumanBase.id_human == id).dicts().get()
    except DoesNotExist:
        raise HumanDAODoesNotExistException


def get_all():
    return HumanBase.select().dicts().execute()


def save(human):
    try:
        id = HumanBase.create(name=f"{human.name}", surname=f"{human.surname}", birth_date=f"{human.birth_date}",
                              gender=f"{human.gender}", address=f"{human.address}")
        return get(id)
    except DataError:
        raise HumanDAODateException(human)
    except AttributeError:
        raise HumanDAOAttributeException(human)


def update(human, id):
    try:
        HumanBase.update(name=f"{human.name}", surname=f"{human.surname}", birth_date=f"{human.birth_date}",
                         gender=f"{human.gender}", address=f"{human.address}").where(HumanBase.id_human == id).execute()
        return get(id)
    except DataError:
        raise HumanDAODateException(human)
    except AttributeError:
        raise HumanDAOAttributeException(human)


def delete(id):
    human = get(id)
    human.delete_instance()
