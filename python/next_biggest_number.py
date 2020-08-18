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


def is_ascending(number):
    """return true if digits are arranged in ascending order"""
    num_list = num_to_list(number)
    for i in range(len(num_list)-1):
        if num_list[i] > num_list[i+1]:
            return False
    return True


def is_descending(number):
    """return true if digits are arranged in descending order"""
    num_list = num_to_list(number)
    for i in range(len(num_list)-1):
        if num_list[i] < num_list[i+1]:
            return False
    return True


def swap(num_list, index_a, index_b):
    """swap two numbers in a list based on index"""
    num_to_swap_a = num_list[index_a]
    num_to_swap_b = num_list[index_b]
    num_list[index_a] = num_to_swap_b
    num_list[index_b] = num_to_swap_a
    return num_list

    
def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    #TODO: Implement me!
    return 0

if __name__ == "__main__":
    main()



