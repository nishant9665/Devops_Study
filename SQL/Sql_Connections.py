import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='world'
)

# Create a cursor object
cursor = connection.cursor()

# Example query
cursor.execute("select * from world.country;")

# Fetch the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the connection
connection.close()
