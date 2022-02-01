import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='scoe.responsenetcloud.in',
                                         database='scoe_gauravg',
                                         user='scoe_gauravg',
                                         password='trytoH@ckme1')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
    
cursor.execute("SHOW DATABASES")
for ele in cursor:
    print(ele)
    
    
cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Gaurav", "Kopargaon")
cursor.execute(sql, val)

connection.commit()

print(cursor.rowcount, "record inserted.")


# finally:
#       if connection.is_connected():
#           cursor.close()
#           connection.close()
#           print("MySQL connection is closed")
          

          
          