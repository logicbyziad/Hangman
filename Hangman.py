###############################################################################
############################### Hangman #######################################
###############################################################################

import random

## File Handling
with open('word_bank.txt', 'r') as file:
    content = file.read()

word_list = content.split()

hang_word = random.choice(word_list).lower()

word_length = len(hang_word)

chances = word_length +2
guess_no = 0
guessed_letters = 0
incorrect = []
correct = []
print("#######################################\n")

word_string = str("_ "*word_length)
print(word_string)

##########################################################################
########################### Functions ####################################
##########################################################################

## spacer function
def spacer():

    print("#######################################\n")

## Function that returns position of letter in the word, else gives empty list
def is_there(letter, word):

    positions = [index for index, char in enumerate(word) if char == letter]
    return positions


## Function for Character/Word Visual
def print_word (letter, positions):
    global guessed_letters
    global word_string
    global word_list

    word_list = list(word_string)

    for i in range(len(word_string)):
        
        if (i/2 in positions) and (word_list[i] == '_') :
            word_list[i] = letter
            word_string = ''.join(word_list)
            guessed_letters += 1

    print(word_string)


##########################################################################
############################### Logic ####################################
##########################################################################

while (guess_no < chances):

    spacer()
    guess_input = input("Guess the word, or man gets hanged!\n").lower()
    guessed_letter = guess_input[0]
    already_guessed = (guessed_letter in incorrect) or (guessed_letter in correct) 

    while (already_guessed):
        guess_input = input("Letter is already guessed\n").lower()
        guessed_letter = guess_input[0]
        already_guessed = (guessed_letter in incorrect) or (guessed_letter in correct) 
    
    place_list = is_there(guessed_letter, hang_word)

    if (place_list == []):
        incorrect.append(guessed_letter)
        guess_no += 1
        print(f"Incorrect, Try Again\nIncorrect Letters: {incorrect}")
        print(word_string)

    else:
        correct.append(guessed_letter)
        guess_no += 1
        print_word(guessed_letter, place_list)
        print(f"Incorrect Letters: {incorrect}")
    
    if guessed_letters == word_length:
        print(f"YOU WON!\nThe word is \"{hang_word}\"\n")
        spacer()
        break
    
    if guess_no == chances:
        print(f"GAME OVER!\nThe word was \"{hang_word}\"\n")
        spacer()
        break