import database

def getUserProfile(user_id):
    ''' Return information about a given user '''

    user = database.executeQuery("SELECT * FROM user WHERE id=" + str(user_id))

    if user:
        user = user[0]
        user_columns = database.databaseSetup["tables"]["user"]["columns"]
        return {
            user_columns[0]["name"]: user[0],
            user_columns[1]["name"]: user[1],
            user_columns[2]["name"]: user[2],
            user_columns[3]["name"]: user[3],
            user_columns[4]["name"]: user[4],
            user_columns[5]["name"]: user[5],
            user_columns[6]["name"]: user[6],
            user_columns[7]["name"]: user[7],
            user_columns[8]["name"]: user[8],
        }
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
        userList.append({
            user_columns[0]["name"]: user[0],
            user_columns[1]["name"]: user[1],
            user_columns[2]["name"]: user[2],
            user_columns[3]["name"]: user[3],
            user_columns[4]["name"]: user[4],
            user_columns[5]["name"]: user[5],
            user_columns[6]["name"]: user[6],
            user_columns[7]["name"]: user[7],
            user_columns[8]["name"]: user[8],
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
