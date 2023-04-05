#!/usr/bin/python3
"""
Script that takes in a URL and email address, and sends a POST request
  to the passed URL with the email as parameter
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    response = requests.post(url, email)
    print(response.text)
