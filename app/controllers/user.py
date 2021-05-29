from flask_restful import Resource
from flask import request
from app.models.user import User


class UserAPI(Resource):
    def post(self):
        id = request.form['id']
        password = request.form['password']
        name = request.form['name']

        User(id, password, name).save()

        return {
            'message': 'User login'
        }, 201




