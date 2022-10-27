import random

fh = open("target_words.txt")

words_list = []

for words in fh:
    words = words.strip()
    words_list.append(words)

target_word = random.choice(words_list)

print(target_word)