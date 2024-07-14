#!/usr/bin/python3
"""
'7-error_code' Reads a URL from the cmd line and
display the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    code = response.status_code
    if code >= 400:
        print("Error code:", code)
    else:
        content = response.text
        print(content)
