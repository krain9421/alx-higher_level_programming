#!/usr/bin/python3
""" Script that fetches the URL `https://intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://intranet.hbtn.io/status")
    req2 = urllib.request.Request("http://0.0.0.0:5050/status")

    # Handling URLError
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read()
            content_type = type(content)
            content_utf = content.decode("utf8")

        print("Body response:")
        print("\t- type: {}".format(content_type))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content_utf))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
