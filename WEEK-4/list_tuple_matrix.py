marks = [23,78,39,56,10,10,10,23,78,23,23]
print(marks)
mid = len(marks)//2
print(marks.index(23, mid, mid+5))

#use pop to remove duplicates?
# remove duplicates 23 in marks list using pop.
while marks.count(23)>1:
    idx = marks.index(23)
    marks.pop(idx)
print(marks)

'''
Tuple is more memory efficient than set.
-indexing & slicing can be done.
-it is immutable i.e. it can't be modified.
'''
records = (23, 'param', 17, 30, 7, False, [23,54])

marks.extend(records)   #list and tuple concentenation
print(marks)

s = 'rishabh'
marks.extend(s)    #list and string concantenation
print(marks)


#singleton list
marks = [23]
print(type(marks))

#singleton tuple
marks = (23, )  # marks = 23,
print(marks)


matrix = [
    [1,2],
    [4,5]
]

matrix2 = [
    [5,6],
    [7,8]
]

final_matrix=[]
m = len(matrix) #rows
n = len(matrix[0])

for i in range(m):
    inner =[]
    for j in range(n):
        s = matrix[i][j]+matrix2[i][j]
        inner.append(s)
    final_matrix.append(inner)

print(final_matrix)



#n = int(input())
#matrix = []
#for i in range(n):
    #row=[]
    #for j in range(n):
        #x = int(input())
        #row.append(x)
    #matrix.append(row)
#print(matrix)



#how to create matrix?
#n = int(input())
#matrix = []
#for i in range(n):
    #row = input().split()
    #row = list(map(int, row))
    #matrix.append(row)
#print(matrix)

#explore map, split in python.




# create an identity matrix?
n = int(input())
identity_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
        if i==j:
            row[j]=1
    identity_matrix.append(row)

print(identity_matrix)
