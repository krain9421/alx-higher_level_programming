#!/bin/bash
# Script that takes in a URL, sends a GET request to that URL, and displays the body of the response
response=$(curl -s -w "%{http_code}" -o >(cat - >&2) $1); [ "$response" == "200" ] && curl -s $1
