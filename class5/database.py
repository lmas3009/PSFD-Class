import pymysql as Mysql

def mysql():
    sql = Mysql.connect(host="localhost",user="root",password="",database="psfd")
    mycursor = sql.cursor()
    return mycursor

