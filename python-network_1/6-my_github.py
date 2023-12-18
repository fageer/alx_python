"""importing the requests and sys packages"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth(username, password))
    data = response.json()
    print(data.get("id"))
