import pymysql

conn= pymysql.connect(host="localhost", user="root", passwd="root", db="parlebot")
myCursor = conn.cursor()

myCursor.executee("INSERT INTO test(title, question1, question2) VALUES('test', 'test1', 'test2');")