import requests
"""importing the requests package"""

if __name__ == "__main__":
    """get the body of the response"""
    response = requests.get("https://alu-intranet.hbtn.io/status")
    print(f"- type: {type(response.text)}")
    print(f"- content: {response.text}")
