from flask_restful import Resource
from flask import request, jsonify
from api.resources.db_management import query_db
from passlib.hash import argon2

class User(Resource):
    def get(self, id):
        return query_db('select username from user where id = ?', [id])
    
class Users(Resource):
    def put(self):
        try:
            data = request.get_json()
        except Exception:
            return {"message": "bad request"}, 400

        hash = argon2.hash(data['password'])
        query_db('insert into user values (NULL, ?, ?)', [data['username'], hash],commit=True)
        return {"message": "user registered"}, 201

    def get(self):
        return query_db('select username, hash from user')
