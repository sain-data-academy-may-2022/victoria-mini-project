'''Function to clear screen in terminal'''

import os

def clear_screen():
    '''Function to clear the terminal screen'''
    # os.system('cls' if os.name == 'nt' else 'clear')
    # for windows
    if os.name == 'nt':
        os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')
    pass
