#!/usr/bin/python3
"""
'4-hbtn_status.py' Fetches a url using the 'requests' package.
"""
import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    content = response.text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
