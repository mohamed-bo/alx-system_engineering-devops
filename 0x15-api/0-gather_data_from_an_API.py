#!/usr/bin/python3
"""return to-do list"""
from sys import argv
from requests import get
if __name__ == '__main__':
    linkAPI = "https://jsonplaceholder.typicode.com"
    toDoApi = linkAPI + "/user/{}/todos".format(argv[1])
    userApi = linkAPI + "/users/{}".format(argv[1])
    toDorespone = get(toDoApi).json()
    name = get(userApi).json()
    length = len(toDorespone)
    result = len([todo for todo in toDorespone
                  if todo.get("completed")])
    name = name.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, result, length))
    for todo in toDorespone:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
