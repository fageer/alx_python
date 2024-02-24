'''
This module export content from an api into a csv file define on creation
return : csv
'''
import csv
import requests
import sys

user_id = str(sys.argv[1])

user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)

user_data = requests.get(user_url).json()
todo_data = requests.get(todo_url).json()

filename = "{}.csv".format(user_id)

with open(filename, 'w', newline='') as file:
    writter = csv.writer(file, quoting = csv.QUOTE_ALL)
    for task in todo_data:
        writter.writerow([user_id, str(user_data['username']),task['completed'], task['title']])
        