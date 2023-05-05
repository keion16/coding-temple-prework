question 1
Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    """greet user with simple greeting."""
    print("Hello, " + user_name.title() + ".")
    hello_name('keion')

question 2
Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_0dds():
    for value in range(1,100,2):
        print(value)

question 3
Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    """Retun max number in list."""
def max_num_in_list(a_list):
    value = a_list[0]
    for item in a_list:
        if item > value:
            value = item
    return value
a_list = [4,33,174,67]
print(max_num_in_list(a_list))

question 4 
Write a function to return if the given year is a leap year. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    leap = False
    if (year % 4 == 0) and (year % 100 != 0):
        leap = True
    elif (year % 100 == 0) and (year % 400 != 0):
        leap = False
    else:
        leap = False
    return leap

question 5
Write a function to check to see if all numbers in list are consecutive numbers. 

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min()), max(1)+1)
a_list = [2,4,6,8,10]
print(is_consecutive(a_list))




    



    
