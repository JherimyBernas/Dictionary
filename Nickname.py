print("\nProgrammed by: Jherimy Bernas\n")

# Printing my own nickname.
print("    * ***** *   * ")
print("    * *     ** ** ")
print("    * ****  * * * ")
print("*   * *     *   * ")
print(" ***  ***** *   * ")

# Input your nickname.
one = ["  *  ", "**** ", " *** ", "**** ", "*****", "*****", "*****", "*   *", "*****", "    *", "*   *", "*    ",
       "*   *", "*   *", " *** ", "**** ", " **  ", "**** ", "*****", "*****", "*   *", "*   *", "*   *", "*   *",
       "*   *", "*****"]

two = [" * * ", "*   *", "*   *", "*   *", "*    ", "*    ", "*    ", "*   *", "  *  ", "    *", "*  * ", "*    ",
       "** **", "**  *", "*   *", "*   *", "*  * ", "*   *", "*    ", "  *  ", "*   *", "*   *", "*   *", " * * ",
       " * * ", "   * "]

three = ["*****", "**** ", "*    ", "*   *", "**** ", "**** ", "*  **", "*****", "  *  ", "    *", "***  ", "*    ",
         "* * *", "* * *", "*   *", "**** ", "* ** ", "**** ", "*****", "  *  ", "*   *", "*   *", "* * *", "  *  ",
         "  *  ", "  *  "]

four = ["*   *", "*   *", "*   *", "*   *", "*    ", "*    ", "*   *", "*   *", "  *  ", "*   *", "*  * ", "*    ",
        "*   *", "*  **", "*   *", "*    ", "*  * ", "*  * ", "    *", "  *  ", "*   *", " * * ", "** **", " * * ",
        "  *  ", " *   "]

five = ["*   *", "**** ", " *** ", "**** ", "*****", "*    ", "*****", "*   *", "*****", " *** ", "*   *", "*****",
        "*   *", "*   *", " *** ", "*    ", " ** *", "*   *", "*****", "  *  ", " *** ", "  *  ", "*   *", "*   *",
        "  *  ", "*****"]

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
space = "   "

while True:
    try:
        nickname = input(str("\nnter Nickname: ")).upper()
        if nickname.isnumeric():
            raise ValueError
    except ValueError:
        print("\nInvalid.")
    else:
        line1 = []
        line2 = []
        line3 = []
        line4 = []
        line5 = []

        for i in nickname:
            if i.isspace():
                line1.append(space)
                line2.append(space)
                line3.append(space)
                line4.append(space)
                line5.append(space)

            else:
                index = letters.index(i)
                line1.append(one[index])
                line2.append(two[index])
                line3.append(three[index])
                line4.append(four[index])
                line5.append(five[index])

        print(*line1)
        print(*line2)
        print(*line3)
        print(*line4)
        print(*line5)

    try:
        run_again = int(input("\nRUN AGAIN?\n1. YES\n2. NO\n\nEnter choice: "))
        if run_again not in range(1, 3):
            raise ValueError
    except ValueError:
        print("\nInvalid")
        break
    else:
        if run_again == 1:
            continue
        else:
            print("\nThank you!")
            break
