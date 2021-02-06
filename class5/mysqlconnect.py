import pymysql as a
mydb = a.connect(host="localhost",user="root",password = "",database="psfd")
if(mydb):
    print("Connected")
else:
    print("Not Connected")