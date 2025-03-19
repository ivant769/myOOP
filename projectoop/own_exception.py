import flask_restful
import peewee


class MissingURL(flask_restful.HTTPException):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code


class DateImpossible(peewee.PeeweeException):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
