

print('entering while loop')
while True:
    print('in while loop')
    user_input_1 = input('enter 1 to continue, or 0 to leave >')

    if user_input_1 == '0':
        print('leaving while loop')
        break

    elif user_input_1 == '1':
        print('staying in while loop')

        while True:
            print('in nested while loop')
            user_input_2 = input('enter 1 or 0')

            if user_input_2 == '0':
                print('leaving nested while loop')
                break
            
            elif user_input_2 == '1':
                print('staying in while loop')