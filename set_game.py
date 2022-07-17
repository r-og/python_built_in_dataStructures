enter_words = [] 

while True:
    try:
        participate = input('Would you like to enter a word? (y/n) ')
        if participate == 'y' or participate == 'Y':
            enter_this_word = input('Please enter a word: ')
            enter_words.append(enter_this_word)

        elif participate == 'n' or participate == 'N':
            print(set(enter_words))
            break
        else: 
            break
    except ValueError:
        print('Wrong value entered ...')
        continue

    print(enter_words)

