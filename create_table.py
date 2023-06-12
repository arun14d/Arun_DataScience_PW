import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not EXISTS test1") ## carries a sql query
mycursor.execute("CREATE TABLE if not exists test1.test_table ( c1 INT , c2 VARCHAR(50), c3 INT , c4 FLOAT ,c5 VARCHAR(40))")
mydb.close() ## we are supposed to call all the time
# code - 0 - Successfully completed in Python
# code -  1 - not successfully