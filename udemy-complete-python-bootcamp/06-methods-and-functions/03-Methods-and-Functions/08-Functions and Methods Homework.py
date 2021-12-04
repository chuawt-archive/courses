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
