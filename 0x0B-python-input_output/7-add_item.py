#!/usr/bin/python3

"""
Adds all arguments to a Python list, and then save them to a file.
    - use your function save_to_json_file from 5-save_to_json_file.py
    - use your function load_from_json_file from 6-load_from_json_file.py
    - The list must be saved as a JSON representation in the file add_item.json
"""
import sys


if __name__ == "__main__":
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save(items, "add_item.json")
