from projectLib.utils import serverResponse
from flask import request
from .constants import USERS_REQ_LIMIT, SALARY
from projectLib.request_validation import getUserEndpt_ReqValidator
from marshmallow import ValidationError


def addUsersEndpt(app, mongo):
    @app.route("/users", methods=['GET'])
    def getUsers():
        if request.method == 'GET':
            args = request.args.to_dict()
            try:
                print(args)
                cleaned_args = getUserEndpt_ReqValidator().load(args)
            except ValidationError as e:
                return serverResponse(str(e), 401, "Invalid request")

            foundUsers = mongo.db.users.find(
                {
                    SALARY: {
                        "$lt": cleaned_args["maxSalary"],
                        "$gt": cleaned_args["minSalary"]
                        }
                },
                limit = USERS_REQ_LIMIT,
                skip = cleaned_args['offset']
                )
            data = {"results": [user for user in foundUsers]}
            return serverResponse(
                data,
                200,
                f"{len(data['results'])} users found"
                )
