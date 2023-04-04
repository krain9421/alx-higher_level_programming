#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status using ``requests`` library
"""
import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
