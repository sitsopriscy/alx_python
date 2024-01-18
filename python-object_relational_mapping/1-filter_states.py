# Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
# Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
# You must use the module MySQLdb (import MySQLdb)
# Your script should connect to a MySQL server running on localhost at port 3306
# Results must be sorted in ascending order by states.id
# Results must be displayed as they are in the example below
# Your code should not be executed when imported


import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    # Extract username, password, and database name from command-line arguments
    username, password, database = argv[1], argv[2], argv[3]

    # Connecting to the MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Executing the SQL query to fetch states starting with 'n' (case-insensitive)
    query = "SELECT * FROM states WHERE LOWER(name) LIKE '%n' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the fetched rows
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
