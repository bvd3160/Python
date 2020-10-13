import random

final_word_segment = ""
segments = []
dictionary = {'honey': 'Something produced by bees', 'milk': 'From cows, goats and sheep', 'bat': 'Used in Baseball',
              'fish': 'They live in the sea', 'batman': 'He wanders the streets of Gotham',
              'football': 'The beautiful game', 'rules': 'We were made to be broken', 'spongebob': 'Lives in a pineapple',
              'python': 'A snake and programming language', 'matrix': 'Main Character is Neo'}
# list of words to guess from
guess_words = list()
for i in dictionary.keys():
    guess_words.append(i)

# choose a word to be guessed from the list of words
selected_word = random.choice(guess_words)

# randomly selected word from the list to play hangman with.
selected_word = random.choice(guess_words)
# the length of the randomly selected word
word_length = len(selected_word)
# number of guesses the player has
lives = int(word_length / 1.5)
guessed = False

for (key, value) in set(dictionary.items()):
    if (key == selected_word):
        print("HINT:", value)
# START initialisation of layout showing how many spaces the word will occupy.
for x in range(0, word_length):
    print('_ ', end='')
print("\n")


# END initialisation


# split the selected word into individual characters
def split_word():
    word_list = list(selected_word)
    return word_list


# is the letter valid?
def valid_letter(letter):
    letter = str(letter)
    if (letter in selected_word and len(letter) == 1):
        return True


# is the letter valid?
def valid_word(word):
    word = str(word)
    if (word == selected_word):
        return True


# Hangman Processing
while (lives > 0):

    # first guess request
    print("GUESSES LEFT:", lives)
    user_input = str(input(("Enter a LETTER or GUESS the word if you think you know it: ")))
    lives -= 1
    # take the letter the user enters and compare it with the ones in the word
    # 1. Boolean - is the letter in there?
    if (valid_letter(user_input)):
        print("Yes '", user_input, "' is in there")
        for x in range(len(split_word())):
            if (user_input == split_word()[x]):
                final_word_segment = split_word()[x] + " "
                segments.append(user_input)
                print(final_word_segment, end='')
            else:
                final_word_segment = " _ "
                print(final_word_segment, end='')
        '''
        #print("\n",segments)
        for y in range (len(split_word())):
            for val in segments:
                if(val == split_word()[y]):
                    print(split_word()[y] + " ", end='')
                else:
                    print(" _ ", end='')
        '''
        print("\n___________________________________")
    elif (valid_word(user_input)):
        word_list = split_word()
        for i in range(len(word_list)):
            print(word_list[i] + " ", end='')
        print("\nYou have successfully guessed the word, and avoided HANGING! Well done!!", "GUESSES LEFT:", lives)
        print("___________________________________")
        guessed = True
        break
    else:
        if (len(user_input) == 1):
            print("Sorry! that letter is not in the word.", "GUESSES LEFT:", lives)
            print("___________________________________")
        else:
            print("Is that even a word? Well, either way you took as stab and got it wrong so...", end='')
            lives = 0;
if (lives == 0 and guessed == False):
    print("\nunfortunately you've run out of guesses: TIME FOR YOUR HANGING! \nThank you for playing!",
          "GUESSES LEFT:", lives)
