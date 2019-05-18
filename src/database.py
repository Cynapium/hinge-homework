import sqlite3
from sqlite3 import Error

databaseName = "hinge.db"
#connection = None

def initializeDatabase():
    global connection
    #connection = sqlite3.connect(databaseName)

def executeQuery(request):
    """ Execute SQL requests """
    global connection
    results = []

    print ("Received request: ", request)

    try:
        with sqlite3.connect(databaseName) as connection:
            cursor = connection.cursor()
            cursor.execute(request)
            data = cursor.fetchall()
            if request.upper().startswith("SELECT"):
                results = data
    except Error as error:
        print ("An error occured: ", error.args[0])
        print ("For the request: ", request)

    return results

def insertRecord(table, record):
    global connection
    columns = []
    values  = []
    for key in record:
        columns.append(key)
        value = record[key]
        if isinstance(value, str):
            values.append('"' + value + '"')
        else:
            values.append(value)

    separator = ", "
    sql = "INSERT INTO " + table + " (" + separator.join(columns) + ") VALUES ("+ separator.join(values)+ ");"
    print (sql)

    try:
        with sqlite3.connect(databaseName) as connection:
            cursor = connection.cursor()
            ret = cursor.execute(sql)
            userId = cursor.lastrowid
            connection.commit()
            print(ret)
    except Error as error:
        print ("An error occured: ", error.args[0])
        print ("For the request: ", sql)

    return userId


