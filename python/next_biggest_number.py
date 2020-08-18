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


def find_second_largest(number, num_list):
    """find second largest number in num_list based on number"""
    sorted_num_list = sorted(num_list)
    for i in sorted_num_list:
        if i > number:
            return i


def next_biggest_number(num):
    #TODO: Implement me!
    # case 1 - single digit input cannot be rearranged
    # case 2 - input is in descending order cannot be rearranged to fit requirement
    if is_descending(num) or len(str(num)) < 2:
        return -1
    
    # case 3 - input that is in asc order simply needs the last two digets swapped
    elif is_ascending(num):
        num_list = num_to_list(num)
        result = swap(num_list, len(num_list)-2, len(num_list)-1)
        result = list_to_num(result)
        return result


def main():
    result = next_biggest_number(sys.argv[1])
    print(result)


if __name__ == "__main__":
    main()



