#!/bin/bash
# Send a POST request with additional query parameters
curl -s -X POST -d "email=demtest@gmail.com&subject=Dem will always be here for DAMSKAL" "$1"
