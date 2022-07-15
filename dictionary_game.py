grocery_items = {1: 'test'} # empty dictionary to store items

def enter_key():
    while True:
        try:
            get_key = int(input('Please enter a key: '))
            for key in grocery_items:
                if get_key in grocery_items:
                    print('Key already in use... try again\n')
                    continue
                else:
                    return get_key
        
        except ValueError:
            print('Try again, not a number!\n')
            continue


print(enter_key())