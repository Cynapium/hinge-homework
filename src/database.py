import json
import sqlite3
from sqlite3 import Error

databaseName = None
databaseSetup = None


def initializeDatabase(name, setupFile):
    global databaseSetup
    global databaseName

    databaseName = name
    with open(setupFile, 'r') as f:
        databaseSetup = json.load(f)


def executeQuery(request):
    """ Execute SQL requests """
    global connection
    results = []

    print ("Received request: ", request)

    try:
        with sqlite3.connect(databaseName) as connection:
            cursor = connection.cursor()
            cursor.execute(request)
            results = cursor.fetchall()
    except Error as error:
        print ("An error occured: ", error.args[0])
        print ("For the request: ", request)

    return results

def insertRecord(table, record):
    global connection
    columns = []
    values  = []
    for key in record:
        value = record[key]
        if value != None:
            columns.append(key)
            if isinstance(value, str):
                values.append('"' + value + '"')
            else:
                values.append(str(value))

    separator = ", "
    sql = "INSERT INTO " + table + " (" + separator.join(columns) + ") VALUES ("+ separator.join(values)+ ");"
    print (sql)

    with sqlite3.connect(databaseName) as connection:
        cursor = connection.cursor()
        ret = cursor.execute(sql)
        userId = cursor.lastrowid
        connection.commit()
        return userId

    return 0


def updateRecord(table, record, whereColumns):
    global connection

    # Build the "SET" with the list of columns to update
    updateSet = []
    updateWhere = []
    for key in record:
        # Format value
        value = record[key]
        if isinstance(value, str):
            value = key + '="' + value + '"'
        else:
            value = key + "=" + str(value)
        # Add to where clause or set list
        if key in whereColumns:
            updateWhere.append(value)
        elif record[key] != None:
            updateSet.append(value)

    separator = ", "
    sql =  "UPDATE " + table
    sql += " SET " + ", ".join(updateSet)
    sql += " WHERE " + ", ".join(updateWhere)
    print (sql)

    try:
        with sqlite3.connect(databaseName) as connection:
            cursor = connection.cursor()
            ret = cursor.execute(sql)
            userId = cursor.lastrowid
            connection.commit()
    except Error as error:
        print ("An error occured: ", error.args[0])
        print ("For the request: ", sql)

    return 0


