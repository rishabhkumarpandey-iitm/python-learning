# A computer does exactly what it is told, nothing more and nothing less. At the lowest level it 
# understands only machine code, which is just 0s and 1s, that is not practical for us to write.
# Programming languaage allows us to communicate instructions to a computer in a form that can be executed by the computer.
# Python is one of them.

#why python?
# 1) Easy to read and write: Printing a greeting is one line in python. C or Java need several lines of setup for the same thing.
# 2)Libraries for Data Science and AI: NumPy, pandas, Matplotlib, scikit-learn and many more.
# How python work?
# we write code => Python Executes it => computer performs instruction => gives output
print("Hello World!") #print is function. () gives input to the function. "" text you want to display.
#You can print string, numbers, charecters, multiple objects(separeted by commas)

# Variables : used to store a value. it may vary or change.
age = 12
print(age)
print(30, 10, 55)
print(-20, -75, -91)
print(23.7)
print("Param", "Welcome to replit")
#How to print large numbers?
print(140,000,000) #After comma, it will be considered as new argument.
print(140000000) # hard to read
print(140_000_000) # easy to read
print("Hello, World")
print(12_34_56_78)



#name = input("Enter Your Name: ")  #takes imformation from user.
#print(name)

#age = int(input(' Enter your age:'))
# Calculating year of birth
#print(2026-age)
            

# Quotes:
# Single or double quotes both work, as long as opening and closing quote match.
print("Hello")
print('Hello')
#if text itself has a quote in it, wrap the text in other kind of quote.
print("It's a lovely day.")   #print('it's a lovely day.') =>this will give error coz python thinks the text ends at apostrophe in It's.
#Either use double quotes outside or put a backlash before the quote to say its a part of test
print('It\'s a lovely day')
print('He said "Hello" to me.')
print("He said \"Hello\" to me.")




