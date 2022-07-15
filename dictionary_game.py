grocery_items = {1: 'test'} # empty dictionary to store items, first item added for testing

# allows the user to set a key for the item entered into dictionary
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


# allows user to enter an item to be entered into the dictionary
def enter_item():
    while True:
        try:
            get_item = input('Enter a grocery item to add to the list: ')
            for item in grocery_items:
                if get_item in grocery_items:
                    print('Item already in dictionary.. try again\n')
                    continue
                else:
                     return get_item
            
        except:
            print('Something wrong occurred... try again\n')