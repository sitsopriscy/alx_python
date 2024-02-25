""" Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv """

import csv
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


def write_to_csv(user_id, username, tasks):
    filename = "{}.csv".format(user_id)

    with open(filename, mode="w", newline="") as employee_file:
        employee_writer = csv.writer(
            employee_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )

        for task in tasks:
            employee_writer.writerow(
                [user_id, username, task.get("completed"), task.get("title")]
            )


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])

    user_data = get_user_data(user_id)
    username = user_data.get("username")  # Store username
    user_tasks = get_user_tasks(user_id)

    # For each task, store relevant data in l_task
    l_task = []
    for task in user_tasks:
        l_task.append([user_id, username, task.get("completed"), task.get("title")])

    # Write data to CSV file
    write_to_csv(user_id, username, user_tasks)
