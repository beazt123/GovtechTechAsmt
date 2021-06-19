from flask import request
from projectLib.request_validation import getUserEndpt_ReqValidator


def addUsersEndpt(app, mongo):
    @app.route("/users", methods=['GET'])
    def getUsers():
        if request.method == 'GET':
            args = request.args
            fileName = args.to_dict()