from flask_restful import Api, Resource, reqparse
from database import *

users = [
    {
        "name": "Matthieu",
        "age": 29,
        "occupation": "Software Engineer"
    },
    {
        "name": "Barbara",
        "age": 27,
        "occupation": "Software Engineer"
    },
    {
        "name": "Arthur",
        "age": 22,
        "occupation": "Video Game Player"
    }
]

class User(Resource):

    def get(self, user_id):
        ''' Get user info '''

        user = executeQuery("SELECT * FROM user WHERE id=" + str(user_id))[0]
        result = { "user": {} }

        if user:
            result["user"] = {
                "id": user[0],
                "first_name": user[1],
                "phone": user[2],
                "email": user[3],
                "birthdate": user[4],
                "description": user[5],
            }
            return result, 200
        else:
            return "User not found", 404


    def post(self, user_id):
        ''' Create new user '''
        parser = reqparse.RequestParser()
        parser.add_argument("first_name")
        parser.add_argument("birthdate")
        parser.add_argument("description")
        args = parser.parse_args()

        user = {
            "first_name": args["first_name"],
            "description": args["description"],
            "birthdate": args["birthdate"]
        }
        id = insertRecord("user", user)
        return id, 201


    def put(self, user_id):
        ''' Update user details '''
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, user_id):
        ''' Remove user '''
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200


