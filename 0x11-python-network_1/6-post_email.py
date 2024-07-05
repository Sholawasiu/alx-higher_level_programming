#!/usr/bin/python3
# 6-post_email.py
"""
This python script takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays the
body of the response
"""
import sys
import requests


def main():
    """ Main function """
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    res = requests.post(url, data=email)
    print(res.text)


if __name__ == '__main__':
    main()
