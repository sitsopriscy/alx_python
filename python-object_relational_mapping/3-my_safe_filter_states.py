# Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
# What? Empty?

# Yes, it’s an SQL injection to delete all records of a table…

# Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

# Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
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

    # Execute the SQL query to retrieve states where name matches the argument and is injection safe
    cursor.execute(
        "SELECT * FROM states\
                    WHERE name LIKE %s\
                    ORDER BY states.id ASC",
        (argv[4],),
    )

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
