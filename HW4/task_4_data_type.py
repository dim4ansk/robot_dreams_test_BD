# ===============================================  TASK 4 =============================================

value = input("Enter something pls: ")

match value:
    case value if value.isdigit():
        print(f"Your value is of type int")
    case value if value.isalpha():
        print(f"Your value is of type str")
    case value if isinstance(float(value), float):
        print(f"Your value is of type float")

