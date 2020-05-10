from flask_pymongo import PyMongo, ObjectId
from flask import Response, request
from .database.todo_model import Todo
from flask_restful import Resource
from flask_cors import cross_origin
from datetime import datetime

class TodosApi(Resource):
    def get(self):
        todos = Todo.objects().to_json()
        return Response(todos, mimetype="application/json", status=200)

    @cross_origin('*')
    def post(self):
        body = request.get_json()
        todo =  Todo(**body).save()
        id = todo.id
        return {'id': str(id)}, 200
        
class TodoApi(Resource):
    def put(self, id):
        body = request.get_json()
        print(body)
        Todo.objects.get(id=id).update(**body)
        return {'id': str(id)}, 200
    
    @cross_origin('*')
    def delete(self, id):
        todo = Todo.objects.get(id=id).delete()
        return '', 200
    
    @cross_origin('*')
    def get(self, id):
        todos = Todo.objects.get(id=id).to_json()
        return Response(todos, mimetype="application/json", status=200)