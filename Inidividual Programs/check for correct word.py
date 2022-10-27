fh  = open("all_words.txt")
all_words = []

while True:
    guess_word = input()
    for words in fh:
        words = words.strip()
        all_words.append(words)
    if guess_word not in all_words:
        print("This isnt a word")
    else:
        print("Correct")