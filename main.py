from pyscript import display, document

def create_account(e):
    document.getElementById('final').innerHTML = ' '
    user = document.getElementById('username').value
    pa = document.getElementById('password').value
    alpha = pa.isalpha()
    num = pa.isdigit()

    if len(user) < 7:
        display(f'Your username is too short. Please add more characters.', target="final")
    
    elif len(pa) < 10:
        display(f'Your password is too short. Please add more characters.', target="final")

    elif alpha == True:
        display(f'Your password must contain at least one number.', target="final")

    elif num == True:
        display(f'Your password must contain at least one letter.', target="final")

    else:
        display(f'Account created.', target="final")
    

