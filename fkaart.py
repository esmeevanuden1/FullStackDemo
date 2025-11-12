def start():
    print("dit is felix")
    return krijgkaarten()

def krijgkaarten():
    import mysql.connector

    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",      # or your server IP
        user="root",           # your MySQL username
        password="",
        database="yugiohdb"
    )

    # Create a cursor
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM kaart")

    # Fetch all results
    rows = cursor.fetchall()

    # Display the results
    eindstring = "["
    for row in rows:
        print(row)
        eindstring += "{\"naam\":\""+row[2]+"\"},"

    # Clean up
    cursor.close()
    conn.close()
    return eindstring[:-1] +"]"

