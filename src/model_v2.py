from db import database
from response import ClientException

def userProfileFromArray(userArray):

    userColumns = database.databaseSetup["tables"]["user"]["columns"]

    if len(userArray) != len(userColumns):
        return {}

    userProfile = {}
    for index in range(0, len(userColumns)):
        userProfile[userColumns[index]["name"]] = userArray[index]

    return userProfile


def getUserProfile(user_id):
    ''' Return information about a given user '''

    user = database.executeQuery("SELECT * FROM user WHERE id=" + str(user_id))

    if user:
        return userProfileFromArray(user[0])
    else:
        return {}


def createUserProfile(userProfile):
    ''' Create a new user '''
    userId = database.insertRecord("user", userProfile)
    userProfile["id"] = userId
    return userProfile


def updateUserProfile(userId, userProfile):
    ''' Update a user profile '''
    userProfile["id"] = userId
    database.updateRecord("user", userProfile, "id")
    return userProfile


def getListUsers():
    ''' Get list of all users '''
    
    userList = []

    queryResults = database.executeQuery("SELECT * FROM user")
    user_columns = database.databaseSetup["tables"]["user"]["columns"]

    for user in queryResults:
        userList.append(userProfileFromArray(user));

    return userList


def getListIncommingLikes(userId):
    ''' Return the list of incomming likes for a given user, minus people that
        the user has already rated '''

    userIds = database.executeQuery(
        """ SELECT r.user
            FROM rating r
            LEFT JOIN rating r2
             ON r.user=r2.user_target
             AND r.user_target=r2.user
            WHERE r.type="L"
             AND r2.type IS NULL
             AND r.user_target=""" + str(userId))

    likes = []
    for user in userIds:
        likes.append("/v2/users/" + str(user[0]))

    return likes


def getListMatches(userId):
    ''' Return the list of matches for a given user '''

    userIds = database.executeQuery(
        """ SELECT r.user_target
            FROM rating r
            LEFT JOIN rating r2
             ON r.user=r2.user_target
             AND r.user_target=r2.user
            WHERE r.type="L"
             AND r2.type="L"
             AND r.user=""" + str(userId))

    likes = []
    for user in userIds:
        likes.append("/v2/users/" + str(user[0]))

    return likes


def getListRecommendations(userId, filters):
    ''' Return the list of recommendations for a given user '''

    s = """ SELECT id
            FROM user
            WHERE id!={0}
            AND id NOT IN (
                SELECT user
                FROM rating
                WHERE user_target={0}
            )
            AND id NOT IN (
                SELECT user_target
                FROM rating
                WHERE user={0}
            )""".format(userId)

    for filterName in filters:
        value = filters[filterName]
        if value == None:
            continue
        if isinstance(value, str):
            value = '"' + value + '"'
        else:
            value = str(value)
        s += " AND ({0}={1} OR {0} IS NULL) ".format(filterName, value)

    userIds = database.executeQuery(s)

    recommendations = []
    for user in userIds:
        recommendations.append("/v2/users/" + str(user[0]))

    return recommendations


def setRating(ratingDetails):
    ''' '''

    if ratingDetails["user"] == ratingDetails["user_target"]:
        raise ClientException("user and user_target are equal")
    
    database.insertRecord("rating", ratingDetails)
    return ratingDetails
