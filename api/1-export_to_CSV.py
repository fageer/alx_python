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

    with open("{}.csv".format(userid), "w") as csvfile:
        columnnames = ["USER_ID", "USER_NAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=columnnames)
        writer.writeheader()
        for result in results:
            userdict = {
                "USER_ID": userid,
                "USER_NAME": username,
                "TASK_COMPLETED_STATUS": result['completed'],
                "TASK_TITLE": result['title']
            }
            writer.writerow(userdict)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = sys.argv[1]
    else:
        id = 1
    getData(id)
