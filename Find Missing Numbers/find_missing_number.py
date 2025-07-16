# Given an array containing a range of numbers from 0 to n with a missing number, find the missing number in the input array.

def find_missing_num(n):
    numbers = set(n)
    # length = len(n)
    output = []
    for i in range (1, max(n)):
        if i not in numbers:
            output.append (i)
    return output

try:
    list_of_numbers = input("input the list of numbers here : ")
    num_list = [int(x) for x in list_of_numbers.split(",")]
    print("Here is the list of the missing numbers list :", find_missing_num(num_list))
except Exception as e:
    print (e)