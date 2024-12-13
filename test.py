import psycopg2

# Update these values with your actual database connection details
HOST = "ec2-18-217-36-102.us-east-2.compute.amazonaws.com"
PORT = 5432
DATABASE = "madlib_db"
USER = "postgres"
PASSWORD = "MyPassword"

def main():
    # Establish the connection
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        dbname=DATABASE,
        user=USER,
        password=PASSWORD
    )

    # Create a cursor to execute the query
    cur = conn.cursor()

    # Execute the query
    cur.execute("DROP TABLE IF EXISTS myresults_summary CASCADE;")
    cur.execute("DROP TABLE IF EXISTS myresults CASCADE;")
    cur.execute("SELECT madlib.logregr_train('mydata','myresults','y','x');")
    cur.execute("SELECT * FROM myresults;")
    # Fetch all rows
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
