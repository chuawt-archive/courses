# Functions and Methods Homework

# %%
'''Write a function that computes the volume 
of a sphere given its radius.
'''
def vol(rad):
    return (4 / 3) * 3.14 * (rad ** 3) 

print(vol(2))


# %%
'''Write a function that checks whether a 
number is in a given range (inclusive of 
high and low).
'''
def ran_check(num, low, high):
    if low <= num <= high:
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'{num} is not in the range between {low} and {high}')

ran_check(5,2,7)
# %%
def ran_bool(num, low, high):
    return low <= num <= high

print(ran_bool(3,1,10))


# %%
'''Write a Python function that accepts a 
string and calculates the number of upper 
case letters and lower case letters.
'''
def up_low(s):
    n_lower = 0
    n_upper = 0
    for char in s:
        if char.isupper():
            n_upper += 1
        elif char.islower():
            n_lower += 1
    print(f'No. of Upper case characters : {n_upper}\nNo. of Lower case Characters : {n_lower}')

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# %%
'''Write a Python function that takes a 
list and returns a new list with unique 
elements of the first list.
'''
def unique_list(lst):
    return list(set(lst))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


# %%
'''Write a Python function to multiply 
all the numbers in a list.
'''
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print(multiply([1,2,3,-4]))


# %%
'''Write a Python function that checks 
whether a word or phrase is palindrome 
or not.
'''
def palindrome(s):
    s = s.replace(' ', '')
    mid_point = (len(s) + 1) //2
    first_half = s[:mid_point]
    second_half = s[mid_point:]
    rev_second_half = second_half[::-1]
    return first_half == rev_second_half

print(palindrome('helleh'))


# %%
## Hard

'''Write a Python function to check 
whether a string is pangram or not. 
(Assume the string passed in does not 
have any punctuation). 

Pangrams are words or sentences containing 
every letter of the alphabet at least once.
'''
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(' ', '').lower()
    unique_str1 = set(str1)
    return unique_str1 == set(alphabet)

print(ispangram("The quick brown fox jumps over the lazy dog"))