from flask import Flask, jsonify, request
from config import config
from flask_restful import Api
from src.database.db import initialize_db
from src.router import TodosApi, TodoApi
from flask_mongoengine import MongoEngine


app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = config

initialize_db(app)

api.add_resource(TodosApi, '/api/todos')
api.add_resource(TodoApi, '/api/todos/<id>')



if __name__ == '__main__':
    app.run(debug=True)