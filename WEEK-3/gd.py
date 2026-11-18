#write a python code using a while loop that counts from 1 to 17, and then enters an infinite loop when it reaches 18
i = 1
while i<=20:
    print(i)
    if i ==18:
        while True:
            print(i)
    else:
        i+=1
