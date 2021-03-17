from wtforms.validators import DataRequired, Length, ValidationError
from application import db
from application.extra_functions import GetDbTableNameFromPassedValue


class IsNumericCheck:
    def __init__(self, message=None):
        if not message:
            message = "Only whole numbers allowed"
        self.message = message

    def __call__(self, form, field):
        if not str(field.data).isdigit():
            raise ValidationError(self.message)


class SymbolCheck:
    def __init__(self, message=None):
        if not message:
            message = "No special characters or symbols allowed"
        self.message = message

    def __call__(self, form, field):
        _forbidenChars = "}{:;@~\|`¬.!@#$%^&*()-+?_=,<>/"
        for char in _forbidenChars:
            if char in field.data:
                raise ValidationError(self.message)


class ExistsInDbCheck:
    def __init__(self, table=None, message=None):
        if not message:
            message = "Id of item doesn't exist."
        self.message = message
        self.passedTable = table

    def __call__(self, form, field):
        table = self.passedTable
        if table == None:
            try:
                table = GetDbTableNameFromPassedValue(form.active_table.data)
            except:
                raise ValidationError("table doesn't exist")
        else:
            table = GetDbTableNameFromPassedValue(table)
        exists = db.session.query(table).filter_by(
            id=field.data).first() is not None
        if not exists:
            raise ValidationError(self.message)