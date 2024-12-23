'''
Problem Statement 2:
Write a Python program that takes a full name as input in the format "First Last".
- Make sure it is in "title case" i.e. first letter capitalized.
- Assign the first name and last name to two separate variables at once.
- Format the output to display the name as "Last, First".
- Print the initials of the name using string slicing.

Example imput : full_name = 'Donald tRump'

'''

f_name = "priyanka sAtdive"
F1 = f_name.title()
first,last = F1.split()
print (f'{last} , {first}')
print (f'"{last[0]}{first[0]}"')#### Problem Statement 2:
