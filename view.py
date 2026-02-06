from contact_book import create_table, add_contact,list_contacts, search_contacts, update_contact, delete_contact
def menu():
    print("""
          Contact Book
          1. Add Contact
          2. List Contact
          3. Search Contact
          4. Update Contact
          5. Delete Contact
          6. Exit
          """)

def main():
    create_table()
    
    while True:
        menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            print("Provide following info: ")
            name = input("Contact Name: ")
            email = input("Contact Email: ")
            phone = input("Contact Phone: ")
            add_contact(name,email,phone)

        elif choice == "2":
            list_contacts()
            
        elif choice == "3":
            user_input = input("Search by name or email: ")
            search_contacts(user_input)
            
        elif choice == "4":
            contact_id = input("Enter the contact id: ")
            contact_name = input("Updated Name: ")
            contact_email = input("Updated Email: ")
            contact_phone = input("Updated Phone: ")
            update_contact(contact_id, contact_name, contact_email, contact_phone)
        
        elif choice == "5":
            contact_id = input("Enter the contact id: ")
            delete_contact(contact_id)
        
        elif choice == "6":
            print("Good Bye...")
        
        else:
            print("Invalid Choice!")
            break

if __name__ == "__main__":
    main()
