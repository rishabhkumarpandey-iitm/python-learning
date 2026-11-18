#Permutation (permutation): Given a string s, print all the possible two-letter permutations(without repitition) of the letters in the string.
task = input()

if task == 'permutation':
    s = input()
    for i in s:
        for j in s:
            if i!=j:
                print(i+j)

elif task == 'sorted_permutation':
    s = input()
    for i in s:
         for j in s:
              if i!=j and i<j:
                  print(i+j)
    