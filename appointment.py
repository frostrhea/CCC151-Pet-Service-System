import mysql.connector


try:
    connection = mysql.connector.connect(
        host="",
        user="",
        password="",
        database="dbpetservice"
    )
    if connection.is_connected():
        print("Connected to MySQL database.")
except mysql.connector.Error as error:
    print("Error connecting to MySQL database:", error)


#WIP