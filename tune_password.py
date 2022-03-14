def checkslash(password: str) -> str:
    # removes (if we need) _ and - from password
    items = ['_', '-']
    possibilities = {'y', 'yes', '1'}
    test = {'test', 'unittest', 'unit_test', 'unit', 'unit test'}

    for i in range(len(items)):
        print(f'do we need to remove {items[i]} in password? write 1, y, yes')
        # write smth from {test} for unit test
        check_letter = input()

        if(check_letter.lower() in test):
            print("unit test!")
            for item in items:
                password = password.replace(f'{item}', '')
                return password

        elif(check_letter.lower() in possibilities):

            password = password.replace(f'{items[i]}', '')

    return password


def up_low_dig(password: str) -> str:
    # removes (if we need) upper letters (ABCD) lower (abcd) and digits
    # for upper and lower it makes upper -> lower and back
    items = ['upper letters', 'lower letters', 'digits']
    possibilities = {'y', 'yes', '1'}
    # write smth from {test} for unit test
    test = {'test', 'unittest', 'unit_test', 'unit', 'unit test'}

    for i in range(len(items)):
        print(f'do we need to remove {items[i]}? write 1, y, yes')
        check_letter = input()

        if(check_letter.lower() in test):
            print("unit test!")
            for item in items:
                password = password.replace(f'{item}', '')
                return password

        if(check_letter.lower() in possibilities):
            password = [
                password.lower(),
                password.upper(),
                ''.join([i for i in password if not i.isdigit()]),
            ][i]

    return password


if __name__ == '__main__':
    print('u cant run this file as main!')
