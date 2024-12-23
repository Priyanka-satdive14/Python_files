people = {'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
print(f"Number of person :{len(people)}")
people['Lisa']='black'
print (f"updated colour:{people['Lisa']}")
del people['Jenny']
sort_people = dict(sorted(people.items()))
print("student and their fav colur in sorted order")
for student,colour in sort_people.items():
    print(f'{student}: {colour}')
people