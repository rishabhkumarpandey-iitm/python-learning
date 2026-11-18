name = input("Enter Your Name:")
Location = input("Enter Your Location:")

#format of time:[2- digit hour][space][AM or PM]
time_start = input("Enter the time when you started your study:") 
time_end = input("Enter the time when you ended the study:")

#name,location,study_hrs

time_start_in_hrs = (int(time_start[:2])%12)+(12 if time_start[-2:]=='PM' else 0)
time_end_in_hrs = (int(time_end[:2])%12)+(12 if time_end[-2:]=='PM' else 0)
time_hrs = time_end_in_hrs - time_start_in_hrs
print(name,'studied','for',time_hrs,'hrs','at',Location)