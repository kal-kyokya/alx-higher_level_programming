#!/bin/bash
# Display all HTTP method accepted by the server
curl -sI $1 | grep "Allow" | cut -d " " -f 2-
