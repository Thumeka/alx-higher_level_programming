#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        bigger = my_list[0]
        for i in my_list:
            if i > bigger:
                bigger = i
        return bigger
    else:
        return None
