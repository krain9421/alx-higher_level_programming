#!/usr/bin/python3
"""
Script that takes in a URL then sends a request to the URL
  while managine error codes
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    # Handling error codes
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
