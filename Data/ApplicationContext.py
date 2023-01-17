import sqlite3
import json



class ApplicationContext():
    with open("./Data/Startup.json") as stringConnection:
        connection = json.load(stringConnection)
    database = connection['StartConnection']
    conn = None
    cursor = None
    connected = False


    def connect(self):
        ApplicationContext.conn = sqlite3.connect(ApplicationContext.database)
        ApplicationContext.cursor = ApplicationContext.conn.cursor()
        ApplicationContext.connected = True
        
    def disconnect(self):
        ApplicationContext.conn.close()
        ApplicationContext.connected = False

    def execute(self, sql, params =None):
        if ApplicationContext.connected:
            if params == None:
                ApplicationContext.cursor.execute(sql) 
            else:
                ApplicationContext.execute(sql, params)
                return True
        else:
            return False
    def fetchall(self):
        return ApplicationContext.cursor.fetchall()

    def persist(self):
        if ApplicationContext.connected:
            ApplicationContext.commit()
            return True
        else:
            return False

