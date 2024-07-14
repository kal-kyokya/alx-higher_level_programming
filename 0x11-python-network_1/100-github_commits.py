#!/usr/bin/python3
"""
'100-github_commits' Returns the 10 most recent GitHub repo commits.
"""
from requests.auth import HTTPBasicAuth as HBA
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[1]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10"
    rest_api = url

    response = requests.get(rest_api)
    json_content = response.json()

    for commit in json_content:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
