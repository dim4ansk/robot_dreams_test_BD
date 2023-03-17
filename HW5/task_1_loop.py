# ===============================================  TASK 1 =============================================

text = input("Enter something pls: ")

for word in text:
    if word.isdigit():
        if int(word) % 2:
            print(f"This symbol '{word}' - odd number")
        else:
            print(f"This symbol '{word}' - even number")
    elif word.isalpha():
        if word == word.lower():
            print(f"This symbol '{word}' - lower letter")
        else:
            print(f"This symbol '{word}' - upper letter")
    else:
        print(f"This symbol '{word}' does not apply to letters or numbers")
