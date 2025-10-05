#!/usr/bin/python3
#'import' brings 'requests' library into scope.
import requests

#'r' is the name of the variable where the result of the GET is stored.
#'=' is an assignment operator, tells Python to store GET result in 'r'
r = requests.get('https://api.chucknorris.io/jokes/random')

#'data' is the variable where JSON().GET request will be stored.
#'r.son().get('value')'  tells Python to get the 'value' from the JSON data
data = r.json().get('value')

#print(data) tells Python to print the result of 'data'
print(data)

