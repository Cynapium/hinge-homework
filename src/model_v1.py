from db import database

def getUserProfile(userId):
    ''' Return information about a given user '''

    sql = """SELECT id, first_name, description, birthdate
             FROM user
             WHERE id=""" + str(userId)

    user = database.executeQuery(sql)

    if user:
        user = user[0]
        user_columns = database.databaseSetup["tables"]["user"]["columns"]
        return {
            "id": user[0],
            "name": user[1],
            "description": user[2],
            "birthdate": user[3]
        }
    else:
        return {}

def createUserProfile(userProfile):
    ''' Create a new user '''
    user = {
        "first_name": userProfile["name"],
        "birthdate": userProfile["birthdate"],
        "description": userProfile["description"],
    }
    userId = database.insertRecord("user", user)
    userProfile["id"] = userId
    return userProfile


def updateUserProfile(userId, userProfile):
    ''' Update a user profile '''

    user = {
        "id": userId,
        "first_name": userProfile["name"],
        "birthdate": userProfile["birthdate"],
        "description": userProfile["description"],
    }

    userProfile["id"] = userId
    database.updateRecord("user", user, "id")
    return getUserProfile(userId)


def getListUsers():
    ''' Get list of all users '''
    
    userList = []

    queryResults = database.executeQuery("""SELECT id, first_name, description, birthdate
                                            FROM user""")
    user_columns = database.databaseSetup["tables"]["user"]["columns"]

    print(queryResults)

    for user in queryResults:
        userList.append({
            "id": user[0],
            "name": user[1],
            "description": user[2],
            "birthdate": user[3]
        })

    return userList


def getListIncomingLikes(user_id):
    ''' Return the list of incomming likes for a given user, minus people that
        the user has already rated '''

    users = database.executeQuery(
        """ SELECT r.user
            FROM rating r
            LEFT JOIN rating r2
             ON r.user=r2.user_target
             AND r.user_target=r2.user
            WHERE r2.type IS NULL
             AND r.type="L"
             AND r.user_target=""" + str(user_id))

    return users


def getListMatches(userId):
    ''' Return the list of matches for a given user '''

    userIds = database.executeQuery(
        """ SELECT r.user
            FROM rating r
            LEFT JOIN rating r2
             ON r.user=r2.user_target
             AND r.user_target=r2.user
            WHERE r.type="L"
             AND r2.type="L"
             AND r.user=""" + str(userId))

    return userIds


def getListRecommendations(userId):
    ''' Return the list of recommendations for a given user '''

    userIds = database.executeQuery(
        """ SELECT id
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
            )""".format(userId))

    return userIds


def setRating(ratingDetails):
    ''' '''
    
    database.insertRecord("rating", ratingDetails)
    return ratingDetails
