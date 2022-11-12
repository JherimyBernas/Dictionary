# Write a python program for contact tracing:
print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE, YR. & SECTION: BSCOE 2-2")


# Display a menu of options.
def menu():
    print("\nMenu:\n1. -> Add an item\n2. -> Search\n3. -> Contacts\n4. -> Exit")


dictionary = {}

while True:
    menu()
    try:
        # Allow user to select item in the menu.
        choice = int(input("\nWhat do you want to do? (1-4): "))
    except ValueError:
        print("\nInvalid.")
    else:
        # Perform the selected option.

        # Ask personal data for contact tracing.
        if choice == 1:
            name = str(input("\nFull name: "))
            try:
                age = int(input("Age: "))
                contact = int(input("Phone Number: "))
            except ValueError:
                print("\nInvalid.")
            else:
                address = str(input("Address: "))
                dictionary[name] = {"Age:": age, "Contact:": contact, "Address:": address}
                print("\nSaved.")

        # Search, ask full name then display the record.
        elif choice == 2:
            search = str(input("Enter full name: "))
            if search in dictionary:
                print("\nFull name:", search)
                for key, value in dictionary[search].items():
                    print(key, value)
            else:
                print("\nInvalid.")

        # Display contacts.
        elif choice == 3:
            print("\nContacts:\n")
            for i in dictionary:
                print("     Full name:", i)
                for key, value in dictionary[i].items():
                    print("    ", key, value)
                print()

        # Exit.
        elif choice == 4:
            break

        else:
            print("\nInvalid.")
