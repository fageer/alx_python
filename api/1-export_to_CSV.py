import csv
import requests
import sys

def get_data(user_id):
    # Construct URLs for user and user's tasks
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = "{}/todos".format(user_url)

    try:
        # Fetch user data
        response = requests.get(user_url)
        response.raise_for_status()  # Raise an error for unsuccessful requests
        user_data = response.json()
        username = user_data['username']

        # Fetch user's tasks
        response = requests.get(todo_url)
        response.raise_for_status()  # Raise an error for unsuccessful requests
        tasks = response.json()

        # Write data to CSV file
        with open("{}.csv".format(user_id), "w", newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in tasks:
                writer.writerow([user_id, username, task['completed'], task['title']])
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    except KeyError:
        print("Error: User data incomplete or in unexpected format.")

if __name__ == "__main__":
    # Check if a user ID is provided as a command-line argument
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        try:
            user_id = int(user_id)  # Convert user ID to integer
        except ValueError:
            print("Error: User ID must be an integer.")
            sys.exit(1)
        get_data(user_id)
    else:
        print("Error: Please provide a user ID as a command-line argument.")
        sys.exit(1)
