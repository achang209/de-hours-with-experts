#!/usr/bin/python3
import sys

def num_to_list(number):
    """function to help convert a multi-digit interger to a list of single digit intergers"""
    result = []
    for i in str(number):
        result.append(int(i))
    return result

def list_to_num(num_list):
    """function to help convert a list of single digit integers to a single multi-digit integer"""
    num_list = [str(i) for i in num_list]
    num_str = "".join(num_list)
    result = int(num_str)
    return result

def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    #TODO: Implement me!
    return 0

if __name__ == "__main__":
    main()



