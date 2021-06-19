import ssl
from flask_pymongo import PyMongo

mongo = PyMongo(tls=True)