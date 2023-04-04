#!/usr/bin/python3
""" Script that fetches the URL `https://intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    # req = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        content = response.read()
        content_type = type(content)
        content_utf = content.decode("UTF-8")

        print("Body response:")
        print("\t- type: {}".format(content_type))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content_utf))
