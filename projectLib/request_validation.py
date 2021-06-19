import pandas as pd
from .constants import ID, LOGIN, SALARY, NAME, USERS_REQ_LIMIT
from .utils import readEmpCSVData
from marshmallow import fields, Schema, validates, ValidationError, validates_schema

def validateEmpData(df):
    if type(df) == str:
        dframe = readEmpCSVData(df)
    elif type(df) == pd.DataFrame:
        dframe = df.copy(deep=True)

    else:
        raise TypeError("Input must be a file path or pandas dataframe")

    dframe.dropna(how="all", inplace=True)

    uniqueColumns = [ID, LOGIN]
    for column in uniqueColumns:
        dupes = dframe.duplicated(column, keep=False)
        if len(dframe[dupes]) > 0:
            return False, f"'{column}' contains duplicate entries"
    
    if any(dframe.isna().to_numpy().flatten()):
        return False, "Data contains null fields"
    
    if len(dframe[dframe[SALARY] <= 0]):
        return False, "Data contains negative salaries"

    validColumns = [ID, LOGIN, SALARY, NAME]
    if not all(map(lambda x : x in validColumns, dframe.columns)):
        return False, "Data contains extra unwanted fields"

    if not all(map(lambda x : x in dframe.columns, validColumns)):
        return False, "Data contains insufficient fields"

    return True, "Data is clean"

class getUserEndpt_ReqValidator(Schema):
    minSalary = fields.Float(required=True)
    maxSalary = fields.Float(required=True)
    offset = fields.Int(required=True)
    limit = fields.Int(required=True)
    sort = fields.Str(required=True)

    @validates("sort")
    def validate_sort(self, value):
        validKeys = [ID, LOGIN, SALARY, NAME]

        if "-" not in value and "+" not in value:
            print(value)
            raise ValidationError("Sort order must be provided")
        elif value.strip("+") not in validKeys and \
                value.strip("-") not in validKeys:
            raise ValidationError("Invalid sort key")
    
    @validates("limit")
    def validate_limit(self, numRequestedUsers):
        if numRequestedUsers > USERS_REQ_LIMIT:
            raise ValidationError("limit cannot be greater than 30")


    @validates_schema
    def validate_quantity(self, data, **kwargs):
        if data['maxSalary'] < data['minSalary']:
            raise ValidationError("maxSalary cannot be less than minSalary")


if __name__ == "__main__":
    try:
        result = getUserEndpt_ReqValidator().load(
            {
                "minSalary":1,
                "maxSalary":10,
                "offset":0,
                "limit":30,
                "sort":"+name"
            }
            )
        # val = getUserEndpt_ReqValidator().validate(
        #     {"minSalary":"l"}
        #     )
        print("Success")
        print(result)
        # print(val)

    except ValidationError as err:
        print(err.messages)
        print("Validation Error")
    # except:
    #     print("error")