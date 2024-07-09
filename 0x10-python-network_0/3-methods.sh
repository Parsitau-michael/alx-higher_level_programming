#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -X -I OPTIONS "$1" | grep "Allow:" | tr -d '\r'
