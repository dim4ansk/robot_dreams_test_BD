# ===============================================  TASK 1-2-3 =============================================

value = input("Enter something pls: ")

if value.isalpha():
    print(f"Your text '{value}' is a word. And its length is {len(value)}")
elif value.isdigit():
    print(f"Your {value} is a number")
    if int(value) % 2 == 0:
        print("This value is even")
    else:
        print("This value is odd")
else:
    print(f"'{value}' is a mixed text")
