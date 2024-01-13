import MySQLdb
from sys import argv


conn = MySQLdb.connect(host='localhost', 
                       port=3306, 
                       user=argv[1], 
                       passwd=argv[2], 
                       database=argv[3])

cur = conn.cursor()


cur.execute("SELECT id, name, states.name FROM cities"
            "JOIN states ON cities.state_id = states.id"
            "ORDER BY cities.id ASC")

records = cur.fetchall()

for record in records:
    print(record)
