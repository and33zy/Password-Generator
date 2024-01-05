import random   #Module that allows to generate random values
import string   #Module that allows to use special characters and numbers

x = string.ascii_letters + string.digits + string.punctuation
"""
Assigns the variable x to 3 different functions from the string module
joined with the + symbol
"""

j = int(input("How many characters do you want?"))
# assigns the variable j to user input, and also formats the input to an integer

"""
defining a function that takes parameter 'a' which will be replaced
with the variable j
"""

def pwgen(a):
    if a < 8:   #default str length must be 8 if user input is less than 8
        a = 8
    pw = ''
    for i in range(a):
        pw += random.choice(x) #loops function random.choice(x) which makes the characters
    return pw

print("Your password is:", pwgen(j))
input("Press enter to exit")
