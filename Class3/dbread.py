import mysql.connector as Mysql

mysql = Mysql.connect(host="localhost", user="root",
                      password="password123", database="EmployeeDB")

mycursor = mysql.cursor()

mycursor.execute("select * from employee")

myresult = mycursor.fetchall()
for row in myresult:
    print(row)
