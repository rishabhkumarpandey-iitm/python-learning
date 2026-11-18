'''
Vowel counter: Count the number of vowels in a string.
Name: vowel_count
Inputs: text:str
Output: the count of vowels (as an integer).

'''
text = input()
v = 'aeiou'
vowel_count = 0
for i in text.lower():
    if i in v:
        vowel_count+=1

print(vowel_count)
