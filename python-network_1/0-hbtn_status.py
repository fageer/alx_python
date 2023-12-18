import requests


response = requests.get("https://alu-intranet.hbtn.io/status")
print(f"type: {type(response)}")
print(f"type: {response.text}")
