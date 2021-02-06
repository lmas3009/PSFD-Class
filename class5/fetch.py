import pymysql as Mysql

mysql = Mysql.connect(host="localhost",user="root",password="",database="psfd")

mycursor = mysql.cursor()

mycursor.execute("select * from patients")

res = mycursor.fetchall()
print(res)

mysql.close()