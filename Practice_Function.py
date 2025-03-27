# Write a python function to find the maximum number.
def find_maximum_number(*args, **kwargs):
    all_numbers = list(args) + list(kwargs.values())

    if not all_numbers:
        return None

    max_number = all_numbers[0]

    for number in all_numbers:
        if number > max_number:
            max_number = number
    return max_number


print(find_maximum_number(-10, -12, -73, -41, -15)) 
print(find_maximum_number(a=-20, b=-30, c=-10)) 
print(find_maximum_number(5, 8, a=2, b=19, c=3))  
print(find_maximum_number()) 



#Write a python function to sum all the numbers in a list.
#sample List: (8,2,3,0,7)
#output: 20


def find_sum_of_numbers(*args):
    sum = 0
    for number in args:
        sum = sum + number

    return sum
print(find_sum_of_numbers(10,20,5))



# Write a python function to multiply all the numbers in a list.
#sample List: (8,2,3,7)
#output: 336

def find_multiplication_of_numbers(*args):
    mul = 1
    for number in args:
        mul = mul * number

    return mul

print(find_multiplication_of_numbers(8,2,3,7))


#Write a python program to reverse a string.

def reverse_a_string(num):
    return num[::-1]

print(reverse_a_string("aman"))


#Write a python function to calculate the factorial of a number(non-negative integer) The function accepts the number as an argument.

def find_factorial(number):
    if number <= 1:
        return number
    
    fac = 1
    while number >= 1:
        fac = fac * number
        number = number - 1

    return fac

print(find_factorial(5))


#Write a python function that accepts a string and counts the number of upper and lower case letters.

def count_upper_and_lower_case(sentence:str)->dict:

    counts = {"upper" : 0, "lower" : 0}

    for s in sentence:
        if s.isupper():
            counts["upper"] += 1
        elif s.islower():
            counts["lower"] += 1

    return counts


print(count_upper_and_lower_case("AMan"))


#Write a python function that takes a list and returns a new list with distinct elements from the first list .

def unique_elemnets(numbers):
    unique_numbers = set()

    for n in numbers:
        unique_numbers.add(n)

    return list(unique_numbers)

print(unique_elemnets([1,2,3,3,4,4,4,5,6,6,6,7]))



#Write a python function that checks whether a passed string is a palindrome or not .

def check_palindrome(userip):
    palindrome = userip[::-1]

    if palindrome != userip:
        print("Not a palindrome")
    else:
        print("palindrome")

print(check_palindrome("nitin"))



























