import db_connection as dbConn

class Create:
    def func_CreateData(self):

        connection = dbConn.getConnection()
        id = input('Enter Id = ')        
        name = input('Enter Name = ')
        age = input('Enter Age = ')

        try:
           query = "Insert Into Employee(ID, Name, Age) Values(?,?,?)" 
           cursor = connection.cursor()

           cursor.execute(query, [id, name, age])

           connection.commit()
           print('Data Saved Successfully')

        except:
             print('Something wrong, please check')

        finally:
           connection.close()
