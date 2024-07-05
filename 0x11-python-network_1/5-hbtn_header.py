#!/usr/bin/python3
# 5-hbtn_header.py
"""
This python script takes in a URL, send a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests


def main():
    """ Main function """
    res = requests.get(sys.argv[1])
    print(res.headers.get("X-Request-Id"))


if __name__ == '__main__':
    main()
