import pymysql
import dbconfig
import datetime
from decimal import Decimal
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

    def add_crime(self, category, date, latitude, longitude, description):
        connection = self.connect()
        try:
            sql_query = "INSERT INTO crimes (category, date, latitude, longitude, description) VALUES (%s, %s, %s, %s, %s)"
            with connection.cursor() as cursor:
                cursor.execute(sql_query, (category, 
                                        date, 
                                        latitude, 
                                        longitude,
                                        description))
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()
    
    def get_all_crimes(self):
        connection = self.connect()
        try:
            sql_query = "SELECT latitude, longitude, date, category, description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
            named_crimes = [] 
            for crime in cursor:
                named_crime = {
                    'latitude': float(crime[0]),
                    'longitude': float(crime[1]),
                    'date': datetime.datetime.strftime(crime[2],"%Y-%m-%d"),
                    'category': crime[3],
                    'description': crime[4]
                }
                named_crimes.append(named_crime)
            return named_crimes
        finally:
            connection.close()
        
        
    """
    def get_all_crimes_mock(self):
            named_crimes = [{ 
                    'latitude': -33.301304,
                    'longitude': 26.523355,
                    'date': "2000-01-01",
                    'category': "mugging",
                    'description': "mock description"
                }]
            return named_crimes
    """       