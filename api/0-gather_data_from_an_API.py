import requests
import sys


def getData(id):
    usersurl = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    request1 = requests.get(usersurl)
    result = request1.json()
    name = result['name']
    todourl = "{}/todos".format(usersurl)
    request2 = requests.get(todourl)
    results = request2.json()

    tasksTitles = []
    count = 0
    for result in results:
        if result['completed']:
            count += 1
            tasksTitles.append(result['title'])
    
        
    print("Employee {} is done with tasks({}/{}):".format(name, count, len(results)))
    for task in tasksTitles:
        print("\t {}".format(task))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = sys.argv[1]
    else:
        id = 1
    getData(id)
