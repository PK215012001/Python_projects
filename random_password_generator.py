# Python programme to generate some no.of random passwords
import random
import string
char_list = string.ascii_letters + string.digits + string.punctuation
# characters which are being used in generating the password
# char_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
#              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#              'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#              'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
#              'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
#              'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*',
#              '(', ')', '-', '_', '+', '=', '.']

FILE = 'random_passwords.txt'

def get_number(propmpt):
    '''Function to get a proper number from user'''
    while True:
        num = input(propmpt).strip()
        try:
            if (int(num) <= 0):
                print('Enter positive integers only.')
            else:
                return int(num)
        except ValueError:
            print('Invalid numerical value. Please enter valid numerical value.')
        

def generate_random_password(length):
    '''Function to generate random password of the given length'''
    password = random.sample(char_list, k= length)
    return ''.join(password)


def password_list(count):
    ''''Function to generate a list of given count of passwords'''
    for i in range(count):
        length = random.choice(range(8, 17))
        password = generate_random_password(length)
        yield password


def file_write(passwords):
    '''Function to write the genrated password into a file'''
    try:
        with open(FILE, 'w') as f:
            for password in passwords:
                f.write(f'{password}\n')
        print('Passwords written file.')
    except IOError as e:
        print(f'Error writting to a file:{e}')


# def radnom_password_length():
#     '''Function to randomly choose a number between 8 and 16'''
#     length = random.choice(range(8, 17))
#     return length


def main():
    # passwrd_lenght = radnom_password_length()
    # while(passwrd_lenght < 8 or passwrd_lenght > 16):
    #     print('Password length should be in between 8 to 16 characters')
    #     passwrd_lenght = get_number('Enter the length of the password you want: ')
    passwrd_cnt = get_number('Enter the random passwords count: ')
    list_passwords = password_list(passwrd_cnt)
    file_write(list_passwords)


if (__name__ == '__main__'):
    main()