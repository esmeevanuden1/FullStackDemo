def start(): 
    print("dit is esmee")
    return krijgspelers2() 


def krijgspelers():
    import mysql.connector

    # Connect to MySQL
    conn = mysql.connector.connect(
        host="127.0.0.1",      # or your server IP
        user="root",           # your MySQL username
        password="",
        database="yugiohdb"
    )

    # Create a cursor
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM spelers")

    # Fetch all results
    rows = cursor.fetchall()

    
    # Display the results
    eindstring = "["
    for row in rows:
        print(row)
        eindstring += "{\"naam\":\""+str (row[2])+"\"},"

    # Clean up
    cursor.close()
    conn.close()
    return eindstring[:-1] +"]"


krijgspelers()

def krijgspelers2():
    import mysql.connector

    # Connect to MySQL
    conn = mysql.connector.connect(
        host="127.0.0.1",      # or your server IP
        user="root",           # your MySQL username
        password="",
        database="yugiohdb"
    )

    # Create a cursor
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM spelers")

    # Fetch all results
    rows = cursor.fetchall()
    keys = [i[0] for i in cursor.description]

    data = [
        dict(zip(keys, row)) for row in rows
    ]
    return data