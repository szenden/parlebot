import MySQLdb

db = MySQLdb.connect (unix_socket = '/Applications/MAMP/tmp/mysql/mysql.sock',
                    host = 'localhost',
                    user = 'root',
                    passwd = 'root',
                    db = 'parlebot')

cur = db.cursor() 

cur.execute("SELECT * FROM test")

for row in cur.fetchall() :
    print row[0]
    print row[1]