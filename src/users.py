from flask_restful import Api, Resource, reqparse
import database
from http import HTTPStatus
from response import *
import model_v1
import model_v2

class User(Resource):

    def get(self, version, user_id):
        ''' Get user info '''

        result = { "user": {} }

        try:
            if (version == "v1"):
                result["user"] = model_v1.getUserProfile(user_id)
            elif (version == "v2"):
                result["user"] = model_v2.getUserProfile(user_id)
            else:
                raise Exception("Unrecognized version " + version)

            if not result["user"]:
                response = ErrorResponse(Status.NOT_FOUND, "User not found")
                return response.dump()

        except Exception as e:
            response = ErrorResponse(Status.SERVER_ERROR,                   \
                                     "Could not retrieve user information", \
                                     details=str(e))
            return response.dump()

        return result, Status.OK


    def put(self, version, user_id):
        ''' Update user details '''

        result = { "user":  {} }

        try:
            if (version == "v1"):
                parser = reqparse.RequestParser()
                parser.add_argument("name")
                parser.add_argument("birthdate")
                parser.add_argument("description")
                userInfo = parser.parse_args()

                result["user"] = model_v1.updateUserProfile(user_id, userInfo)

            elif (version == "v2"):
                userColumns = database.databaseSetup["tables"]["user"]["columns"]
                parser = reqparse.RequestParser()
                for column in userColumns:
                    parser.add_argument(column["name"])
                userInfo = parser.parse_args()

                result["user"] = model_v2.updateUserProfile(user_id, userInfo)

            else:
                raise Exception("Unrecognized version " + version)

        except Exception as e:
            response = ErrorResponse(Status.SERVER_ERROR,                   \
                                     "Could not update user information",   \
                                     details=str(e))
            return response.dump()

        return result, Status.OK



class Users(Resource):

    def get(self, version):
        ''' Get list of all the users '''

        result = { "users": [] }

        try:
            if (version == "v1"):
                result["users"] = model_v1.getListUsers()
            elif (version == "v2"):
                result["users"] = model_v2.getListUsers()
            else:
                raise Exception("Unrecognized version " + version)

        except Exception as e:
            response = ErrorResponse(Status.SERVER_ERROR,                    \
                                     "Could not retrieve list of all users", \
                                     details=str(e))
            return response.dump()

        return result, HTTPStatus.OK


    def post(self, version):
        ''' Create new user '''

        result = { "user":  {} }

        try:
            userInfo = {}

            # If V1, manually parse the input to populate a user object
            if (version == "v1"):
                parser = reqparse.RequestParser()
                parser.add_argument("name")
                parser.add_argument("birthdate")
                parser.add_argument("description")
                userInfo = parser.parse_args()

                result["user"] = model_v1.createUserProfile(userInfo)

            # If V2, automatically parse the input from database columns
            elif (version == "v2"):
                userColumns = database.databaseSetup["tables"]["user"]["columns"]
                parser = reqparse.RequestParser()
                for column in userColumns:
                    parser.add_argument(column["name"])
                userInfo = parser.parse_args()

                result["user"] = model_v2.createUserProfile(userInfo)

            # If unrecognized version
            else:
                raise Exception("Unrecognized version " + version)

        except Exception as e:
            response = ErrorResponse(Status.SERVER_ERROR,                    \
                                     "Could not retrieve list of all users", \
                                     details=str(e))
            return response.dump()

        return result, HTTPStatus.OK
