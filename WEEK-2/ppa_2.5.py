
'''
n = int(input())
prime = True
for i in range(2,n):
    if n%i==0:
        prime = False
        break

if prime:
    print('yes')
else:
    print('no')

'''


'''
Name: bmi_category
Inputs: weight_kg:float, height_m:float
Output: BMI = weight / height^2. Print "underweight" if BMI < 18.5, "normal" if < 25, "overweight" if < 30, "obese" otherwise.

weight_kg = float(input())
height_m = float(input())
bmi = weight_kg/(height_m**2)
if bmi<18.5:
    print('underweight')
elif bmi<25:
    print('normal')
elif bmi<30:
    print('overweight')
else:
    print('obese')

    
'''


a = int(input())
b = int(input())
c = int(input())
print(max(a,b,c))