import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   connection = mysql.connector.connect(host='localhost',
                             database='parlebot',
                             user='root',
                             password='root',
                             port='8889')
   sql_insert_query = """ INSERT INTO `usertest`
                          (`id`, `name`, `birth_date`, `age`) VALUES (1,'Scott','test', 26)"""
   cursor = connection.cursor()
   result  = cursor.execute(sql_insert_query)
   connection.commit()
   print ("Record inserted successfully into python_users table")
except mysql.connector.Error as error :
    connection.rollback() #rollback if any exception occured
    print("Failed inserting record into python_users table {}".format(error))
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")