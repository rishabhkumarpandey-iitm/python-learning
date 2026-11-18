number = int(input())
n = str(number)
sum = 0
for i in range(len(n)):
    sum += int(n[i])**len(n)
print(sum)