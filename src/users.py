from flask_restful import Api, Resource, reqparse
from database import *

class Users(Resource):

    def get(self):
        ''' Get user info '''

        result = { "users": [] }

        users = executeQuery("SELECT * FROM user")

        for user in users:
            result["users"].append({
                "id": user[0],
                "first_name": user[1],
                "phone": user[2],
                "email": user[3],
                "birthdate": user[4],
                "description": user[5],
            })

        return result, 200
