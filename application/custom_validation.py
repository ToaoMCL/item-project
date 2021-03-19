from wtforms.validators import DataRequired, Length, ValidationError
from application import db
from application.extra_functions import GetDbTableNameFromPassedValue


class SymbolCheck:
    def __init__(self):
        self.message = "No special characters or symbols allowed"

    def __call__(self, form, field):
        _forbidenChars = "}{:;@~|`¬.!@£#$%^&*()-+?_=,<>/"
        for char in _forbidenChars:
            if char in field.data:
                raise ValidationError(self.message)


class ExistsInDbCheck:
    def __init__(self, table=None, message=None):
        if not message:
            message = "Id of item doesnt exist."
        self.message = message
        self.passedTable = table

    def __call__(self, form, field):
        table = self.passedTable

        try:
            if table == None:
                table = GetDbTableNameFromPassedValue(form.active_table.data)
            else:
                table = GetDbTableNameFromPassedValue(table)
        except:
            raise ValidationError("table doesnt exist")

        if table == None:
            raise ValidationError("table doesnt exist")

        exists = db.session.query(table).filter_by(
            id=field.data).first() is not None
        if not exists:
            raise ValidationError(self.message)