#reverse_sum_palindrome
#odd_char:

output = ' '
while True:
    word = input()
    output+=word[::2]
    if word.endswith('.'):
        break
print(output)
