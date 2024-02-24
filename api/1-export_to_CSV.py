import csv
import requests
import sys


def getData(id):
    usersurl = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todourl = "{}/todos".format(usersurl)

    request1 = requests.get(usersurl)
    result = request1.json()
    userid = result['id']
    username = result['username']

    request2 = requests.get(todourl)
    results = request2.json()

    with open("{}.csv".format(userid), "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
        for result in results:
            writer.writerow([userid, username, result['completed'], result['title']])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = sys.argv[1]
    else:
        id = 1
    getData(id)
