#!/usr/bin/python3
# 10-my_github.py
"""
This python script takes my GitHub credentials (username and password)
and uses the GitHub API to display my id
"""
import sys
import requests


def main():
    """ Main function """
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    json = response.json()

    print(json.get('id'))


if __name__ == '__main__':
    main()
