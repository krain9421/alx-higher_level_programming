#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and then displays
  the value of the variable X-Request-Id
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
