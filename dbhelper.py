import pymysql
import dbconfig

class DBHelper:
    def connect(self, database="crimemap"):
        return pymysql.connect(host='localhost',
                               user=dbconfig.db_user,
                               passwd=dbconfig.db_password,
                               db=database)
    def select_all(self):
        connection = self.connect()
        try:
            sql_query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
            return cursor.fetchall()
        finally:
            connection.close()
    
    def insert(self, data):
        connection = self.connect()
        try:
            sql_query = "INSERT INTO crimes (description) VALUES ('{}');".format(data)
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                connection.commit()
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            sql_query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                connection.commit()
        finally:
            connection.close()
    

