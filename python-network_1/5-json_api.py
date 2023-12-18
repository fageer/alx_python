"""importing the requests and sys packages"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    response = requests.post("http://0.0.0.0:5000/search_user", data=q)

    try:
        json_data = response.json()
        if not json_data:
            print("No result")
        else:
            json_id = json_data.get("id")
            json_name = json_data.get("name")
    except ValueError:
        print("Not a valid JSON")
    

    