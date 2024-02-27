# Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

# NB: The endpoint for access specific TODO items for an employee with ID = 1 will be https://jsonplaceholder.typicode.com/users/1/todos and the endpoint to get specific employee details will be https://jsonplaceholder.typicode.com/users/1

# Requirements:

# You must use urllib or requests module
# The script must accept an integer as a parameter, which is the employee ID
# The script must display on the standard output the employee TODO list progress in this exact format:
# First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
# where:
# EMPLOYEE_NAME: name of the employee
# NUMBER_OF_DONE_TASKS: number of completed tasks
# TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
# Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

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


def display_user_progress(user_data, tasks):
    print("Employee {} is done with tasks".format(user_data.get("name")), end="")

    completed_tasks = [task for task in tasks if task.get("completed")]

    print("({}/{}):".format(len(completed_tasks), len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])

    user_data = get_user_data(user_id)
    user_tasks = get_user_tasks(user_id)

    display_user_progress(user_data, user_tasks)
