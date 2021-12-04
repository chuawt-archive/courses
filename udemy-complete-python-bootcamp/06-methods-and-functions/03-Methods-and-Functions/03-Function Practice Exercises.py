# Function Practice Exercises

## Warmup Section

### Lesser of Two Evens
'''Write a function that returns the lesser of 
two given numbers if both numbers are even, 
but returns the greater if one or both numbers are odd.'''
# %%
def lesser_of_two_evens(a, b):
    if a%2==0 and b%2==0:
        return min(a, b)
    else:
        return max(a, b)
# %%
assert lesser_of_two_evens(2, 4) == 2
assert lesser_of_two_evens(2, 5) == 5


# %%
### Animal Crackers
'''Write a function takes a two-word string and 
returns True if both words begin with same letter.
'''
# %%
def animal_crackers(text):
    a, b = text.split()
    return a[0] == b[0]
# %%
assert animal_crackers('Levelheaded Llama') == True
assert animal_crackers('Crazy Kangaroo') == False


# %%
### Makes Twenty
'''Given two integers, return True if the sum 
of the integers is 20 or if one of the integers 
is 20. If not, return False.
'''
# %%
def makes_twenty(n1, n2):
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20
# %%
assert makes_twenty(20, 10) == True
assert makes_twenty(12, 8) == True
assert makes_twenty(2, 3) == False


# %%
## Level 1 Problems

### Old MacDonald
'''Write a function that capitalizes the
 first and fourth letters of a name.
'''
# %%
def old_macdonald(name):
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:]
# %%
assert old_macdonald('macdonald') == 'MacDonald'


# %%
### Master Yoda
'''Given a sentence, return a sentence
 with the words reversed.
'''
# %%
def master_yoda(text):
    list_of_words = text.split()
    return ' '.join(list_of_words[::-1])
# %%
assert master_yoda('I am home') == 'home am I'
assert master_yoda('We are ready') == 'ready are We'


# %%
### Almost There
'''Given an integer n, return True if 
n is within 10 of either 100 or 200.
'''
# %%
def almost_there(n):
    return (90 < n < 110) or (190 < n < 210) 
# %%
assert almost_there(104) == True
assert almost_there(150) == False
assert almost_there(209) == True


# %%
## Level 2 Problems

### Find 33
'''Given a list of ints, return True if the 
array contains a 3 next to a 3 somewhere.
'''

# %%
def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i-1] == 3 and nums[i] == 3:
            return True
    return False
# %%
assert has_33([1, 3, 3]) == True
assert has_33([1, 3, 1, 3]) == False
assert has_33([3, 1, 3]) == False


# %%
### Paper Doll
'''Given a string, return a string where 
for every character in the original there 
are three characters.
'''
# %%
def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result
# %%
assert paper_doll('Hello') == 'HHHeeellllllooo'
assert paper_doll('Mississippi') == 'MMMiiissssssiiissssssiiippppppiii'


# %%
### Blackjack
'''Given three integers between 1 and 11, 
if their sum is less than or equal to 21, 
return their sum. If their sum exceeds 21 
and there's an eleven, reduce the total sum 
by 10. Finally, if the sum (even after 
adjustment) exceeds 21, return 'BUST'.
'''
# %%
def blackjack(a, b, c):
    total = a + b + c
    if total <= 21:
        return total
    elif a == 11 or b == 11 or c == 11:
        return total - 10
    else:
        return 'BUST'
# %%
assert blackjack(5,6,7) == 18 
assert blackjack(9,9,9) == 'BUST'
assert blackjack(9,9,11) == 19


# %%
### Summer of '69
'''Return the sum of the numbers in the 
array, except ignore sections of numbers 
starting with a 6 and extending to the next 9 
(every 6 will be followed by at least one 9). 
Return 0 for no numbers.
'''
# %%
def summer_69(arr):
    continue_add = True
    total = 0
    for num in arr:
        if num == 6:
            continue_add = False
        elif num == 9:
            continue_add = True
        elif continue_add:
            total += num
    return total
# %%
assert summer_69([1, 3, 5]) == 9
assert summer_69([4, 5, 6, 7, 8, 9]) == 9
assert summer_69([2, 1, 6, 9, 11]) == 14


# %%
## Challenging Problems

### Spy Game
'''Write a function that takes in a list of 
integers and returns True if it contains 007 
in order.
'''
# %% 
def spy_game(nums):
    num_list = [0, 0, 7]
    for num in nums:
        if num == num_list[0]:
            num_list.pop(0)
            if len(num_list) == 0:
                return True
    return False
# %%
assert spy_game([1,2,4,0,0,7,5]) == True
assert spy_game([1,0,2,4,0,5,7]) == True
assert spy_game([1,7,2,0,4,5,0]) == False


# %%
### Count Primes
'''Write a function that returns the number
 of prime numbers that exist up to and 
 including a given number.
'''
# %% 
def is_prime(num):
    for k in range(2, int(num**0.5) + 1):
        if num % k == 0:
            return False
    return True

def count_primes(num):
    n_primes = 0
    for n in range(2, num + 1):
        if is_prime(n):
            n_primes += 1
    return n_primes
# %%
assert count_primes(100) == 25                    
assert count_primes(0) == 0
assert count_primes(1) == 0
assert count_primes(2) == 1

# %%
## Just for Fun

### Print Big
'''Write a function that takes in a single
 letter, and returns a 5x5 representation 
 of that letter.
'''
# %%
def print_big(letter):
    letter_dict = {
        'a': '  *  \n * * \n*****\n*   *\n*   *',
        'b': '**** \n*   *\n**** \n*   *\n**** ',
        'c': '*****\n*    \n*    \n*    \n*****',
        'd': '***  \n*  * \n*   *\n*  * \n***  ',
        'e': '*****\n*    \n*****\n*    \n*****',
    }
    return letter_dict[letter]