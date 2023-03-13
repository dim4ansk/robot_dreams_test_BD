# ===============================================  TASK 2 and 3 =============================================

age_in_years = int(input('Enter your age: '))
age_in_month = age_in_years * 12
print("Your age in months", age_in_month)


# ===============================================  TASK 4 =============================================

name = input("Enter your name: ")
my_age = "Му name is " + name + " I’m " + str(age_in_years) + " years old"
print(my_age)

# option with f-string
print(f"Му name is {name} I’m {age_in_years} years old")