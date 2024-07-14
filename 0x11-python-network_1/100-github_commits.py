#!/usr/bin/python3
"""
'100-github_commits' Returns the 10 most recent GitHub repo commits.
"""
from requests.auth import HTTPBasicAuth as HBA
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    rest_api = "https://api.github.com/repos/{}/{}/commits".format(
        owner, repo)

    response = requests.get(rest_api)
    commits = response.json()

    try:
        for i in range(10):
            sha = commits[i].get('sha')
            author = commits[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
    except IndexError:
        pass
