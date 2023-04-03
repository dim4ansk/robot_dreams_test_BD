# ===============================================  TASK 1 =============================================

def exponentiation(num, st):
    return num**st


print(exponentiation(float(input("Enter num: ")), float(input("Enter power value: "))))


# ===============================================  TASK 2  =============================================

def super_sum(*args):
    return sum(args)


print(super_sum(45, 6, 23, -5.6, 7, 0))
