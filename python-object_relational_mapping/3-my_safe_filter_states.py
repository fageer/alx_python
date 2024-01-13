import MySQLdb
from sys import argv


conn = MySQLdb.connect(host='localhost', 
                       port=3306, 
                       user=argv[1], 
                       passwd=argv[2], 
                       database=argv[3])

cur = conn.cursor()


cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC".format((argv[4]),))

records = cur.fetchall()

for record in records:
    print(record)
