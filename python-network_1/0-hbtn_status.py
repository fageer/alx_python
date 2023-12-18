"""importing the requests package"""
import requests


if __name__ == "__main__":
    """get the body of the response"""
    response = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")