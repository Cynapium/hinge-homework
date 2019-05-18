from flask_restful import Api, Resource, reqparse
import database
from http import HTTPStatus
import datetime

def getRatingCode(rating):
    if rating == "likes":
        return "L"
    elif rating == "matches":
        return "M"
    elif rating == "blocks":
        return "B"
    elif rating == "report":
        return "R"
    else:
        return ""

class Likes(Resource):

    def get(self, version, user_id):
        ''' Get list of all incomming likes for that given user '''

        result = { "likes": [] }

        try:
            if (version == "v1"):
                result["likes"] = model_v1.getListIncommingLikes(user_id)
            elif (version == "v2"):
                result["likes"] = model_v2.getListIncommingLikes(user_id)
            else:
                raise Exception("Unrecognized version " + version)

        except Exception as e:
            response = ErrorResponse(Status.SERVER_ERROR,                    \
                                     "Could not retrieve list of all users", \
                                     details=str(e))
            return response.dump()

        return result, HTTPStatus.OK


class Rating(Resource):

    def post(self, user_id, rating, user_target):
        ''' Create new rating from user_id to user_target '''

        result = { "rating": {} }

        try:
            ratingCode = getRatingCode(rating)
            if ratingCode == "":
                return "Unsupported rating type", HTTPStatus.NOT_FOUND

            ratingDetails = {
                "user": user_id,
                "user_target": user_target,
                "type": ratingCode,
                "time": str(datetime.datetime.now())
            }

            if (version == "v1"):
                result["rating"] = model_v1.setRating(ratingDetails)
            elif (version == "v2"):
                result["rating"] = model_v2.setRating(ratingDetails)
            else:
                raise Exception("Unrecognized version " + version)

        except Exception as e:
            response = ErrorResponse(Status.SERVER_ERROR,                    \
                                     "Could not retrieve list of all users", \
                                     details=str(e))
            return response.dump()

        return result, HTTPStatus.OK
