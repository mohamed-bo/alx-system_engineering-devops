#!/usr/bin/python3
"""export to do liost"""
from csv import DictWriter, QUOTE_ALL
from requests import get
from sys import argv
if __name__ == "__main__":
    linkAPI = "https://jsonplaceholder.typicode.com"
    toDoApi = linkAPI + "/user/{}/todos".format(argv[1])
    userName = linkAPI + "/users/{}".format(argv[1])
    user = get(userName).json()
    response = get(toDoApi).json()
    toDoArray = []
    for todo in response:
        result = {}
        result.update({"user_ID": argv[1], "username": user.get(
                       "username"), "completed": todo.get("completed"),
                       "task": todo.get("title")})
        toDoArray.append(result)
    with open("{}.csv".format(argv[1]), 'w', newline='') as f:
        header = ["user_ID", "username", "completed", "task"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writerows(toDoArray)
