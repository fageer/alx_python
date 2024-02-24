import json
import requests
import sys
"""import json, requests, sys"""


def getData(id):
    usersurl = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todourl = "{}/todos".format(usersurl)

    request1 = requests.get(usersurl)
    result = request1.json()
    userid = result['id']
    username = result['username']

    request2 = requests.get(todourl)
    tasks = request2.json()

    jsondata = {
        str(userid): [
            {"task": task['title'], "completed": task['completed'], "username": username}
            for task in tasks
        ]
    }

    with open("{}.json".format(userid), "w") as jsonfile:
        json.dump(jsondata, jsonfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = sys.argv[1]
    else:
        id = 1
    getData(id)
