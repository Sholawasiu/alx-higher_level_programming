#!/usr/bin/python3
# 3-error_code.py
"""
This python script takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8)
"""
import sys
from urllib import request, error


def main():
    """ Main function """
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.status))


if __name__ == '__main__':
    main()
