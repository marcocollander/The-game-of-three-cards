import mysql.connector

mydb = mysql.connector.connect(
    host="raubuc.net",
    user="marcocollander",
    password="Mqalf5942vxegs",
    database="marco_collander_1"
)

my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM threecards")

my_result = my_cursor.fetchall()

for x in my_result:
    print(x)