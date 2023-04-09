# ===============================================  TASK 1  =============================================

choice = int(input("Enter your choice (0 or 1): "))


def set_dupl(set_1, set_2):
    if choice == 0:
        return set_1 & set_2
    elif choice == 1:
        return set_1 ^ set_2


print(set_dupl({1, 2, 4, 'f'}, {1, 2, 6, 8, 'f'}))
