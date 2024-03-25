#!/usr/bin/python3
"""todo"""
from json import dump
from requests import get
from sys import argv
if __name__ == "__main__":
    linkAPI = "https://jsonplaceholder.typicode.com"
    toDoApi = linkAPI + "/user/{}/todos".format(argv[1])
    nameApi = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    toDoResponse = get(toDoApi).json()
    nameUser = get(nameApi).json()
    results = []
    for todo in toDoResponse:
        tod = {}
        tod.update({"task": todo.get("title"), "completed": todo.get(
            "completed"), "username": nameUser.get("username")})
        results.append(tod)
    with open("{}.json".format(argv[1]), 'w') as f:
        dump({argv[1]: results}, f)
