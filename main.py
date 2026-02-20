from pyscript import display
from js import document

def signup(e):
    document.getElementById('output').innerHTML = ''
    # these gets the user and password inputted by the person
    password = document.getElementById('password').value
    username = document.getElementById('username').value

    #this uses simple math to tell user to add more characters to username
    if len(username) < 7:
        remaining = 7 - len(username)
        display(f'Your user is too short. Add at least {remaining} more character/s to proceed.', target='output')

    #these executes the conditions for the password
    elif len(password) < 10:
        passrem = 10 - len(password)
        display(f'Password is not strong enough. Add {passrem} more character/s to proceed.', target='output')

    elif not any(char.isdigit() for char in password):
        display('Password must contain at least one number.', target='output')

    elif not any(char.isalpha() for char in password):
        display('Password must contain at least one letter.', target='output')

    else:
        display('Account Created!', target='output')