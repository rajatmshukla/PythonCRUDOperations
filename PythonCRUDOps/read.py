import db_connection as dbConn

class Read:
    def func_ReadData(self):   
        
        connection = dbConn.getConnection()
        cursor = connection.cursor()

        cursor.execute('select * from Employee')

        for row in cursor:
            print('row = %r' % (row,))
