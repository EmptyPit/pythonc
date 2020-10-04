#!/usr/bin/env python3
import re


class Login:

    def __init__(self, name, password):
        self.name = name
        self.password = password
        # self.sex = sex
        # self.birth = birth
        # self.email = email

    @staticmethod
    def from_file_to_dict():
        with open('/home/andrii/text.txt') as file:
            read = dict([line.strip('\n').split() for line in file.readlines()])
            return read

    def write_to_file(self, smt_to_write):
        if smt_to_write:
            with open('/home/andrii/text.txt', 'a') as file:
                file.write(smt_to_write)

    def sign_in(self, dict_with_data):
        for i in dict_with_data:
            if self.name == i and self.password == dict_with_data[i]:
                return 'Welcome back {}'.format(self.name)
        return 'Wrong password or name try again'

    def validate_password(self):
        validate_string = re.search(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,12}$', self.password)
        if validate_string:
            print('Password validation sucsses')
            return True
        else:
            print('Password validation failed')
            return False

    def validate_username(self, read_from_txt):
        validate_user = re.search(r'^(?=.*?\w).{6,10}$', self.name)
        if validate_user and self.name not in read_from_txt:
            print('Username validation passed')
            return True
        elif self.name in read_from_txt:
            print('This username is already taken, chouse another')
            return False
        else:
            print('Username validation failed')
            return False

    def sign_up(self, val_password, val_username):
        string_to_write = '{} {}\n'.format(self.name, self.password)
        if val_password and val_username:
            print('New user added successful')
            return string_to_write
        else:
            return None

#commit1
#commit2

#commit3

if __name__ == "__main__":
    ch = input('If you want to register write 1 or if you want to sign in 2  ')
    if ch == '1':
        n = input('Please enter your name ')
        p = input('Please enter your password, it should be from 8 to 12 chars, include 1 digit, 1 special '
                  'char, 1 upper and dont include space ')
        lo = Login(n, p)
        print(lo.write_to_file(lo.sign_up(lo.validate_password(), lo.validate_username(Login.from_file_to_dict()))))
        # name = input('Please loggin into the system, Enter your name ')
        # password = input('Please enter your password ')
        # signin = Login(name, password)
        # print(signin.sign_in(Login.from_file_to_dict()))
    elif ch == '2':
        n = input('Please enter your name  ')
        p = input('Please enter your password  ')
        lo = Login(n, p)
        print(lo.sign_in(lo.from_file_to_dict()))
    else:
        print('Wrong input, choose between 1 or 2')



