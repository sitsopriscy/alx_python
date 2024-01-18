# Write a script that lists all states from the database hbtn_0e_0_usa:
# Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
# You must use the module MySQLdb (import MySQLdb)
# Your script should connect to a MySQL server running on localhost at port 3306
# Results must be sorted in ascending order by states.id
# Results must be displayed as they are in the example below
# Your code should not be executed when imported

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve states
    cursor.execute(
        "SELECT * FROM states\
                    WHERE name LIKE 'N%' COLLATE utf8mb4_bin\
                    ORDER BY states.id ASC"
    )

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
