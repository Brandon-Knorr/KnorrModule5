# Brandon Knorr
# Mod 5 Lab 4
# 2/17

from input_helper import *

role_duty = {
    "Administrator": "Duties relate to the functions of the college and supporting students outside of the classroom",
    "Instructor": "Support students through creation and execution of lesson plans",
    "Student": "Attend classes and complete coursework to earn a degree"
}

class Stakeholder:
    def __init__(self, fname, lname, email, role):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.role = role

    def __str__(self):

        duty = 'no description for that role'

        if self.role in role_duty:
            duty = role_duty[self.role]
        

        return f'{self.lname}, {self.fname} | {self.email}\n\t{self.role}: {duty}'
    

stakeholders = [
    Stakeholder("John", "Doe", "jdoe2@my.wctc.edu", "Student"),
    Stakeholder("Patrick", "Gerber", "pgerber1@wctc.edu", "Instructor"),
    Stakeholder("Alli", "Jerger", "ajerger@wctc.edu", "Administrator")
]

def list_stakeholders():
    for i, s in enumerate(stakeholders):
        print(f'{i + 1}: {s}')

def add_stakeholder():
    fname = get_letters('Enter the first name: ')
    lname = get_letters('Enter the first name: ')
    email = get_email('Enter the first name: ')
    role = get_letters('Enter the first name: ').capitalize()

    stakeholders.append(Stakeholder(fname, lname, email, role))

list_stakeholders()
add_stakeholder()
list_stakeholders()


        