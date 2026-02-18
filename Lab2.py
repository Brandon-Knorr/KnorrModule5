# Brandon Knorr
# Mod 5 Lab 2 
# 2/17

from input_helper import *

flag_colors = {
    'Japan': [ 'red', 'white'],
    'Haiti': ['red', 'white', 'blue', 'green'],
    'Ghana': ['red', 'yellow', 'green', 'black'], 
}

def list_flags():
    for flag, colors in flag_colors.items():
        print(f'{flag}:\n\t {", ".join(colors)}')

list_flags()

# if they do add_flag with no parameter country will be ''
# if they use a parameter country will be set

def add_flag(country = ''):

    if country:
        flag = country.capitalize()
    else:
        flag = input('what countries flag do you want to add: ').capitalize()
        
    colors = []

    while True:
        color_to_add = input("\tAdd a color (press enter to stop): ")
      

        if not color_to_add:
            break
            
        colors.append(color_to_add)

    flag_colors[flag] = colors


def search_flags():
    flag = input('which countries flag do you want to see: ').capitalize()

    if flag in flag_colors: 
        print(f'{flag} colors are  {', '.join(flag_colors[flag])}')
    else:
        print(f'we have no record of {flag}. Please add it!')
        add_flag(flag)




while True: 
    clear_console()
    print('--- Flag Database ---')
    print('\t1. List')
    print('\t2. Add')
    print('\t3. Search')
    print('\t4. Exit')
    choice = get_int_in_range("\tSelection: ", 1, 4)

    if choice == 1:
        list_flags()
    elif choice == 2:
        add_flag()
    elif choice == 3:
        search_flags()
    else:
        break

    input('\n\n\nPress enter to continue')

