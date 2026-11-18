marks = [12, 45, 67, 19, 20, 12, 45, 45]
print(marks)

#Acessing elements from lists.
#Indexing retrieves a single element from a list. Every element has an index. Python starts counting from 0, not 1.
#Negative indexing --> Python also allows you to access elements from the end of a list using negative indices.
print(marks[0])
print(marks[-1])

#List slicing --> Slicing allows you to extract multiple elements from a list.  -->list[start:stop:step]
#the start index is included, but the stop index is excluded.


#updating 
marks[0] = 'Rishabh'
print(marks)  # list of index 0 will be replaced by 'Rishabh'.

# marks.reverse() --> reverses the list in-place instead of creating new list.
rev_list = reversed(marks)
print(type(rev_list))  #<class 'list_reverseiterator'>


s = 'Param is good boy'
ls = list(s)
print(ls)   # ['P', 'a', 'r', 'a', 'm']


s = [1,2,3]
s2 = [1,2,3]
s3 = s
print(s,s2,s3)
s3[1] = 0
print(s,s2,s3)

# why s3 and s both got changed?
#this happens because s3 = s does not create a new list. It makes s3 refer to the same list as s.


#What if you want s3 to be independent?
#Use .copy():

a = [22,25,78]
b = [33,99,88,66]
c = a.copy()
print(a,b,c)
c[2]= 'RISHABH'
print(a,b,c)


# REMEMBER:
# s3 = s → both names refer to the same list.
# s3 = s.copy() → separate lists. or you can use s3 = s[:]


# append and insert

	#append():	Adds at the end.. Syntax: s.append(50)
    #insert(): Adds at a specified index.  insert(index, value)


# remove -- removes the value
# pop ---removes the index



#index  ----.index() method is used to find the index (position) of an element in a list.
# .index() method returns the index of the first occurrence of the specified value.
# You can tell Python where to begin searching. list.index(value, start, end)


# .sort() --> method is used to arrange the elements of a list in a particular order.

#s.sort()	Sorts the original list in ascending order
#s.sort(reverse=True)	Sorts the original list in descending order
#sorted(s)	Returns a new sorted list; original remains unchanged

#.extend() method adds all elements from an iterable (such as another list) to the end of an existing list.


#.clear() makes the list empty.


'''Lists and Tuple:
What is a List?
A list is an ordered collection of elements that you can modify after creating it.
Lists are mutable. Mutable means you can change the elements after creating the list.

What is a Tuple?
A tuple is an ordered collection of elements that cannot be modified after creation.Tuples usually use parentheses ().
Tuples are immutable. Immutable means you cannot change an existing element directly.
'''



#matrix 

matrix = [
    [1,2],
    [4,5]
]

matrix2 = [
    [5,6],
    [7,8]
]

m = len(matrix)
n = len(matrix[0])
final_matrix = []
for i in range(m):
    inner = []
    for j in range(n):
        s = matrix[i][j] + matrix2[i][j] 
        inner.append(s)
    final_matrix.append(inner)
print(final_matrix)



#create a matrix of nxn:

n = int(input()) 
matrix = [] 
for i in range(n):
    row = []
    for j in range(n):
        x = int(input())
        row.append(x)
    matrix.append(row)

print(matrix)
