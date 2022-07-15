import time # solely used as a "visual" to the user
# starter list, add more later
word_list = ['random', 'robbed', 'alphabet', 'add',
             'break', 'cactus', 'bunny', 'rain', 'honk']

# function used to accept user input for word search


def grab_letter():
    letter = input('Enter a letter you\'d like to find words for: ')
    time.sleep(2)
    return letter


# function used to grab words based on letter user enters
def grab_words():
    letter = grab_letter()
    words_generated = []  # empty list to store words

    for word in word_list:
        if word.startswith(letter):
            words_generated.append(word)

    # keeps track of how many words are returned
    word_count = len(words_generated)
    print(f'Number of words found {word_count}')
    time.sleep(2)
    print(words_generated)


print('Welcome to WORD GRABER\nFollow the prompts to get your words')
time.sleep(2)
grab_words()
