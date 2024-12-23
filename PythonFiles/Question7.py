'''
Define a procedure histogram() that takes a list of integers and prints a histogram to the
screen using a character '*'.
'''
data = [1,2,3,4,5]
count = 0 #use as index

#loop through each interger in the list
for number in data:
    print(f"{count}: ",end="")

    #print * those many times
    print("*"*number)
    count +=1     