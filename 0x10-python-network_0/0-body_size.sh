#!/usr/bin/bash
# Use 'cURL' to get the content size of request
curl -sI $1 | sed -n 's/^Content-Length: //p'
