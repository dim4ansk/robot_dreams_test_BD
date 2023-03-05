def func(a, b):
    return f" Your result {a+b}"

def func_2(x, y):
    return x*y


if __name__ == "__main__":
    print(func(int(input("Enter your first number: ")), int(input("Enter your second number: "))))
    print(func_2(2, 10))