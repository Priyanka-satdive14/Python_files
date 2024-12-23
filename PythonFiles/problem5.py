
'''#### Problem Statement 2:
Write a Python program that:

1. Takes a sentence as input.
2. Counts the number of vowels in the sentence.
3. Reverses the sentence using string slicing.
4. Replaces all occurrences of a specific word in the sentence with another word using basic string operations.
'''
Sentance="I learn programming in python"
vowels = "aAeEIiOoUu"
count = 0
for i in Sentance:
    if i in vowels:
        count = count + 1
    
print(count)


#reverse sentence
reverse=Sentance[::-1]
print(reverse)

#replace
new_variable = "studid"
old_word="learn"
replaced_word=Sentance.replace(old_word,new_variable)
print(replaced_word)