import MySQLdb
from sys import argv


conn = MySQLdb.connect(host='localhost', 
                       port=3306, 
                       user=argv[1], 
                       passwd=argv[2], 
                       database=argv[3])

cur = conn.cursor()


cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

records = cur.fetchall()

for record in records:
    if record [1][0] == 'N':
        print(record)


cur.close()
conn.close()
