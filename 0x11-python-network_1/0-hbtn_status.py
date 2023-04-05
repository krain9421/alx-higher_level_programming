#!/usr/bin/python3
""" Script that fetches the URL `https://intranet.hbtn.io/status """
import urllib.request as request


if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        content_utf = content.decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content_utf))
