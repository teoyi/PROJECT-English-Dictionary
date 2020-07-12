import json
import os

def title():
    print('''
    Welcome to the dictionary!
    Type in the word you are searching for when prompted!
    Input x if you would like to exit the application!
    ''')

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
#
# searching = True
# while searching:
#     # User Input
#     word = input('\nWhat would you like to search?: ')
#     if word == 'x':
#         exit()
#     else:
#         print(dict[word.lower()])
#         break
#
# finish = True
# while finish:
#     choice = input('\nWould you like to search another word? (Y/N) : ')
