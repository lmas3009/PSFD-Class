import mysql.connector as Mysql

mysql = Mysql.connect(host="localhost",user="root",password="password123")

mycursor = mysql.cursor()
# for creating
mycursor.execute("Create Database EmployeeDB")

# for showing the database
mycursor.execute("show databases")
for db in mycursor:
    print(db)
