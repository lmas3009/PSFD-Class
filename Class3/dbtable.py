import mysql.connector as Mysql

mysql = Mysql.connect(host="localhost",user="root",password="password123",database="EmployeeDB")

mycursor = mysql.cursor()
mycursor.execute("Create table employee(name varchar(200), salary int(20)")

mycursor.execute("show table employee")
for tb in mycursor:
    print(tb)