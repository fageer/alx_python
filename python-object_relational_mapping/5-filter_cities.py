import MySQLdb
from sys import argv


conn = MySQLdb.connect(host='localhost', 
                       port=3306, 
                       user=argv[1], 
                       passwd=argv[2], 
                       database=argv[3])


cur = conn.cursor()


cur.execute("""SELECT name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY id ASC
                """, (argv[4], ))


print(", ".join(map(lambda x: x[0], cur.fetchall())))
