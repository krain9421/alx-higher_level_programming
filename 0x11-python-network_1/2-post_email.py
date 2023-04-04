#!/usr/bin/python3
"""
Script that takes in a URL and email, then sends a POST request to the URL
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode()
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        value = response.read().decode('utf8')

    print(value)
