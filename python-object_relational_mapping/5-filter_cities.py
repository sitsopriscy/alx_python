# Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

# Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
# You must use the module MySQLdb (import MySQLdb)
# Your script should connect to a MySQL server running on localhost at port 3306
# Results must be sorted in ascending order by cities.id
# You can use only execute() once
# The results must be displayed as they are in the example below
# Your code should not be executed when imported


import MySQLdb
from sys import argv


def filter_cities(username, password, database, state_name):
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    cursor = db.cursor()

    query = "SELECT name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = %s) ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(argv[0]))
        exit(1)

    username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]

    filter_cities(username, password, database, state_name)
