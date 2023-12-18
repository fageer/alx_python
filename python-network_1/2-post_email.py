"""importing the requests and sys packages"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data=email)
    print(f"Email: {email}")
