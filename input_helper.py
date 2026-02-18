# Brandon Knorr
# input helper file

import os
import re

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def clear_console():
    # Use 'cls' for Windows (nt) and 'clear' for Linux/macOS (posix)
    os.system('cls' if os.name == 'nt' else 'clear')


def get_int_in_range(prompt, bottom, top):
    while True:
        try:
            user_input = int(input(prompt))
            if bottom <= user_input <= top:
                return user_input
            else:
                print(f"Please enter a number between {bottom} and {top}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_email(prompt):
   #From: https://uibakery.io/regex-library/email-regex-python 
    email_pattern = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"

    while True:
        email = input(prompt)
        if re.search(email_pattern, email):
            return email
        print('invalid email.')


def get_letters(prompt):
    letter_pattern = r"^[a-zA-Z]+$"
    while True:
        user_input = input(prompt)
        if re.match(letter_pattern, user_input):
            return user_input
        print('please enter only letters')

