"""
Write a function called "show_excitement" where the string "I am super excited for this course!" is returned exactly 5 times, where each sentence is separated by a single space.

Return the string with "return".
You can only have the string once in your code.
Don't just copy/paste it 5 times into a single variable!
"""

#python3
def show_excitement():
    result = ''
    TEXT = 'I am super excited for this course!'
    for _ in range(5):
        result = result + ' ' + TEXT   
    return result.strip() #remove the first whitespace

print(show_excitement())