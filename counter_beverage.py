import RPi.GPIO as IO
import time
import pymssql


def dbconnect():
    # Set database connection parameters
    server = 'servername'
    user = 'username'
    password = 'password'
    database = 'database'

    # Connect to the database
    conn = pymssql.connect(server=server, user=user,
    password=password, database=database)

    # Return the connection object
    return conn

time.sleep(60)
conn = dbconnect()
cur = conn.cursor()
IO.setmode(IO.BOARD)
IO.setup(15, IO.IN)
count = 0
counter = 0
while True:
    if IO.input(15) == 1:
        count = count + 1
        if count == 1:
            counter = counter + 1
            try:
                cur.execute("INSERT INTO table (counter) VALUES (%d)",
                ('1'))
                conn.commit()
                print("counter -->" + str(counter))
            except TypeError as e:
                print(e)
                conn.close()
                conn = dbconnect()
                pass
    else:
        count = 0
