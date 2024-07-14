#!/usr/bin/python3
"""
'6-post_email' Reads a URL and an email from the cmd line and
POST them using the 'requests' package.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    query_str = {'email': email}
    response = requests.post(url, data=query_str)
    content = response.text
    print(content)
