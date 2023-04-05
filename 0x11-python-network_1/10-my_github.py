#!/usr/bin/python3
"""
Script that uses the Github API to display a user's Github id.
"""

import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'
    auth = (user, passwd)
    # Getting the HTTP response
    response = requests.get(url, auth=(user, passwd))
    res_json = response.json()
    git_id = res_json.get('id')

    print(git_id)
