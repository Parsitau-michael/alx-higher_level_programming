#!/usr/bin/bash

# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response

URL=$1

curl -s -w '%{size_download}\n' "$URL" -o /dev/null
