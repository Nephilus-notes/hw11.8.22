# Exercise 1
# Given a list as a parameter,write a function that returns a list of numbers that are less than ten


# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]

def below_ten(a_list):
    less_than_ten = []
    for num in a_list:
        if num < 10:
            less_than_ten.append(num)
        else:
            continue
    return less_than_ten

print(below_ten(l_1))

def below(a_list):
    return [num for num in a_list if num < 10]

print(below(l_1))
            

# Exercise 2
# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merge_sort(list1, list2):
    return sorted(list1 + list2)

merge_sort(l_1, l_2)