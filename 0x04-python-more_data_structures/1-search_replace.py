#!/usr/bin/python3
# 1-search_replace.py

def search_replace(my_list, search, replace):
    update_list = my_list[:]
    for elem in range(len(update_list)):
        if update_list[elem] == search:
            update_list[elem] = replace
    return (update_list)
