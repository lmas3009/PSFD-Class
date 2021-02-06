import pymysql as Mysql

mysql = Mysql.connect(host="localhost",user="root",password="",database="psfd")

mycursor = mysql.cursor()

cmd = "CREATE TABLE patients(name CHAR(20),age INT(10))"

mycursor.execute(cmd)

# mycursor.execute("show table hospital")
for tb in mycursor:
    print(tb)
mysql.close()