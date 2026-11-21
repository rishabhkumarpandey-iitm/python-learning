'''
words_with_repeated_letters: Return a set of words that contain at least one repeated letter.
'''
# s = input()
# output= set()
# for i in s.split():
#     if len(set(i))!=len(i):
#         output.add(i)

# print(output)

''''common_items_sorted: Return common items from all given collections as a sorted list.'''
collection= ["hello", ["h", "e", "l"], ("l", "h", "o")]
output = set(collection[0]).intersection(collection[1:])
print(output)




