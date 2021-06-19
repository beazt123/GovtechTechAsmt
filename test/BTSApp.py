import sys
sys.path.append("..\\")

from flask import Flask
from flask_testing import TestCase
from projectLib.utils import serverResponse

import projectLib.database

import mongomock
from unittest.mock import patch, Mock
import os

class BTSAppTestCase(TestCase):
    @patch.object(projectLib.database,"mongo", side_effect=mongomock.MongoClient)
    def create_app(self, mockMongo):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config["FLASK_ENV"] = "development"
        app.add_url_rule(
            "/health",
            methods=["GET"], 
            view_func = \
                lambda  : serverResponse(
                    None, 
                    200, 
                    """Yes this server is alive."""
                    )
            )
        self.mongo = mockMongo
        
        return app


