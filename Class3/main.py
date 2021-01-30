import mysql.connector as Mysql

mysql = Mysql.connect(host="localhost",user="root",password="password123")

if(mysql):
    print("Connected")
else:
    print("Not Connected")