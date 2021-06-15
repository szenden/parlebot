import sqlite3

cnx = sqlite3.connect ('parlebot.db')

# (host='localhost', port=8889, user='root', password='root', db='parlebot')

insert_query = ("INSERT INTO test VALUES (3, 'titel', 'vraag1', 'vraag2')")

cursor = cnx.cursor()
cursor.execute(insert_query)

cnx.commit()
cursor.close()
cnx.close()