# Brandon Knorr
# Module 5 Assignment - Employee Manager
# Uses dictionaries, regex validation, and classes

from input_helper import get_int_in_range, get_letters, get_username, get_valid_email

# Job titles and descriptions dictionary
# Sources:
# - Account Manager: https://www.indeed.com/hire/job-description/account-manager
# - Project Manager: https://www.indeed.com/hire/job-description/project-manager
# - Senior Developer: https://www.indeed.com/hire/job-description/senior-software-engineer
# - Junior Developer: https://www.indeed.com/hire/job-description/junior-software-developer
JOB_DESCRIPTIONS = {
    "Account Manager": "Responsible for communicating with clients and conveying their needs to the project manager",
    "Project Manager": "Manages the time of the developers to make sure client needs are fulfilled",
    "Senior Developer": "Oversees the work done by junior developers and works on difficult problems",
    "Junior Developer": "Works at the direction of the senior developer and project manager"
}


class Employee:
    
    def __init__(self, firstname, lastname, username, email, job_title):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.job_title = job_title
    
    def __str__(self):
        job_desc = self.get_job_description()
        return f"{self.job_title} | {self.lastname}, {self.firstname} | {self.email} | {self.username}\n\t{job_desc}"
    
    def get_job_description(self):
        """Returns the job description for the employee's job title"""
        return JOB_DESCRIPTIONS.get(self.job_title, "No description available")


employees = [
    Employee("Aragorn", "Arathorn", "aragor1234", "agor@mtirith.com", "Senior Developer"),
    Employee("Arwen", "Undomiel", "arwenu3423", "arwenun@rivend.com", "Account Manager"),
    Employee("Gimli", "Durin", "gdurin9191", "gdurin9191@gcaves.com", "Project Manager")
]


def display_menu():
    print("\n====Employee Manager====")
    print("\t1. List Employees")
    print("\t2. Add Employee")
    print("\t3. Remove Employee")
    print("\t4. List Jobs")
    print("\t5. Exit")


def list_employees():
    if not employees:
        print("No employees to display.")
        return
    
    for i, emp in enumerate(employees, 1):
        print(f"{i}. {emp}")


def add_employee():
    firstname = get_letters("Enter a first name: ")
    lastname = get_letters("Enter a last name: ")
    email = get_valid_email("Enter an email: ")
    username = get_username("Enter a username: ")
    
    print("Available job titles:")
    job_titles = list(JOB_DESCRIPTIONS.keys())
    for i, title in enumerate(job_titles, 1):
        print(f"\t{i}. {title}")
    
    selection = get_int_in_range("Select a job title: ", 1, len(job_titles))
    job_title = job_titles[selection - 1]
    
    new_employee = Employee(firstname, lastname, username, email, job_title)
    employees.append(new_employee)
    print(f"\n{firstname} {lastname} has been added as a {job_title}.")


def remove_employee():
    if not employees:
        print("No employees to remove.")
        return
    
    list_employees()
    selection = get_int_in_range("Which employee do you want to remove: ", 1, len(employees))
    removed = employees.pop(selection - 1)
    print(f"\n{removed.firstname} {removed.lastname} has been removed.")


def list_jobs():
    for title, description in JOB_DESCRIPTIONS.items():
        print(f"{title}")
        print(f"\t{description}")


def main():
    while True:
        display_menu()
        selection = get_int_in_range("Selection: ", 1, 5)
        
        if selection == 1:
            list_employees()
        elif selection == 2:
            add_employee()
        elif selection == 3:
            remove_employee()
        elif selection == 4:
            list_jobs()
        elif selection == 5:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
