import pymysql as Mysql

mysql = Mysql.connect(host="localhost", user="root",
                      password="", database="psfd")

mycursor = mysql.cursor()

cmd = "Insert into patients(name,age) values('Lohit',34)"

mycursor.execute(cmd)
mysql.commit()
