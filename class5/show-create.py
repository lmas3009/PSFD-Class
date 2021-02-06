import pymysql as Mysql

mysql = Mysql.connect(host="localhost",user="root",password="",database="psfd")

mycursor = mysql.cursor()
# for creating
mycursor.execute("Create Database Hospital")

# for showing the database
mycursor.execute("show databases")
for db in mycursor:
    print(db)
