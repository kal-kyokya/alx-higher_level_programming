#!/usr/bin/python3
"""
'5-hbtn_header' Reads a URL from the cmd line and
fetches a particular header associated with it.
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    headers = response.headers
    print(headers['X-Request-Id'])
