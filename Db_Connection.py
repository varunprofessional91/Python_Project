import mysql.connector
from mysql.connector import Error

try:
    sql_con = mysql.connector.connect(host='localhost', database='jspweb', user='root', password='')
    sql_select_Query = "select * from acc_created"
    cursor = sql_con.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    # print("Total number of rows in python_developers is - ", cursor.rowcount)
    # print(pd.DataFrame(records))
    for row in records:
        print(" %s || %s || %s || %s ||  %s || %s || %s " % (row[0], row[1], row[2], row[3], row[4], row[7], row[8]))
    cursor.close()

except Error as e:
    print("MySql Connection Error!", e)
finally:
    # closing database connection.
    if sql_con.is_connected():
        sql_con.close()
        print("MySQL Connection Closed")
