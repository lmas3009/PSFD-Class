import mysql.connector as a
mydb = a.connect(host="localhost",user="root",password = "password123")
if(mydb):
    print("Connected")
else:
    print("Not Connected")