'''
Level 1: Basic character replacement
Q1 · Easy
replace_digits
Read a string s.

Replace every digit (0–9) with #.

Keep all other characters unchanged.

Example:
Input:
Hello123 World45!

Output:
Hello### World##!


Concepts: isdigit(), conditions, string mapping.
'''
task = input('Enter Your Task:')

if task =='replace_digits':
    s = input()
    result = ''.join('#' if i.isdigit() else i for i in s)
    print(result)

'''
Q2 · Easy
replace_spaces
Read a string s.

Replace every space with an underscore _.

Keep all other characters unchanged.

Example:
Input:
I love Python programming

Output:
I_love_Python_programming


Concepts: Character comparison, conditions.
'''
if task =='replace_spaces':
    s = input().split()
    result = '-'.join(i for i in s)
    print(result)


'''
Level 2: Character transformation
Q3 · Intermediate
uppercase_vowels
Read a string s.

Convert all lowercase vowels into uppercase.

Keep consonants, uppercase letters, numbers and special characters unchanged.

Example:
Input:
Hello World 123

Output:
HEllO WOrld 123


Concepts: lower(), upper(), membership operator.
'''
if task =='charecter_transformation':
    s = input()
    vowels = 'aeiou'
    result= ''.join(i.upper() if i.lower() in vowels else i for i in s)
    print(result)


'''
Level 3: Slightly challenging
Q5 · Intermediate+
toggle_vowels
Read a string s.
- Convert lowercase vowels into uppercase.
- Convert uppercase vowels into lowercase.
- Keep everything else unchanged.
Example:
Input:
Hello EDUCATION!

Output:
HEllO edUcAtIOn!


Concepts: Multiple conditions, character mapping.
'''
if task == 'toggle_vowels':
    s = input()
    vowels = 'aeiou'
    result = ''
    for ch in s:
        if ch.lower() in vowels:
            if ch.isupper():
                result+=ch.lower()
            else:
                result+=ch.upper()
        else:
            result+=ch 
    print(result)

'''
alternate_replacement
Read a string s.

Replace characters at even indices (0, 2, 4, ...) with *.

Keep characters at odd indices unchanged.

Example:
Input:
Python

Output:
* y * h * n


The actual output should not contain extra spaces:
*y*h*n


Concepts: range(), indexing, mapping.
'''

if task =='alternate_replacement':
    s = input()
    n = len(s)
    result = ''.join('*' if ch%2==0 else s[ch] for ch in range(n))
    print(result)

'''
Level 4: IITM-style challenge
Q7 · Challenge
character_mapping
Read a string s.

Apply the following rules:
1. Lowercase letters → uppercase.
2. Uppercase letters → lowercase.
3. Digits → @.
4. Spaces → _.
5. All other special characters remain unchanged.
Example:
Hello World 123!

Output:
hELLO_wORLD_@@@!
'''
if task == 'character_mapping':
    s = input()
    result = ''
    for i in s:
        if i.islower():
            result+=i.upper()
        elif i.isupper():
            result+= i.lower()
        elif i==' ':
            result+='_'
        elif i.isdigit():
            result+='@'
        else:
            result+=i
    print(result)
        
            

            