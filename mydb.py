import mysql.connector

dataBase=mysql.connector.connect(
    host = 'bj-cynosdbmysql-grp-bmbmqkk2.sql.tencentcdb.com',
    user ='wikigao',
    passwd ='wikigao123,',
    port = '20092',
)

#prepare a cursor object
cursorObject=dataBase.cursor()

#create a database

cursorObject.execute("CREATE DATABASE eldercogao")

print("all done")