import requests


response = requests.get("https://alu-intranet.hbtn.io/status")
print(f"- type: {type(response.text)}")
print(f"- content: {response.text}")
