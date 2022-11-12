

# Display a menu of options.
def menu():
    print("\nMenu:\n1 -> Add an item\n2. -> Search\n3. -> Exit")


dictionary = {}

while True:
    menu()
    try:
        choice = int(input("\nWhat do you want to do? (1-3): "))
    except ValueError:
        print("\nInvalid.")
    else:
        if choice == 1:
            name = str(input("\nFull name: "))
            try:
                age = int(input("Age: "))
                contact = int(input("Phone Number: "))
            except ValueError:
                print("\nInvalid.")
            else:
                address = str(input("Address: "))
                dictionary[name] = {"Age:": age, "Contact:": contact, "Address": address}
                print("\nSaved.")

        elif choice == 2:
            search = str(input("Enter full name: "))
            if search in dictionary:
                print("\nFull name:", search)
                for key, value in dictionary[search].items():
                    print(key + ":", value)
