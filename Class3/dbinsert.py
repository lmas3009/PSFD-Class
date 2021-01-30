import mysql.connector as Mysql

mysql = Mysql.connect(host="localhost", user="root",
                      password="password123", database="EmployeeDB")

mycursor = mysql.cursor()

form = "Insert into employee(name,salary) values(%s,%s)"
employee = [{"Lohit", 123}, {"Teja", 152}]
mycursor.executemany(form, employee)
mysql.commit()
