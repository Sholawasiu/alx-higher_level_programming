#!/usr/bin/python3
# 4-hbtn_status.py
"""
This python script fetches https://alx-intranet.hbtn.io/status
"""
import requests


def main():
    """ Main function """
    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))


if __name__ == '__main__':
    main()
