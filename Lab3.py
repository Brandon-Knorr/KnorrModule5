# Brandon Knorr
# Module 5 Lab 3
# 2/17


import re
from input_helper import get_email

#RegEx
# -regular expression
# -language agnostic
# -identifieng patterns in strings

# Selectors 
# - characters of the pattern 
# [abc] = "a" or "b" or "c" or that contains
# [a-c]
# [A-Z]
# [0-9] any number
# [a-zA-Z]
# [a-zA-Z0-9] 

# Quantifiers 
# - how many of a selection 
# - [a]{3} == [a] [a] [a] = 'aaa'
# [a]{3,5} = 'aaa' 'aaaa' 'aaaaa'
# [a]{3,} = 'aaa' 'aaaaa'

# Assertions 
# where to search for the pattern
# ^ start of the string 
# $ end of the string 

string_to_test = 'abcde'
test_pattern = r'[a]'
is_match = re.search(test_pattern, string_to_test)
if is_match:
    print('it is a match!')



email = get_email('please enter an email: ')