import MySQLdb
from sys import argv


conn = MySQLdb.connect(host='localhost', 
                       port=3306, 
                       user=argv[1], 
                       passwd=argv[2], 
                       database=argv[3])

cur = conn.cursor()


cur.execute("""SELECT GROUP_CONCAT(name ORDER BY id ASC SEPARATOR ', ')
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                """, (argv[4], ))

records = cur.fetchall()

if records:
    print(records)
else:
    print("")
