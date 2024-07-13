#!/usr/bin/python3
# Fetch a url using the 'urllib' package
import urllib.request as req


if __name__ == "__main__":
    url = "http://kalkyokya.tech/"
    with req.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(content.decode(encoding="utf-8")))
