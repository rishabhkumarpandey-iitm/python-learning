'''
Loop Based String Processing

Strings are one of the most common data types processed using loops. In this exercise, you will write a multi-functional program that performs different operations on strings based on the task provided as the first input.

Each task demonstrates a different application of loops such as filtering, mapping, early termination using break, skipping iterations using continue, and formatted printing.

Problem Type - Standard Input - Standard Output

Implement the following tasks.
'''

task = input()

'''
1. Filtering
only_vowels

Read a string s and print only the vowels present in the string, one per line, while preserving their original order.

Assume vowels are:

a e i o u A E I O U

If the string contains no vowels, print nothing.

Input

    s : str

skip_digits

Read a string s and print every character except digits.

Each remaining character should be printed on a new line.

Input

    s : str
'''
'''
if task =='only_vowels':
    s = input()
    output = ''
    vowels = 'aeiou'
    for char in s:
        if char.lower() in vowels:
            output+=char 
    print(output)
'''


if task =='only_vowels':
    s = input()
    vowels = 'aeiou'
    output = ''.join(char for char in s if char.lower() in vowels)
    print(output)

elif task =='skip_digits':
    s = input()
    output = ''.join(char for char in s if char.isalpha()) 
    print(output)
    

'''
2. Mapping
swap_case_manual

Read a string s.

Without using Python's built-in swapcase() method, convert every lowercase letter to uppercase and every uppercase letter to lowercase.

Non-alphabetic characters should remain unchanged.

Print the converted string.

Input

    s : str
'''
if task == 'swap_case_manual':
    s = input()
    result = ''
    for i in s:
        if i.isalpha():
            if i.isupper():
                result+=i.lower()
            elif i.islower():
                result+=i.upper()
        else:
            result+=i
    print(result)


'''
char_position

Read a string s.

Print every character along with its position (starting from 1) in the following format:

1 : H
2 : e
3 : l
...

Input

    s : str
'''

if task =='char_position':
    s = input()
    result = []
    for i in range(len(s)):
        result.append(f'{i+1} : {s[i]}')
    output = '\n'.join(result)

    print(output)





    





