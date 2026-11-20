'''
Question 1. character_code
Read a string s.

Print each character followed by its ASCII value in the format:
H : 72
e : 101
l : 108
l : 108
o : 111


Concepts: for loop, ord(), string iteration.

'''
task = input()

'''
result = []
if task =='charecter_code':
    s = input()
    for i in s:
        result.append(f'{i} : {ord(i)}')
    output = '\n'.join(result)
    print(output)
'''
if task =='charecter_code':
    s = input()
    result = [f'{i} : {ord(i)}' for i in s]
    output = '\n'.join(result)
    print(output)

'''
Question 2. replace_vowels
Read a string s.

Replace every vowel (a, e, i, o, u), irrespective of case, with *.

Keep all other characters unchanged.

Example:
Input:  Hello World
Output: H*ll* W*rld


Concepts: lower(), conditions, string mapping.
'''

'''
if task =='replace_vowels':
    s = input()
    vowels = 'aeiou'
    result = ''
    for char in s:
        if char.isalpha():
            if char in vowels:
                result+='#'
            else:
                result+=char
        else:
            result+=char
        print(result) 
'''
'''
if task == 'replace_vowels':
    s = input()
    vowels = 'aeiou'
    result = list('#' if char in vowels else char for char in s)
    print(''.join(result))
'''
if task == 'replace_vowels':
    s = input()
    vowels = 'aeiou'
    result = ''.join('#' if char.lower() in vowels else char for char in s)
    print(result)



