import pandas as pd
from .constants import ID, LOGIN, SALARY
from .utils import readEmpCSVData
from marshmallow import fields, Schema, validates, ValidationError

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

    return True, "Data is clean"

class getUserEndpt_ReqValidator(Schema):
    name = fields.String(required=True)
    age = fields.Integer(
        required=True, 
        error_messages={"required": "Age is required."}
        )
    city = fields.String(
        required=True,
        error_messages={"required": {"message": "City required", "code": 400}},
    )
    email = fields.Email(required=True)

    @validates("city")
    def validate_quantity(self, value):
        if "a" not in value:
            raise ValidationError("City must contain the letter 'a'")

if __name__ == "__main__":
    try:
        # result = UserSchema().load({"email": "foo@bar.com"})
        val = UserSchema().validate({"email": "foo@bar.com", "city":"citt"})
        print("Success")
        # print(result)
        print(val)

    except ValidationError as err:
        print(err.messages)
        print("Validation Error")
    except:
        print("error")