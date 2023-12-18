"""importing the requests and sys packages"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    value = response.headers.get('X-Request-Id')
    print(value)
