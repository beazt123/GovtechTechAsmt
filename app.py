from flask import Flask
from projectLib.database import mongo
from projectLib.uploadCsvEndpt import addUploadCsvEndpt
from projectLib.usersEndpt import addUsersEndpt

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb+srv://beazt123:wushuer1997@govtechemp.4a9zv.mongodb.net/govtechEmp?retryWrites=true&w=majority"
    app.config["SECRET_KEY"] = "U5WG0MYyEDf6TnMlN7bVAQTxf5iMHc2iQUU9RJIyZz0"
    mongo.init_app(app)
    addUploadCsvEndpt(app, mongo)
    addUsersEndpt(app, mongo)

    return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)