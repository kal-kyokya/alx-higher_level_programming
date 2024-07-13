#!/usr/bin/python3
"""
'3-error_code' reads a URL from the cmd line, sends a request
and displays the body of the response.
"""
import sys
from urllib import request, error


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            content = response.read()
            html = content.decode('utf-8')
            print(html)
    except error.HTTPError as err:
        print("Error code:", err.code)
