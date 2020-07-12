import json
import os

def title():
    print('''
    Welcome to the dictionary!
    - Type in the word you are searching for when prompted!
    - Input x if you would like to exit the application!
    ''')
title()
###
### Loading dictionary file that contains words in key and value format
###

os.chdir('/Users/luke/Desktop/Python/GitClone/PROJECT-English-Dictionary/Data')
#print(os.getcwd())
f = open('data.json','r')
dict = json.load(f)
# print(dict)

###
### Input/output
###

searching = True
while searching:
    # User Input
    word = input('\nWhat would you like to search?: ')
    if word == 'x':
        print('\nThank you for using this dictionary!')
        print('\nExiting Dicitonary...')
        searching = False
        exit()
    elif word in dict:
        print(dict[word.lower()])
    else:
        print('Sorry, the word you are looking for is not in the dictionary!')

    restart = True
    while restart:
        choice = input('\nWould you like to search another word? (Y/N) : ')
        if choice.lower() == 'y':
            break
        elif choice.lower() == 'n':
            print('\nThank you for using this dictionary!')
            print('\nExiting Dicitonary...')
            searching = False
            exit()
        else:
            print('\nSorry, that is an invalid input. \nPlease try again!')
            continue
    continue
