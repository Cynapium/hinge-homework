import sqlite3
from sqlite3 import Error
import json

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print (e)
    return None


def createTable(connection, tableName, tableInfo):

    columns = tableInfo["columns"]

    sql = "CREATE TABLE IF NOT EXISTS " + tableName + " ("
    tables = []
    for col in columns:
        c = col["name"] + " " + col["type"]
        if col.get("mandatory", 0):
            c += " NOT NULL"
        tables.append(c)
    sql += ", ".join(tables)

    for key in tableInfo["keys"]:
        if key["type"] == "primary":
            sql += ", PRIMARY KEY (" + key["columns"] + ")"

    sql += ");"

    print (sql)

    try:
        cursor = connection.cursor()
        #cursor.execute("drop table " + tableName)
        #connection.commit()
        cursor.execute(sql)
        connection.commit()
    except Error as e:
        print ("Error: " + e)


def loadTables(connection, setupFile):
    with open(setupFile, 'r') as f:
        databaseSetup = json.load(f)

    for tableName in databaseSetup["tables"]:
        createTable(connection, tableName, databaseSetup["tables"][tableName])
    

def setup_database(db_file):
    connection = create_connection(db_file)
    loadTables(connection, "schema_database.json")
    connection.close()

if __name__ == '__main__':
    setup_database("hinge.db")
