print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE, YEAR & SECTION: BSCOE 2-2")

# The program has an array variable containing 10 random numbers
array_ = [1, 4, 3, 4, 4, 5, 6, 2, 56, 200]

# Display the initial content of the array
print("\nArray: ", array_)


# Display a menu of options
def main():
    print("\nMenu:\n"
          "1 -> Add element\n2 -> Insert an element\n3 -> Modify an element\n"
          "4 -> Delete an element\n5 -> Arrange in ascending order\n6 -> Arrange in descending order\n"
          "7 -> Display array\n8 -> Exit")


# Display the resulting values of the array
def result():
    print("\nThis is the new Array: ", array_)


while True:
    main()
    try:
        # Allow user to select item in the menu (check if valid)
        choice = int(input("\nWhat do you want to do? (1-8): "))
    except ValueError:
        print("\nInvalid.")
    else:

        # Perform the selected option (you may prompt additional info to user when need)
        if choice == 1:
            add_element = str(input("\nEnter the element you want to add: "))
            if add_element.isdigit():
                int_add = int(add_element)
                array_.append(int_add)
            else:
                array_.append(add_element)
            result()

        elif choice == 2:
            ins_element1 = str(input("\nEnter the element you want to insert: "))
            try:
                ins_element2 = int(input("Enter index: "))
            except ValueError:
                print("\nInvalid.")
            else:
                if ins_element1.isdigit():
                    int_ins = int(ins_element1)
                    array_.insert(ins_element2, int_ins)
                else:
                    array_.insert(ins_element2, ins_element1)
                result()

        elif choice == 3:
            try:
                mod_element1 = int(input("\nEnter the index you want to modify: "))
                if mod_element1 not in array_:
                    raise ValueError
            except ValueError:
                print("\nInvalid.")
            else:
                mod_element2 = str(input("Enter the element you want to replace: "))
                if mod_element2.isdigit():
                    int_mod = int(mod_element2)
                    array_[mod_element1] = int_mod
                else:
                    array_[mod_element1] = mod_element2
                result()

        elif choice == 4:
            try:
                del_element = int(input("\nEnter the index you want to delete: "))
            except ValueError:
                print("\nInvalid.")
            else:
                del array_[del_element]
                print("\nThe element has been deleted.")
                result()

        elif choice == 5:
            array_.sort(key=lambda e: (isinstance(e, str), e))
            result()

        elif choice == 6:
            array_.sort(reverse=True, key=lambda e: (isinstance(e, str), e))
            result()

        # You may add other options and features
        elif choice == 7:
            print("\nArray:", array_)

        # You may add other options and features
        elif choice == 8:
            break

        else:
            print("\nInvalid.")
