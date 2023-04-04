#!/usr/bin/python3
"""
Script that takes a URL and sends a request to the URL
urllib.error.HTTPError exceptions will be managed
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    # Handling URLError
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read()

        print(content.decode('utf8'))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
