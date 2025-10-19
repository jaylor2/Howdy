#!/usr/bin/python3
#'import' brings 'requests' library into scope.
import requests
import json 
import sys

def chuckit(category):
    #'r' is the name of the variable where the result of the GET is stored.
    #'=' is an assignment operator, tells Python to store GET result in 'r'
    r = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')

    #'data' is the variable where JSON().GET request will be stored.
    #'r.son().get('value')'  tells Python to get the 'value' from the JSON data
    data = r.json().get('value')
    #print(data) tells Python to print the result of 'data'
    print(data)


#Defining function to check if the searched category exists
def catchuck(category):
    #gets category list
    response = requests.get('https://api.chucknorris.io/jokes/categories')
    #checks if response OK, if response OK, turn JSON response into a Python-parsable list and store in pythonlist
    if response.status_code == 200:
         pythonlist = response.json()
    #Very rudimentary error code handling; could revamp later with handling for each error code instead of just "Status Error"
    else:
        print('Status Error')
    #if the category is in our list, return the category, if not then we'll keep our list.
    if category in pythonlist:
        return category
    else:
        return pythonlist

#created a help function for further error handling
def help(categories):
    print('Category Unavailable. Avalailable categories are:')
    for category in categories:
        print(category)


#created main function to bring everything under one command and included help function.
def main(category):
    check  = catchuck(category)
    if type(check) is list:
        help(check)
    chuckit(category)
#allows us to run the script with arguments using "sys.argv[]"
main (sys.argv[1])

