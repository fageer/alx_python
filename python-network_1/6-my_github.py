"""importing the requests and sys packages"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = {'Authorization': f'Bearer {password}'}
    response = requests.get("https://api.github.com/usrs", auth=auth)
    if response.status_code >= 400:
        print("None")
        print(response.json()["id"])
