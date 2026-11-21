sentence = input()
def count_vowels(s:str):
    v=0
    for i in s:
        if i.lower() in 'aeiou':
            v+=1
    return v

output=''
for i in sentence.split():
    output+=i+'('+str(count_vowels(i))+') '
print(output)
    

