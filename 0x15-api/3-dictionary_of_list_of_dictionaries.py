#!/usr/bin/python3
"""export to do of all users"""

from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    linkApi = "https://jsonplaceholder.typicode.com"
    userApi = "https://jsonplaceholder.typicode.com/users"
    userLIst = get(userApi).json()
    res = {}
    for user in userLIst:
        listOfTodo = []
        toDoApi = linkApi + "/user/{}/todos".format(user.get("id"))
        name_url = "https://jsonplaceholder.typicode.com/users/{}".format(
            user.get("id"))
        toDoResponse = get(toDoApi).json()
        nameResponse = get(name_url).json()
        for todo in toDoResponse:
            todo_dict = {}
            todo_dict.update({"username": nameResponse.get("username"),
                              "task": todo.get("title"),
                              "completed": todo.get("completed")})
            listOfTodo.append(todo_dict)
        res.update({user.get("id"): listOfTodo})
    with open("todo_all_employees.json", 'w') as f:
        dump(res, f)
