#!/bin/bash
# Send a POST request with additional query parameters
curl -s -X POST -d "email=demtest@gmail.com&subject=I will always be here for PLD" "$1"
