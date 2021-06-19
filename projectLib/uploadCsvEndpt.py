import pandas as pd
from flask import request
from .constants import ID, LOGIN, NAME, SALARY
from .utils import serverResponse, readEmpCSVData, dbEmpDataLock
from .request_validation import validateEmpData


def addUploadCsvEndpt(app, mongo):
    @app.route("/users/upload", methods=['POST'])
    def uploadUsers():
        if request.method == 'POST':
            formdata = request.files
            csvFile = formdata.get("file")
            df = readEmpCSVData(csvFile)
            print(df)
            valid, msg = validateEmpData(df)
            if not valid:
                return serverResponse(None, 401, msg)

            
            with dbEmpDataLock:
                for row in df.itertuples():
                    exists = mongo.db.users.find_one({NAME: row.name})
                    print(row.name)
                    if exists:
                        return serverResponse(None, 401, f"There is already someone with the name '{row.name}'")

                for row in df.itertuples():
                    mongo.db.users.update_one(
                        {LOGIN: row.login},
                        {  
                            "$set": {
                                ID: row.id,
                                NAME: row.name,
                                SALARY: row.salary
                            }
                        },
                        upsert=True
                    )
            return serverResponse(None, 200, "CSV can been successfully uploaded")


            
