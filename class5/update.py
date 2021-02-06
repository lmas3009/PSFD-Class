import pymysql as Mysql

mysql = Mysql.connect(host="localhost", user="root",
                      password="", database="psfd")

mycursor = mysql.cursor()

cmd = "UPDATE patients SET name='Amit' where id='1'"
res = mycursor.execute(cmd)
print(res)

