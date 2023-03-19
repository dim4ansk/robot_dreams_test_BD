# ===============================================  TASK 3.1 =============================================
for num in range(1, 2):
    print(num)
    for num_2 in range(2, 3):
        print(num, num_2)
        for num_3 in range(3, 4):
            print(num, num_2, num_3)
            for num_4 in range(4, 5):
                print(num, num_2, num_3, num_4)
                for num_5 in range(5, 6):
                    print(num, num_2, num_3, num_4, num_5)


# ===============================================  TASK 3.2 =============================================

# Швидший спосіб

for num in range(1, 6):
    for num_i in range(1, num + 1):
        print(num_i, end=' ')  # end - розділяє кожен print не абзацом, а пробілом
    print()  # даний прінт після проходження першого циклу переносить ітерації на новий рядок
