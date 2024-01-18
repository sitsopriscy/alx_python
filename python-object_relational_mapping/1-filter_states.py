# Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
# Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
# You must use the module MySQLdb (import MySQLdb)
# Your script should connect to a MySQL server running on localhost at port 3306
# Results must be sorted in ascending order by states.id
# Results must be displayed as they are in the example below
# Your code should not be executed when imported


import MySQLdb
from sys import argv


def filter_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Executing the SQL query to fetch states starting with 'n' (case-insensitive)
    query = "SELECT * FROM states WHERE LOWER(name) LIKE 'n%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]

    # Call the function to filter and display states
    filter_states(username, password, database)
