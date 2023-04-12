# ===============================================  TASK 1  =============================================
def zero_func(num):
    print(num)
    if num > 0:
        zero_func(num-1)


zero_func(int(input("Enter number pls: ")))


# ===============================================  TASK 2  =============================================

lst = [0, 1]


def fibonacci(count):
    if count == 0:
        return 0
    if len(lst) < count+1:
        lst.append(lst[-1] + lst[-2])
        fibonacci(count)
    return lst[-1]


while True:
    choice = (int(input("Enter number: ")))
    if choice >= 0:
        fibonacci(choice)
        print(f"Number in list of Fibonacci - {fibonacci(choice)}")
        print(f"List of Fibonacci - {lst}")
        break
    else:
        print("Enter values greater than -1")


# ===============================================  TASK 3  =============================================

def factorial(number):
    if number <= 0:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(int(input("Enter number: "))))