#!/usr/bin/python3
"""
'2-post_email' reads an email and a URL from the cmd line,
sends a POST request with the email abd return the body of the response.
"""
import sys
from urllib import request, parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'name': "The Dem", 'email': email}

    query_str = parse.urlencode(data)
    str_to_byte_q_str = query_str.encode("utf-8")
    print(query_str)
    print(str_to_byte_q_str)

    POST = request.Request(url, data=str_to_byte_q_str, method='POST')

    with request.urlopen(POST) as response:
        print(response.read())
