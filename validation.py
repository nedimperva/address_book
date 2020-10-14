import re
 
 # function for inputing and validating name
def input_first_name():
    pattern = "[A-Z][a-z]+"
    print("""Enter your first name: (Name must start with capital letter)""",
          end=" ")
    temp = input()
    while (re.search(pattern, temp) == None):
        print("Please enter your name in required format:", end=" ")
        temp = input()
    return temp

# function for inputing and validating last name
def input_last_name():
    pattern = "[A-Z][a-z]+"
    print("""Enter your last name: (Name must start with capital letter)""",
          end=" ")
    temp = input()
    while (re.search(pattern, temp) == None):
        print("Please enter your last name in required format:", end=" ")
        temp = input()
    return temp

# function for validating number
def input_number():
    # number should look like this +387-62-111-000 or +387 62 111 000
    pattern = "\+\d\d\d(-|\s)\d\d(-|\s)\d\d\d(-|\s)\d\d\d"
    print("""Please enter the number in one of the following formats,
    (+387-62-111-000 or +387 62 111 000) ->""",
          end=" ")
    temp = input()
    while (re.search(pattern, temp) == None):
        print("Please enter your number in required format:", end=" ")
        temp = input()
    return temp


# function for validating email
def input_email():
    pattern = "[a-zA-Z0-9_.+]+@[a-zA-Z]+.(com|ba|gov|fit.ba)"
    print("""Please enter your email adress (example@email.com)""", end=" ")
    temp = input()
    while (re.search(pattern, temp) == None):
        print("Please enter your email in required format:", end=" ")
        temp = input()
    return temp

# function for validating adress
def input_adress():
    pattern = "[A-Z][a-z]+,\s[A-Z][a-z]+,\s\d\d\d\d\d"
    print("""Please enter your adress in the following format
    Street, Town, PostalCode""", end=" ")
    temp = input()
    while (re.search(pattern, temp) == None):
        print("Please enter your adress in required format:", end=" ")
        temp = input()
    return temp