"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here


def get_user_input():

    user_input = input("-> ")
    tokens = user_input.split(" ")

    return tokens


def exit_program(tokens):

    if tokens[0] == 'q':
       
        print('You exited the program.')
        
        return



    elif len(tokens) < 2:
        print('There are not enough inputs')
        

