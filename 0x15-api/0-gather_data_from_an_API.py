#!/usr/bin/python3
"""return to-do list"""
import requests
import sys
if __name__ == "__main__":
    linkApi = "https://jsonplaceholder.typicode.com/"
    user = requests.get(linkApi + "users/{}".format(sys.argv[1])).json()
    response = requests.get(linkApi + "response", params={"userId": sys.argv[1]}).json()
    result = [t.get('title') for t in response if t.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(result), len(response)))
    [print("\t {}".format(c)) for c in result]
