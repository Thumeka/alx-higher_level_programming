#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newTee = []
    for i in range(list_length):
        divi = 0
        try:
            divi = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            newTee.append(divi)
    return newTee
