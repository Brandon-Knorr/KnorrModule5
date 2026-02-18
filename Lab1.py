# Brandon Knorr
# Mod 5 Lab 1 
# 2/17 11:59

# dictionaries are a collection 
# key value pairs 
# keys and values can be any data type you want like a string, int, etc
# keys must be unique 
# 
# 

from input_helper import get_int_in_range

happiness_level = {
    1: 'sad',
    2: 'moderate',
    3: 'happy',
} 

print(happiness_level[1])


user_happiness = get_int_in_range('Enter happiness level from 1-3: ', 1, 3)

#Expressions are anything that resolve to a single value 
print(f'Today you are feeling {happiness_level[user_happiness]}')


county_population = {
    'Milwaukee': 930500,
    'Dane': 605563,
    'Waukesha': 423061,
    'Brown': 277579,
    'Racine': 201139,
}

# create a new key
county_population['Outagamie'] = 198514

# deleting a key
county_population.pop('Brown')

# update a key
county_population['Milwaukee'] = 1000000

# reading a key
for x in county_population:
    print(f'{x} county has a population of {county_population[x]}')

# tuple is the simplest collection you can have 
# you create these with ()
my_tuple = (3, 'Brandon', True)

for key, value in county_population.items():
    print(f'{key}: {value}')

