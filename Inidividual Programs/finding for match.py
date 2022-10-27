
fh = open("all_words.txt")

##choose random target word
target_word = "movie"
target_letter = list(target_word)
all_words = []
attempts = 0
max_attempts = 6

while attempts < 6:

    guess_word = input("Enter guess: ")
    guess_letter = list(guess_word)
    position = [0, 0, 0, 0, 0]
    if len(guess_word) == 5:
        attempts = attempts + 1
        for i in range(0, 5):
            if guess_letter[i] == target_letter[i]:
                position[i] = 2
            if position[i] == 0:
                if guess_letter[i] in target_word:
                    position[i] = 1
        print(position)
        attempts_left = 6 - attempts
        str_attempts_left = str(attempts_left)
        print("You have " + str_attempts_left + " attempts left")
    else:
        print("Please only enter a 5 letter word")


    if guess_word == target_word:
        if attempts == 1:
            print("Congratul---... Wait! You got it in one attempt??")
            quit()
        elif attempts == 2:
            print("Damn, I guess the word was too easy")
            quit()
        elif attempts >= 3:
            attempts = str(attempts)
            print("Congratulations!! You did it in " + attempts + " attemps!")
            quit()

print("Sorry ;( You ran out of attempts")

