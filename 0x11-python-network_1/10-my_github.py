#!/usr/bin/python3
"""
'10-my_github' Uses 'Basic Authentication' to access a GitHub account
through the 'requests' module's class 'HTTPBasicAuth'.
"""
from requests.auth import HTTPBasicAuth as HBA
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    rest_api = "https://api.github.com/user"

    response = requests.get(rest_api, auth=HBA(username, password))
    content = response.json()
    print(content.get('id'))
