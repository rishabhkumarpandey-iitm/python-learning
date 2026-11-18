

#Perfect square checker: Check whether the input number is a perfect square.

#num = int(input())
#s1 = (num**0.5)

#s2 = s1**2
#if s2 == num:
    #print('yes')
#else:
    #print('no')
#print(s1, s2)
#if (num**0.5)**2 == num:
    #print('yes')
#else:
    #print('no')
#print(num == s2)

#error: it is better approach to take integer of s1 and then check it's square.

num = int(input())
print('yes' if (int(num**0.5))**2 == num else 'no' )

#Vowel checker: Check if a string has a vowel in it.
inp = input().lower()
print('yes' if (('a' in inp) or ('e' in inp) or ('i' in inp) or ('o' in inp) or ('u' in inp)) else 'no')

#Palindrominator: Takes a string and joins it with the same string reversed. Eg. "cal" -> "calac".
text = input()
print(text+text[-2::-1])
