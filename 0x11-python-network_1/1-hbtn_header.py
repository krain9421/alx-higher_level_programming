#!/usr/bin/python3
""" Script that displays the X-Request-Id variable in a URL response """
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.info()

    print(header.get('X-Request-Id', 'Key not found'))
