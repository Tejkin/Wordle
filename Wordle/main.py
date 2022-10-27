import random

attempts = 0
MAX_ATTEMPTS = 6
ALL_WORDS_PATH = "C:/Users/CHENTH/Documents/Wordle-1/Wordle/word-bank/all_words.txt"
TARGET_WORDS_PATH = "C:/Users/CHENTH/Documents/Wordle-1/Wordle/word-bank/target_words.txt"

# Start the game
def start():
    attempts = 0
    target_word = get_target_word()
    print(target_word)
    while attempts < 6:
        guess_word = guess_input()
        target_letter = list(target_word)
        while True:
            if check_valid_word(guess_word) == True:
                break
            else:
                guess_word = guess_input()
        attempts = attempts + 1
        is_correct(guess_word, target_word, attempts)
        score = score_guess(guess_word, target_word)
        read_score(score, target_letter)

# Choosing Random Target Word
def get_target_word():
    fh = open(TARGET_WORDS_PATH, "r")
    words_list = []
    for words in fh:
        words = words.strip()
        words_list.append(words)
    target_word = random.choice(words_list)
    return target_word

# Ask for guess
def guess_input():
    return (input("Enter guess: "))

# Check for a valid word
def check_valid_word(guess_word):
    fh = open(ALL_WORDS_PATH, "r")
    valid_words = []
    for words in fh:
        words = words.strip()
        valid_words.append(words)
    if guess_word not in valid_words:
        print("This isnt a word")
        return False
    else:
        return True

# Check for correct guess
def is_correct(guess_word, target_word, attempts):
    if guess_word == target_word:
        if attempts == 1:
            print("Congratul---... Wait! You got it in one attempt??")
            quit()
        elif attempts == 2:
            print("Damn, I guess the word was too easy")
            quit()
        elif attempts >= 3:
            print("Congratulations!! You did it in " + str(attempts) + " attemps!")
            quit()
    else:
        return

# Scores guess
def score_guess(guess_word, target_word):
    position = [0, 0, 0, 0, 0]
    guess_letter = list(guess_word)
    target_letter = list(target_word)

    for i in range(0, 5):
        if guess_letter[i] == target_letter[i]:
            position[i] = 2
        if position[i] == 0:
            if guess_letter[i] in target_word:
                position[i] = 1
    return position

# Change scores to be readable
def read_score(score, target_letter):
    for i in score:
        if i == 2:
            index = score.index(i)
            score[index] = target_letter[index]
        if i == 1:
            index = score.index(i)
            score[index] = "?"
        if i == 0:
            index = score.index(i)
            score[index] = "X"
    print(' '.join(score))

        

start()