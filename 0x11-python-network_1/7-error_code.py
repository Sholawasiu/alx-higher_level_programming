#!/usr/bin/python3
# 7-error_code.py
"""
This python script takes in a URL, sends a request to the URL,
and displays the body of the response
"""
import sys
import requests


def main():
    """ Main function """
    res = requests.get(sys.argv[1])

    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)


if __name__ == '__main__':
    main()
