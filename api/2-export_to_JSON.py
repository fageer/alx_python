"""import json, requests, sys"""
import json
import requests
import sys
"""import json, requests, sys"""


def getData(id):
    """
    Get data from json api and export to json file
    """
    usersurl = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todourl = "{}/todos".format(usersurl)

    request1 = requests.get(usersurl)
    results = request1.json()
    userid = results['id']
    username = results['username']

    request2 = requests.get(todourl)
    tasks = request2.json()

    alldata = {}

    jsondata = [
            {"task": task['title'], "completed": task['completed'], "username": username}
            for task in tasks
        ]
    
    alldata[str(userid)] = jsondata

    with open("{}.json".format(userid), "w") as jsonfile:
        json.dump(alldata, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = sys.argv[1]
    else:
        id = 1
    getData(int(id))
