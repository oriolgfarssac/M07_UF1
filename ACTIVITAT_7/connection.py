import psycopg2

conn = psycopg2.connect(
    database="",
    user="",
    password="",
    host="localhost",
    port=""
)

connection = conn.cursor()
print(connection)
