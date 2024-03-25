#!/usr/bin/python3
"""export todo for all list_users"""
import json
import requests

if __name__ == "__main__":
    apiUrl = "https://jsonplaceholder.typicode.com/"
    list_users = requests.get(apiUrl + "list_users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            } for todo in requests.get(apiUrl + "todos",
                                       params={"userId": user.get("id")}).json()]
                                       for user in list_users}, jsonfile)
