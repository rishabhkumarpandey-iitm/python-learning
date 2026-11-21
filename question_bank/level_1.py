'''
Question 1 – Edge Character Extraction
Level 1 · Basic

Type: PYQ-inspired · 10 marks · Function-based · No loops

Problem statement

Write a function extract_edges(s) that accepts a string s and returns a new string containing:
- The first two characters of s.
- A hyphen (-).
- The last two characters of s.
However, if the string contains fewer than four characters, return the original string unchanged.

Input format

Implement the following function:
def extract_edges(s):    # Your code



The function receives one string argument. You do not need to use input() or print().

Output format

Return the resulting string.

Constraints
- s contains only ordinary English letters.
- The string may contain fewer than four characters.
- The string may also contain exactly four characters.
Sample test cases
SAMPLE 1

Input
extract_edges("PROGRAMMING")



Expected output
PR-NG



SAMPLE 2

Input
extract_edges("cat")



Expected output
cat



SAMPLE 3

Input
extract_edges("ABCD")



Expected output
AB-CD



What this question tests
- String indexing.
- String slicing.
- len().
- Conditional statements.
- Function implementation.
- Handling short strings correctly.

Your task: Write the Python function independently and submit your code.
'''
task = input('enter your task:')

if task =='extract_edges':
    def extract_edges(s):
        if len(s)>=4:
            return s[:2]+'-'+s[-2:]
        else:
            return s

'''
Question 2 – Circular Index Extraction
Level 2 · Intermediate
 PYQ-inspired · 10 marks · Function-based · No loops

Write a function circular_extract(s, k) that:
1. Accepts a string s and a non-negative integer k.
2. Treats the string as circular.
3. Returns the character at index k, considering circular indexing.
For example, if the string is "PYTHON":
- Index 0 → P
- Index 5 → N
- Index 6 → P
- Index 7 → Y
Input format
def circular_extract(s, k):    # Your code



Sample cases
Function call	Expected output
circular_extract("PYTHON", 2)	'T'
circular_extract("PYTHON", 6)	'P'
circular_extract("CODE", 7)	'E'
circular_extract("ABC", 0)	'A'

Constraints:
- s is non-empty.
- k >= 0.
What this tests: String indexing, len(), arithmetic operators and boundary handling.

Submit your function only. I will evaluate it before revealing the next question.
'''
if task =='Circular Index Extraction':
    def circular_extract(s:str,k:int) :
        return s[k%len(s)]
    s = 'python'
    k = 5
    print(circular_extract(s,k))

'''
Q3. Extract Middle Characters
Write a function middle_chars(s) that accepts a string s and returns its middle character(s).

Rules:
- If the string has an odd length, return the single middle character.
- If the string has an even length, return the two middle characters.
Sample test cases
Input s	Expected output
"PYTHON"	"TH"
"CODE"	"OD"
"HELLO"	"L"
"AB"	"AB"
"A"	"A"

Your task
Write only this function:
def middle_chars(s):    # Your code



You may test it using print() statements separately.
'''
def middle_chars(s:str):
    n = len(s)
    mid = n//2
    if n%2!=0:
        return s[mid]
    else:
        return s[(mid-1):(mid+1)]

'''
Q4. Remove First and Last Occurrence
Level 2 · 10 marks
 Function-based
 No loops


Problem statement

Write a function remove_ends(s) that accepts a string s and returns a new string after removing its first and last characters.

Rules:
- If the string has 2 or more characters, remove the first and last characters.
- If the string has fewer than 2 characters, return an empty string.
Sample test cases
Input	Expected output
"PROGRAMMING"	"ROGRAMMIN"
"PYTHON"	"YTHO"
"AB"	""
"A"	""
"HELLO"	"ELL"

Your task
Write the function:
def remove_ends(s):    # Your code
'''
if task == 'remove_ends':
    def remove_ends(s:str):
        return s[1:-1]
    print(remove_ends('programming'))


'''
Q5. Swap First and Last Characters
Level 2 · 10 marks
 Function-based
 No loops


Problem statement

Write a function swap_ends(s) that accepts a string and returns a new string by swapping its first and last characters.

Rules:
- If the string has 2 or more characters, swap the first and last characters.
- If the string has fewer than 2 characters, return it unchanged.
Sample test cases
Input	Expected output
"PYTHON"	"NYTHOP"
"HELLO"	"OELLH"
"AB"	"BA"
"A"	"A"
"DATA"	"AATD"

Your task
Write:
def swap_ends(s):    # Your code



Important: Try to solve this using string slicing and concatenation. No loops.
'''
if task =='swap_ends':
    def swap_ends(s:str):
        if len(s)<2:
            return s
        else:
            return s[-1]+s[1:-1]+s[0]

    p = input()
    print(swap_ends(p))





'''
Q6. Replace Vowels with *
Level 2 · 10 marks
 Function-based
 No loops


Problem statement

Write a function replace_vowels(s) that accepts a string s and returns a new string in which every vowel is replaced with *.

Vowels: a, e, i, o, u (both uppercase and lowercase).
Sample test cases
Input	Expected output
"Hello World"	"H*ll* W*rld"
"PYTHON"	"PYTH*N"
"education"	"*d*c*t**n"
"AEIOU"	"*****"
"rhythm"	"rhythm"

Your task
Write the function:
def replace_vowels(s):    # Your code
'''
if task =='replace_vowels':
    def replace_vowels(s:str):
        result =''.join('#' if i.lower() in 'aeiou' else i for i in s)
        return result
    s = input()
    print(replace_vowels(s))


'''
Remove Duplicate Characters

Write remove_duplicates(s) preserving the first occurrence of each character.

Examples:
- "banana" → "ban"
- "HELLO" → "HELO"
- "programming" → "progamin"
No explicit loops. Try solving it independently.

Paste your code when ready.
'''

if task =='remove_duplicates':
    def remove_duplicates(s:str):
        return set(s)


'''
Q9. Count Vowels and Consonants
Level 2 · 10 marks
 Function-based
 Loops


Problem statement

Write a function count_vowels_consonants(s) that accepts a string and returns a dictionary containing:
- Number of vowels.
- Number of consonants.
Ignore spaces, digits and special characters.

Treat uppercase and lowercase letters equally.
Sample test cases
Input	Expected output
"Hello World"	{'vowels': 3, 'consonants': 7}
"PYTHON"	{'vowels': 1, 'consonants': 5}
"AEIOU"	{'vowels': 5, 'consonants': 0}
"123 !"	{'vowels': 0, 'consonants': 0}

Your task
def count_vowels_consonants(s):    # Your code


'''
if task == 'count_v_c':
    s = input()
    v=0
    c=0
    output = {}
    for i in s:
        if i.isalpha():
            if i.lower() in 'aeiou':
                v+=1
            else:
                c+=1

    #         output['vowels'] = v 
    #         output['consonants'] =c
    # print(output) 
    print({'vowels': v, 'consonants': c})

    '''
    Q10. Count Positive, Negative and Zero
Level 2 · 10 marks
 Function-based
 Loops


Write a function count_numbers(nums) that accepts a list of integers and returns a dictionary containing the count of:
- Positive numbers
- Negative numbers
- Zeros
Examples
Input	Expected output
[1, -2, 0, 3, -4, 0]	{'positive': 2, 'negative': 2, 'zero': 2}
[1, 2, 3]	{'positive': 3, 'negative': 0, 'zero': 0}
[-1, -5]	{'positive': 0, 'negative': 2, 'zero': 0}
[]	{'positive': 0, 'negative': 0, 'zero': 0}

Your task
def count_numbers(nums):
    # Your code



Use a for loop and conditional statements.
    '''

if task =='count_numbers':
    def count_numbers(nums:list):
        p=0
        n=0
        z=0
        for i in nums:
            if i>0:
                p+=1
            elif i<0:
                n+=1
            else:
                z+=1
        return {'positive': p, 'negative': n, 'zeros': z}


'''
Q11. Even–Odd Sum
Write a function even_odd_sum(nums) that accepts a list of integers and returns a dictionary containing:
- even: Sum of all even numbers.
- odd: Sum of all odd numbers.
Examples:
even_odd_sum([1, 2, 3, 4, 5, 6])# {'even': 12, 'odd': 9}even_odd_sum([2, 4, 6])# {'even': 12, 'odd': 0}even_odd_sum([])# {'even': 0, 'odd': 0}
'''
if task == 'function even_odd_sum':
    def even_odd_sum(nums:list):
        return {'even': sum([i for i in nums if i%2==0]), 'odd': sum([i for i in nums if i%2!=0])}
    print(even_odd_sum([1, 2, 3, 4, 5, 6]))

'''
Next: Q12 – Filter Positive Numbers

Write a function positive_numbers(nums) that returns a new list containing only positive numbers, preserving their original order.

Example:
positive_numbers([-2, 5, 0, 8, -1, 3])# [5, 8, 3]



Try it yourself!
'''

if task == 'Filter Positive Numbers':
    def positive_numbers(nums:list):
        output = [i for i in nums if i>0]
        return output 
    

'''
Q13 – Square Every Number
Write a function square_numbers(nums) that returns a new list containing the square of every number.

Example:
square_numbers([2, 3, 4, 5])# [4, 9, 16, 25]

'''

if task == 'Square Every Number':
    def square_numbers(nums:list):
        output = list(map(lambda i:i**2,nums))
        return output 
    nums = [2,8,10,15]
    print(square_numbers(nums))

'''
Q14 – Filter and Transform Together
Now let's increase the difficulty.

Write a function double_positive(nums) that:
1. Selects only positive numbers.
2. Doubles each selected number.
3. Returns the resulting list.
Example:
double_positive([-2, 3, 0, 5, -7, 4])# [6, 10, 8]

'''
if task =='Double Positive':
    def double_positive(nums:list):
        output = list(map(lambda x:x*2,[x for x in nums if x>0]))
        return output 
    print(double_positive([-2, 3, 0, 5, -7, 4]))