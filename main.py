import csv
import os.path
import functions

print("Welcome to AddressBook!")

#set initial column names
columns = ["Name", "Last_Name", "Address","Number","Email"]

#check to see if file already exists, if not, write header
if os.path.isfile('./book.csv') == False:
    with open("book.csv","a") as filename:
        writer = csv.DictWriter(filename,fieldnames=columns)
        writer.writeheader()
        filename.close()

#switch users choice, until he exits from program 
choice = 0
while choice != 6:
    
    #Show menu options
    functions.show_menu()
    
    #Promt user for choice
    choice = int(input())
    try:
        while choice < 1 or choice > 6:
            print("Pleas enter valid option:", end=" ")
            choice = int(input())
    except ValueError:
        print("Enter a number!")
    
    #Add contact
    if choice == 1:
        functions.add_contact(columns)
        print("Contact Added!")
    
    #Delete contact
    elif choice ==2:
        functions.delete_contact(columns)
        print("Contact deleted!")
        
    #Search contact
    elif choice==3:
        functions.search_contact()
    
    #Edit contact
    elif choice==4:
        functions.edit_conact(columns)
        print("Contact edited!")
    
    #View all contacts
    elif choice ==5:
        functions.view_all_contacts()
            
    #Exit program
    elif choice == 6:
        pass