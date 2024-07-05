#!/usr/bin/python3
# 8-json_api.py
"""
This python script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests


def main():
    """ Main function """
    letter = '' if len(sys.argv) == 1 else sys.argv[1]
    arg = {"q": letter}
    res = requests.post("http://0.0.0.0:5000/search_user", data=arg)

    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")


if __name__ == '__main__':
    main()
