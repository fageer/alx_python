"""importing the requests and sys packages"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    headers = {'Authorization': f'Bearer {password}'}
    response = requests.get("https://api.github.com/user", headers=headers)
    if response.status_code >= 400:
        print("None")
    else:
        print(response.json()["id"])
