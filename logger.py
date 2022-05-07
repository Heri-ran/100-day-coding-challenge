import sqlite3

class LoggerDB:
    def __init__(self) -> None:
        pass

    def connect_db(self, db_type, db_name, params):
        try:
            if (db_type == "mysql"):
                raise MySQLDBException(params)

            sqliteConnection = sqlite3.connect('resources/gamedb.db')
            cursor = sqliteConnection.cursor()
            print("Database created and Successfully Connected to SQLite")

            sqlite_select_Query = "select sqlite_version();"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            print("SQLite Database Version is: ", record)
            cursor.close()

        except MySQLDBException as exception:
            print("Process for mysqlConnexion")

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

class MySQLDBException(Exception):
    params : object
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.params = args

    