'''
A pangram is a sentence that contains all the letters of the English alphabet at least once, for
example: The quick brown fox jumps over the lazy dog. Your task here is to write a function
to check a sentence to see if it is a pangram or no
'''

import string

def is_panagram(Sentence):
    noramal_sentence = Sentence.lower() #remove spaces and make lowecase sentence
    alphabet_set = set(string.ascii_lowercase) #all letters in english alphabet
    sentence_set = set(noramal_sentence)  #set char of normal sentence

    return alphabet_set.issubset(sentence_set)

test_sentence = [
    "Go hang a salami I'm a lasagna hog.", 
    "Was it a rat I saw?", 
    "Step on no pets",
    "or the exclamation Dammit, I'm mad!"
]

for sentence in test_sentence:
    result = is_panagram(sentence)
    print(f'"{sentence}" -> Panagram :{result}')