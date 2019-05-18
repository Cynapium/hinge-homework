import database

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
    userProfile = {
        "first_name": userProfile["name"],
        "birthdate": userProfile["birthdate"],
        "phone": userProfile["phone"],
        "email": userProfile["email"]
    }
    userId = database.insertRecord("user", userProfile)
    userProfile["id"] = userId
    return userProfile

def updateUserProfile(userId, userProfile):
    ''' Update a user profile '''

    userProfile = {
        "first_name": userProfile["name"],
        "birthdate": userProfile["birthdate"],
        "phone": userProfile["phone"],
        "email": userProfile["email"]
    }

    userProfile["id"] = userId
    database.updateRecord("user", userProfile, "id")
    return userProfile

def getListUsers():
    ''' Get list of all users '''
    
    userList = []

    queryResults = database.executeQuery("""SELECT id, first_name, description, birthdate
                                            FROM user""")
    user_columns = database.databaseSetup["tables"]["user"]["columns"]

    for user in queryResults:
        userList.append({
            "id": user[0],
            "name": user[1],
            "description": user[2],
            "birthdate": user[3]
        })

    return userList

def getListIncommingLikes(user_id):
    ''' Return the list of incomming likes for a given user, minus people that
        the user has already rated '''

    users = database.executeQuery(
        """ SELECT i.user
            FROM interaction i
            LEFT JOIN interaction i2
             ON i.user=i2.user_target
             AND i.user_target=i2.user
            WHERE i2.user_target IS NULL
             AND i.user_target=""" + str(user_id))

    print(users)
    return users

def getListMatches(user_id):
    ''' Return the list of Matches for a given user_id'''

def getListDiscovery(user_id):
    ''' Return the list of people whith whom the user hasn't interacted yet,
        and whose people haven't interacted with the user either. '''

