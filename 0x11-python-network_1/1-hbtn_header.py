#!/usr/bin/python3
"""
'1-hbtn_header' manipulate a cmd line URL and return one of its headers.
"""
from urllib import request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
