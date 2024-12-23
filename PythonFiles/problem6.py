'''
Write a program that asks the user how many days are in a particular month, and what day of
the week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar
for that month.
'''
days_in_month = 30
start_day = 2

#boundary condition checks
if days_in_month not in [28,29,30,31]:
    print ('Invalid days in month entered')
if start_day < 0 or start_day > 6:
    print ('Invalid start day entered')

print("January")

#print the header for calender
print("Mo Tu We Th Fr Sa Su")

#print spaces for first week
current_day = 0
for _ in range(start_day): #throw away something put "_" not to store anything in it
    print ("   ",end="")#continue at line spces

#prints the  days of the month
for day in  range(1,days_in_month+1):
    print(f"{day:2} ",end="")
    current_day += 1
    
    position_count = current_day + start_day

    #move to next line after sunday
    if position_count % 7 == 0:
        print()
print()
print("\n") #new line after the calender




days_in_month = 28
start_day = 2

#boundary condition checks
if days_in_month not in [28,29,30,31]:
    print ('Invalid days in month entered')
if start_day < 0 or start_day > 6:
    print ('Invalid start day entered')

print("February")

#print the header for calender
print("Mo Tu We Th Fr Sa Su")

#print spaces for first week
current_day = 0
for _ in range(start_day): #throw away something put "_" not to store anything in it
    print ("   ",end="")#continue at line spces

#prints the  days of the month
for day in  range(1,days_in_month+1):
    print(f"{day:2} ",end="")
    current_day += 1
    
    position_count = current_day + start_day

    #move to next line after sunday
    if position_count % 7 == 0:
        print()
print()
print("\n") #new line after the calender




days_in_month = 30
start_day = 2

#boundary condition checks
if days_in_month not in [28,29,30,31]:
    print ('Invalid days in month entered')
if start_day < 0 or start_day > 6:
    print ('Invalid start day entered')

print("March")

#print the header for calender
print("Mo Tu We Th Fr Sa Su")

#print spaces for first week
current_day = 0
for _ in range(start_day): #throw away something put "_" not to store anything in it
    print ("   ",end="")#continue at line spces

#prints the  days of the month
for day in  range(1,days_in_month+1):
    print(f"{day:2} ",end="")
    current_day += 1
    
    position_count = current_day + start_day

    #move to next line after sunday
    if position_count % 7 == 0:
        print()
print()
print("\n") #new line after the calender