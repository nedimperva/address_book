import csv
from validation import input_first_name,input_last_name,input_adress,input_email,input_number

#Shows main menu
def show_menu():
    """Function to print menu on screen, and promts for input"""
    
    print("""Please choose one of the options below:
    1. Add contact
    2. Delete contact
    3. Search
    4. Edit contact
    5. View all contacts
    6. Exit from program
    Enter choice: """, end = " ")
    
def add_contact(columns):
    """Function that adds new contact"""
    
    #Prompt user for information
    print("Enter information")
    name = input_first_name()
    last = input_last_name()
    address = input_adress()
    number = input_number()
    email = input_email()
            
    #Add new row to csv 
    with open('book.csv','a') as filename:
        writer = csv.DictWriter(filename,fieldnames=columns)
        writer.writerow(
            {
                'Name' : name,
                'Last_Name' : last,
                'Address' : address,
                'Number' : number,
                'Email' : email
                }
            )
        filename.close()

def delete_contact(columns):
    """Function to search for and delete a contact"""
    
    #Prompt user to enter first and last name of contact to delete
    search_first_name = input_first_name()
    search_last_name = input_last_name()
    temp_contacts = []
    
    #Search through existing csv, copy contacts, if match found do not copy
    with open('book.csv','r') as filename:
        reader = csv.DictReader(filename)
        for row in reader:
            row_first_name = row["Name"]
            row_last_name = row["Last_Name"]
            row_address = row["Address"]
            row_phone = row["Number"]
            row_email = row["Email"]
            #new dict variable to copy to list
            move_contact = {
                "Name":row_first_name,
                "Last_Name":row_last_name,
                "Address":row_address,
                "Number":row_phone,
                "Email":row_email
            }
            #if match found, skip copying, or else add existing contact to list
            if (search_first_name == row_first_name) and (search_last_name == row_last_name):
                pass
            else:
                temp_contacts.append(dict(move_contact))
        filename.close()

    
    #Overwrite contacts from list back to new csv
    with open('book.csv', 'w') as filename:
            writer = csv.DictWriter(filename,fieldnames = columns)
            writer.writeheader()
            for item in temp_contacts:
                writer.writerow(dict(item))
            filename.close()
            
def search_contact():
    """Function to search and print contacts"""
    
    #Prompt user for choice, search by name or number
    print("""Choose search by: ""
                1. Name
                2. Number""")
    found=False
    search_choice = 0
    search_choice = int(input())
    
    #Search by first and last name
    if search_choice == 1:
        search_first_name = input_first_name()
        search_last_name = input_last_name()
            
        with open('book.csv','r') as filename:
            reader = csv.DictReader(filename)
            for row in reader:
                row_first_name = row["Name"]
                row_last_name = row["Last_Name"]
                if (search_first_name == row_first_name) and (search_last_name == row_last_name):
                    print("Search found!")
                    found = True
                    print(row)
            filename.close()
    
    #Search by number              
    elif search_choice == 2:
        print("Enter phone number: ")
        number = int(input())
                
        with open('book.csv','r') as filename:
            reader = csv.DictReader(filename)
            for row in reader:
                row_number = int(row["Number"])
                if number == row_number:
                    print("Search found!")
                    found = True
                    print(row)
            filename.close()
    
    if found == False:
        print("No results found!")
    
def edit_conact(columns):
    search_first_name = input_first_name()
    search_last_name = input_last_name()
    temp_contacts = []
    found = False
    
    with open('book.csv','r') as filename:
        reader = csv.DictReader(filename)
        for row in reader:
            row_first_name = row["Name"]
            row_last_name = row["Last_Name"]
            if (search_first_name == row_first_name) and (search_last_name == row_last_name):
                found = True  
        filename.close()
    
    if found == True:
        with open('book.csv','r') as filename:
            reader = csv.DictReader(filename)
            for row in reader:
                row_first_name = row["Name"]
                row_last_name = row["Last_Name"]
                row_address = row["Address"]
                row_phone = row["Number"]
                row_email = row["Email"]
                if search_first_name == row_first_name and search_last_name == row_last_name:
                    print("Enter new information: ")
                    new_first_name=input_first_name()
                    new_last_name=input_last_name()
                    new_address=input_adress()
                    new_phone=input_number()
                    new_email=input_email()
                    edited_contact= {
                        "Name":new_first_name,
                        "Last_Name":new_last_name,
                        "Address":new_address,
                        "Number":new_phone,
                        "Email":new_email
                    }
                    temp_contacts.append(dict(edited_contact))
                else:
                    move_contact = {
                        "Name":row_first_name,
                        "Last_Name":row_last_name,
                        "Address":row_address,
                        "Number":row_phone,
                        "Email":row_email
                    }
                    temp_contacts.append(dict(move_contact))
            filename.close()
        
        with open('book.csv', 'w') as filename:
            writer = csv.DictWriter(filename,fieldnames = columns)
            writer.writeheader()
            for item in temp_contacts:
                writer.writerow(dict(item))
        filename.close()
    else:
        print("Contact not found!")
          

def view_all_contacts():
    """Function to show all existing contacts"""
    with open('book.csv', 'r') as filename:
            reader = csv.DictReader(filename)
            for row in reader:
                print(row)
            filename.close()
