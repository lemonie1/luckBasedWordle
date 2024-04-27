import random

word_list = ["apple", "banana", "orange", "grape", "kiwi"]
random_word = random.choice(word_list)

inputs = input("What is the word?: ")
if inputs == random_word:
    print("Great Job")
else:
    print("Wrong")
