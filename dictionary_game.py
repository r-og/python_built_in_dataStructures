import time

from cv2 import goodFeaturesToTrack # for visual

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
            if get_item in grocery_items.values(): # .values() used to check if value is in dictionary
                print('Item already in dictionary.. try again\n')
                continue
            else:
                return get_item
            
        except:
            print('Something wrong occurred... try again\n')
            continue


# full program to enter a grocery item into a dictionary
def enter_grocery_item():
    while True:
        try:
            add_item = input('Would you like to enter an item? y/n ')
            if add_item == 'y' or add_item == 'Y':
                key = enter_key()
                item = enter_item()

                grocery_items[key] = item
                time.sleep(2)
                print('item added')
                continue
            else:
                print('\nHere is your grocery list:')
                return grocery_items

        except:
            print('Something went wrong! try again\n')
            continue


print(enter_grocery_item())