''' 
#### Problem Statement 1:

Write a Python program that checks if a given string is a palindrome (reads the same forward and backward).

'''
str1 = 'radar'
str2 =  str1[::-1]
if (str1 == str2):
    print (f'string {str1} is palindrome')
else:
    print (f'string {str1} is not palindrome')