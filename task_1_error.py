
print("Hi. This is a phone book. \nIf you have a new friend and you want to communicate with him, "
      "you can save his contact. "
      "\nFollow the menu instructions and make corrections to the book. GLHF!\n")

print("1 - Add contact\n"
      "2 - Number of records\n"
      "3 - A list of all the names in the book\n"
      "4 - Contact's detailed information\n"
      "5 - Delete contact\n"
      "0 - Exit the program")


dict_contact = {}


def add():

    while True:
        name = str(input("Enter the person's name: "))
        number = input("Enter the person's number: ")
        if len(name) > 0 and number.isdigit() and len(number) == 10:
            if name in dict_contact:
                print("A contact with this name is already in your book!")
                break
            elif number in dict_contact.values():
                print("A contact with this number is already in your book!")
                break
            else:
                dict_contact[name] = number
                print("Done!")
                break
        else:
            print("The name or number entered is incorrect. Try again!\n")


def stats():
    if len(dict_contact) == 0:
        print('List is empty! Please add contacts!')
    else:
        print(f"You have {len(dict_contact)} contacts.")


def all_name_contacts():
    lst_na = [i for i in dict_contact.keys()]
    if len(lst_na) == 0:
        print('List is empty! Please add contacts!')
    else:
        for i, name in enumerate(lst_na):
            print(f"{i+1} - {name}")


def info():
    name_info = input("Enter name by which you want to find information: ")
    if name_info in dict_contact:
        print(f"Phone number of {name_info} - {dict_contact.get(name_info)}")
    else:
        print("No such contact exist. Enter another name or add to phone book!")


def delete():
    name_del = input("Enter name by which you want to delete contact: ")
    if name_del in dict_contact:
        dict_contact.pop(name_del)
        print(f"Contact {name_del} has been removed from the book")
    else:
        print("No such contact exist. Enter another name or add to phone book!")


def menu(num):
    try:
        num = int(num)
        if num == 1:
            add()
        elif num == 2:
            stats()
        elif num == 3:
            all_name_contacts()
        elif num == 4:
            info()
        elif num == 5:
            delete()
        elif num == 0:
            print("Bye!")
            return
        else:
            print("You can enter only numbers whose value is from 1 to 5 inclusive or 0 for exit. Try again!")
    except ValueError:
        print("Invalid input. Please enter a number.")


while True:
    try:
        choice = input("\nSelect a command by entering a number: ")
        print()
        if choice.isdigit() and 6 > int(choice) > 0:
            menu(int(choice))
        elif choice == "0":
            print("Bye!")
            break
        else:
            raise ValueError("You can enter only numbers whose value is from 1 to 5 include or 0 for exit.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("An error occurred:", e)