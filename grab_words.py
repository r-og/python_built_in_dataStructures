import time
# starter list, add more later
word_list = ['random', 'robbed', 'alphabet', 'add', 'break', 'cactus', 'bunny', 'rain', 'honk']

def grab_letter():
    letter = input('Enter a letter you\'d like to find words for: ')
    time.sleep(2)
    return letter



def grab_words():
    letter = grab_letter()
    words_generated = [] # empty list to store words

    for word in word_list:
        if word.startswith(letter):
            words_generated.append(word)
    
    word_count = len(words_generated) # keeps track of how many words are returned
    print(f'Number of words found {word_count}')
    time.sleep(2)
    print(words_generated)


print('Welcome to WORD GRABER\nFollow the prompts to get your words')
time.sleep(2)
grab_words()
