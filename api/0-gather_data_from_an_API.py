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


def get_employee_data(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    # Get employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    todo_list = todo_response.json()

    return employee_data, todo_list


def display_todo_progress(employee_data, todo_list):
    employee_name = employee_data["name"]
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task["completed"])

    result = []
    result.append(
        f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):"
    )

    for idx, task in enumerate(todo_list, start=1):
        result.append(
            f"Task {idx} Formatting: {'OK' if task['completed'] else 'Incorrect'}"
        )

    return result


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_data, todo_list = get_employee_data(employee_id)
    output = display_todo_progress(employee_data, todo_list)

    for line in output:
        print(line)
