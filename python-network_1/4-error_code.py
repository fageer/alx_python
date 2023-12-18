"""importing the requests and sys packages"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    body = response.text
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(body)