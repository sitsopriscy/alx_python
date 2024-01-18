# Write a script that lists all cities from the database hbtn_0e_4_usa

# Your script should take 3 arguments: mysql username, mysql password and database name
# You must use the module MySQLdb (import MySQLdb)
# Your script should connect to a MySQL server running on localhost at port 3306
# Results must be sorted in ascending order by cities.id
# You can use only execute() once
# Results must be displayed as they are in the example below
# Your code should not be executed when imported


import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]

    # Connecting to the MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    cursor = db.cursor()

    query = """SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id """
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
