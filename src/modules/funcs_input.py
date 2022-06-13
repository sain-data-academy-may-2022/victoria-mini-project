'''Module which handles all input functions within the app'''

####################
###### INPUTS ######
####################
# formats a string for proper insertion
def format_string(text: str):
    '''Formats a given string for proper insertion'''
    return text.strip(' £\n\t').title()


# takes a question to ask the user and returns an integer response, allows blank responses if set
def get_int_input(question: str, allow_blank: bool = False, allow_zero: bool = False):
    '''Gets an input question and returns the exact integer if the input can be converted, the number is positive, and allow_blank = False.
    Otherwise returns an empty string if allow_blank is True'''

    valid_num = False

    while not valid_num:
        number = input(f'{question}:\n ')
        try:
            number = int(number)

            if (allow_zero and number == 0) or number > 0:
                valid_num = True

            else:
                raise(ValueError)

        except ValueError:
            if allow_blank and number == '':
                return ''
            else:
                print('Please enter a valid number.')
                return get_int_input(question, allow_blank)
            
    return number


# takes a question to ask the user and returns a float response, allows blank responses if set
def get_float_input(question: str, allow_blank: bool = False):
    '''Gets an input question and returns the exact float if the input can be converted, the number is positive, and allow_blank = False.
    Otherwise returns an empty string if allow_blank is True'''

    valid_num = False

    while not valid_num:
        number = input(f'{question}:\n ')
        try:
            number = float(number)

            if number > 0:
                valid_num = True

            else:
                raise(ValueError)

        except ValueError:
            if allow_blank and number == '':
                return ''
            else:
                print('Please enter a valid number.')
                return get_float_input(question, allow_blank)
            
    return number


# takes a question to ask and returns a string response, allows blank responses if set
def get_string_input(question: str, allow_blank: bool = False):
    '''Gets an input question and returns a non-empty string if allow_blank = False
    and allows an empty string if allow_blank = True'''

    answer = format_string(input(f'{question}\n> '))
    
    if len(answer) > 0 or (answer == '' and allow_blank):
        return answer
    
    elif answer == '' and not allow_blank:
        print('Empty answers not allowed.')
        return get_string_input(question, allow_blank)


# next function here
def func():
    pass

