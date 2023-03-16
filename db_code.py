import mysql.connector as mysql
mydb=mysql.connect(host='localhost',user='root',passwd='1234',database='frs')

def login_check1(username =None,password=None):
    mycursor=mydb.cursor()
    mycursor.execute("select * from login_table")
    result=mycursor.fetchall()
    for i,j in result:
        if i== username and j== password:
            return 1
    return 0 