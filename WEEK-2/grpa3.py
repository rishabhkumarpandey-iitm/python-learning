
#12-Hour Time	24-Hour Time
#12:00 AM (Midnight)	00:00
#6:00 AM	06:00
#12:00 PM (Noon)	12:00
#1:00 PM	13:00
#5:00 PM	17:00
#9:00 PM	21:00
#11:59 PM	23:59



time = '03 PM'
# time_in_hrs:int should have the time in 24 hrs format . Try to do this in a single expression
#t = int(time[:2])
#am_pm = time[-2:]
time_in_hrs = (int(time[:2]) % 12) + (0 if time[-2:]=='AM' else 12)
print(time_in_hrs)

