from flask import Blueprint
from flask_restful import NotFound
from projectoop.custom_errors.human_exception.dao_date import HumanDAODateException
from projectoop.custom_errors.human_exception.dao_attribute import HumanDAOAttributeException
from projectoop.custom_errors.human_exception.key import HumanKeyException
from projectoop.custom_errors.human_exception.value import HumanValueException
from projectoop.custom_errors.human_exception.does_not_exist import HumanDAODoesNotExistException

blueprint = Blueprint('error_handlers', __name__)


@blueprint.app_errorhandler(HumanDAODateException)
def data_error(e):
    return {"Message": "Проверьте вводимую дату"}, 406


@blueprint.app_errorhandler(HumanDAOAttributeException)
def attribute_error(e):
    return {"Message": "Проверьте вводимые значения"}, 415


@blueprint.app_errorhandler(HumanKeyException)
def key_error(e):
    return {"Message": "Проверьте вводимую форму отправки"}, 415


@blueprint.app_errorhandler(HumanValueException)
def value_error(e):
    return {"Message": "Проверьте вводимые переменные в форму"}, 415


@blueprint.app_errorhandler(NotFound)
def not_found(e):
    return {"Message": "Ссылка не действительна"}, 404


@blueprint.app_errorhandler(HumanDAODoesNotExistException)
def does_not_exist(e):
    return {"Message": "Пользователь не найден"}, 404


@blueprint.app_errorhandler(Exception)
def exception_error(e):
    print(e.__class__.__name__)
    return {"Error": "Unexpected error",
            "Massage": "If this was not planned, inform your network administrator"}, 501
