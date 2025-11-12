def start():
    print("dit is felix")
    return "dit is van felix"

def krijgkaarten():
    import mysql.connector

    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",      # or your server IP
        user="root",           # your MySQL username
        password="root",
        database="yugiohdb"
    )

    # Create a cursor
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM kaart")

    # Fetch all results
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    conn.close()
