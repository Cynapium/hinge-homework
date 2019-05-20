import sqlite3
import json
import database

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print (e)
    return None


def insertDummyData(cursor, dataFile):
    with open(dataFile, 'r') as f:
        for line in f:
            if not line.startswith("#"):
                print(line, end =" ")
                cursor.execute(line)


def dropTable(cursor, tableName):
    try:
        sql = "DROP TABLE " + tableName
        cursor.execute(sql)
    except Exception as e:
        print ("Error: " + str(e))

def createTable(cursor, tableName, tableInfo):

    columns = tableInfo["columns"]

    sql = "CREATE TABLE " + tableName + " ("
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
        elif key["type"] == "foreign":
            sql += ", FOREIGN KEY (" + key["column"] + ") REFERENCES " + key["references"]

    sql += ");"

    print (sql)

    try:
        #cursor = connection.cursor()
        cursor.execute(sql)
        #connection.commit()
    except Exception as e:
        print ("Error: " + str(e))


def loadTables(cursor, setupFile):
    with open(setupFile, 'r') as f:
        databaseSetup = json.load(f)

    for tableName in databaseSetup["tables"]:
        dropTable(cursor, tableName)
        createTable(cursor, tableName, databaseSetup["tables"][tableName])


def setup_database(databaseName):
    with sqlite3.connect(databaseName) as connection:
        cursor = connection.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")
        loadTables(cursor, "src/db/schema_database.json")
        insertDummyData(cursor, "src/db/test_data.sql")

        connection.commit()

if __name__ == '__main__':
    setup_database("src/db/hinge-homework-barbara.db")
