import random

# File Path
ALL_WORDS_PATH = "C:/Users/CHENTH/Documents/Python/Wordle/Wordle/word-bank/all_words.txt"
TARGET_WORDS_PATH = "C:/Users/CHENTH/Documents/Python/Wordle/Wordle/word-bank/target_words.txt"
# ALL_WORDS_PATH = "/Users/thomas/Documents/GitHub/Wordle/Wordle/word-bank/all_words.txt"
# TARGET_WORDS_PATH = "/Users/thomas/Documents/GitHub/Wordle/Wordle/word-bank/target_words.txt"



# Play the game
def play():
    attempts = 0
    target_word = get_target_word()
    if cheats == True:
        print("The target word is: " + target_word)
    while attempts < 6:
        guess_word = guess_input()
        target_letter = list(target_word)
        while True:
            if check_valid_word(guess_word) == True:
                break
            else:
                guess_word = guess_input()
        guess_letter = list(guess_word)
        attempts = attempts + 1
        is_correct(guess_word, target_word, attempts)
        score = score_guess(guess_word, target_word)
        read_score(score, target_letter, guess_letter, display)
        attempts_left(attempts)
    else:
        print("You've failed, the word was: " + Colours.GREEN + target_word + Colours.END)
    play_again()
        

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
            print("Correct word is: " + Colours.GREEN + target_word + Colours.END + "\nCongratul---... Wait! You got it in one attempt??")
            play_again()
        elif attempts == 2:
            print("Correct word is: " + Colours.GREEN + target_word + Colours.END + "\nNot bad, figuring out the word in 2 attempts.")
            play_again()
        elif attempts >= 3:
            print("Correct word is: " + Colours.GREEN + target_word + Colours.END + "\nCongratulations!! You did it in " + str(attempts) + " attemps!")
            play_again()
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
def read_score(score, target_letter, guess_letter, display):
    for i in score:
        if i == 2:
            colour = Colours.GREEN
            index = score.index(i)
            score[index] = colour + target_letter[index] + Colours.END
            keyboard(colour, guess_letter[index])
            display[index] = Colours.BOLD + Colours.GREEN + Colours.UNDERLINE + target_letter[index] + Colours.END
        if i == 1:
            colour = Colours.YELLOW
            index = score.index(i)
            score[index] = colour + guess_letter[index] + Colours.END
            keyboard(colour, guess_letter[index])
        if i == 0:
            colour = Colours.RED
            index = score.index(i)
            score[index] = colour + guess_letter[index] + Colours.END
            keyboard(colour, guess_letter[index])
    score = ' '.join(score)
    print(score + "\n")
    list_guess(score)
    print("\t" + ' '.join(display) + "\n")
    print_keyboard()
    

# Class holding colors
class Colours:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Print keyboard
def print_keyboard():
    print("   " + "  ".join(keys1))
    print("     " + "  ".join(keys2))
    print("\t" + "  ".join(keys3))

# Colour keyboard
def keyboard(colour, letter):
    letter = letter.upper()
    while True:
        if letter in keys1:
            index = keys1.index(letter)
            if keys1[index].startswith(Colours.GREEN):
                return
            else:
                keys1[index] = colour + letter + Colours.END
        elif letter in keys2:
            index = keys2.index(letter)
            if keys2[index].startswith(Colours.GREEN):
                return
            else:
                keys2[index] = colour + letter + Colours.END
        elif letter in keys3:
            index = keys3.index(letter)
            if keys3[index].startswith(Colours.GREEN):
                return
            else:
                keys3[index] = colour + letter + Colours.END
        else:
            return

# Print out attempts left
def attempts_left(attempts):
    attempts_left_over = MAX_ATTEMPTS - attempts
    if attempts_left_over >= 3:
        print("You have " + Colours.GREEN + str(attempts_left_over) + Colours.END + " attempts left")
    if attempts_left_over == 2:
        print("You have " + Colours.YELLOW + str(attempts_left_over) + Colours.END + " attempts left")
    if attempts_left_over == 1:
        print("You have " + Colours.RED + str(attempts_left_over) + Colours.END + " attempt left")

# Start asking for command input
def start():  
    global MAX_ATTEMPTS
    MAX_ATTEMPTS = 6
    global cheats
    cheats = False
    # Global lists holding keyboard letters and display
    global keys1, keys2, keys3, display, guess_list
    keys1 = list("QWERTYUIOP")
    keys2 = list("ASDFGHJKL")
    keys3 = list("ZXCVBNM")
    display = list("_____")
    guess_list = ["\tGUESSES"]
    while True:
        command_input = input("Would you lke to play Wordle? Y/N: ")
        if command_input.upper() == "Y":
            play()
        if command_input.upper() == "N":
            command_input = input("What would you like to do?\n1 - Change Max Attempts\n2 - Help\n3 - Toggle Answer Reveal: " + str(cheats) + "\n4 - Back\n5 - Exit\nPlease enter number corresponding to command: ")
            if command_input == "1":
                MAX_ATTEMPTS = int(input("The current Max Attempts is: " + str(MAX_ATTEMPTS) + ". What would you like it to be: "))
                continue
            elif command_input == "2":
                print("Help command output is still a work in progress..")
                continue
            elif command_input == "3":
                if cheats == True:
                    cheats = False
                elif cheats == False:
                    cheats = True
                continue
            elif command_input == "4":
                continue
            elif command_input == "5":
                exit()
            else:
                print("The entered input is invalid or out of scope")
                continue

# User input to play again after finished game
def play_again():
    user_input = input("Would you like to start again?: Y/N \n")
    if user_input.upper() == "Y":
        start()
    else:
        exit()

def list_guess(score):
    guess_list.append(score)
    print("\n\t".join(guess_list) + "\n")

start()