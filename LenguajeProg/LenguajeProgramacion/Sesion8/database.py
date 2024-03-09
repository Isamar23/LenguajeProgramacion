import mysql.connector
import os

class MYSQLBD:
    def __init__(self,host, user, password, database):
        self.host = host
        self.user = user
        self.pw = password
        self.db = database
        
    def connect(self):
        try:
            if(self.connect == None):
              self.connection = mysql.connector.connect(
               host = self.host,
               user = self.user,
               password = self.pw,
             database = self.db
           )

        except mysql.connector.error as error:
         print("error mientras se estaba conectando {}".format(error))
    def disconect(self):
        try:
            if self.connection:
                self.connection.close()
                self.connection = None
        except mysql.connector.error as error:
            print("error")
    def execute_query (self,query, params = None):
         try:
             cursor = self.connection.Cursor
             cursor.execute(query,params)
             result = cursor.fetchall()
             return result
         except mysql.connector.Error as error:
             print(f"Error: {error}")
                
            
db =MYSQLBD("localhost","root","","testlp")
print("conectado")

db.connect()
#db.disconnect()
categorias = db.execute_query("select * from categorias")
print (categorias)

#db.disconnect()

       
          