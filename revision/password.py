password = input('Please Enter Your Password:')
def digits_special_chars_in_strings(p:str):
    d =0
    s=0
    special_chars = ['#','@','$']
    for i in p:
        if i.isdigit():
            d+=1
        elif i in special_chars:
            s+=1

    return [d,s] 
special_chars = ['#','@','$']
if len(password)>=8 and digits_special_chars_in_strings(password)[0]>=1 and digits_special_chars_in_strings(password)[1]>=1:
    print('Password is correct!Fill other Details')
else:
    print('The entered password is wrong.It should have atleast of 8 chars and also make sure it must contain atleast one of special chars[#,@,$] and at least one digit')