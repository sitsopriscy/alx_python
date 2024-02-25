import json
import requests
import sys


def get_user_data(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(url, user_id)
    response = requests.get(user_url)
    return response.json()


def get_user_tasks(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    todos_url = "{}todos?userId={}".format(url, user_id)
    response = requests.get(todos_url)
    return response.json()


def export_to_json(user_id, user_data, tasks):
    filename = "{}.json".format(user_id)

    data_to_export = {
        str(user_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user_data.get("username"),
            }
            for task in tasks
        ]
    }

    with open(filename, "w") as json_file:
        json.dump(data_to_export, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])

    user_data = get_user_data(user_id)
    user_tasks = get_user_tasks(user_id)

    export_to_json(user_id, user_data, user_tasks)
    print(f"Data exported to {user_id}.json successfully.")
    
