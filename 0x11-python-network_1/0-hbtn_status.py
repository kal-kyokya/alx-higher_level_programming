#!/usr/bin//python3
"""
'0-hbtn_status_py' fetches a url using the 'urllib' package
"""
from urllib import request


if __name__ == "__main__":
    url = "http://kalkyokya.tech/"
    with request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(content.decode(encoding="utf-8")))
