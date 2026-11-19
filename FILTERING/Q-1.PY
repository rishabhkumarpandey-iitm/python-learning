'''
Q1. Only Even Numbers
Take a list of integers as input and create a new list containing only even numbers.

Input:
1 2 3 4 5 6 7 8


Expected output:
[2, 4, 6, 8]
'''

task = input()

if task == 'only_evens':
    int_list = list(map(int, input().split()))
    output = [x for x in int_list if x%2==0]
    print(output)

'''
Q2. Only Vowels
Take a string as input and print only the vowels. Preserve their original case.

Input:
PyThOn Programming


Expected output:
O o a i
'''
if task == 'only_vowels':
    s = input()
    output = ''.join(char for char in s if char.lower() in 'aeiou')
    print(output)



'''
Q3. Filter Positive Numbers
Given a list of integers, create a new list containing only positive numbers. Exclude zero.

Input:
-5 10 0 -2 8 15 -9


Expected output:
[10, 8, 15]
'''

if task == 'only_positive':
    l = list(map(int, input().split()))
    output = [n for n in l if n>0]
    print(output)


'''
Q4. Filter Words by Length
Given a sentence, print only those words whose length is greater than 4.

Input:
Python is an amazing programming language


Expected output:
['Python', 'amazing', 'programming', 'language']
'''
if task =='words of more than 4':
    s = input()
    output = [word for word in s.split() if len(word)>4]
    print(output)


'''
Q5. Filter Numbers Divisible by 3 and 5
Given a list of integers, create a new list containing numbers divisible by both 3 and 5.

Input:
10 15 20 30 45 50 60 75


Expected output:
[15, 30, 45, 60, 75]
'''

if task == 'numbers divisible by 3 and 5':
    num = list(map(int,input().split()))
    output = [i for i in num if i%3==0 and i%5==0]
    print(output)




'''
Q6. Filter Palindromes

Take a list of words as input and create a new list containing only palindrome words.

A palindrome reads the same forwards and backwards.

Input:
madam hello level python radar world


Expected output:
['madam', 'level', 'radar']



Hint: Remember Python's string slicing technique:
'''

if task == 'filter_palindromes':
    words = input().split()
    output = [word for word in words if word[::-1]==word]
    print(output)



'''
Next challenge: Q7 – Filter by Multiple Conditions
Given a list of integers, select numbers that satisfy BOTH conditions:
1. Greater than 10.
2. Divisible by 3.
Input:
5 9 12 15 18 20 24 30 7


Expected output:
[12, 15, 18, 24, 30]



Use list comprehension.
'''

if task =='filter by multiple condition':
    loi= list(map(int,input().split()))
    output = [x for x in loi if x>10 and x%3==0]
    print(output)