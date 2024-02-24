"""import json, requests"""
import json
import requests
"""import json, requests"""


def getData():
    """
    Get data from json api and export to json file
    """
    usersurl = "https://jsonplaceholder.typicode.com/users"

    request1 = requests.get(usersurl)
    results = request1.json()

    alldata = {}

    for result in results:
        username = result['username']
        userid = result['id']
        todourl = "https://jsonplaceholder.typicode.com/users/{}/todos".format(userid)
        request2 = requests.get(todourl)
        tasks = request2.json()
        jsondata = [
                {"username": username, "task": task['title'], "completed": task['completed']}
                for task in tasks
            ]
        
        alldata[str(userid)] = jsondata

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(alldata, jsonfile)


if __name__ == "__main__":
    getData()
