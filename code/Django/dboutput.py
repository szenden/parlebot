import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import sys
import mysql.connector
import yattag
from yattag import Doc


try:
   mySQLconnection = mysql.connector.connect(host='localhost',
                             database='parlebot',
                             user='root',
                             password='root',
                             port='8889')
   sql_select_Query = "select * from usertest"
   cursor = mySQLconnection .cursor()
   cursor.execute(sql_select_Query)
   records = cursor.fetchall()
   print("Total number of rows in usertest is - ", cursor.rowcount)
   print ("Printing each row's column values i.e.  developer record")
  
   columns = ['id','name','birth_date', 'age']
   attributes = []
   for row in records:
       attributes.append(dict(zip(columns,row)))

   #print(attributes[0]['id'])

   doc, tag, text, line = Doc().ttl()

   with tag('ul', id='grocery-list'):
    line('li', 'Tomato sauce', klass="priority")
    line('li', 'Salt')
    line('li', 'Pepper')

    print(doc.getvalue())

   #for row in records:
       #print("Id = ", row[0], )
       #print("Name = ", row[1])
       #print("Birth date  = ", row[2])
       #print("Age  = ", row[3], "\n")
   cursor.close()
   
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(mySQLconnection .is_connected()):
        mySQLconnection.close()
        print("MySQL connection is closed")