# ===============================================  TASK 3 =============================================
import numpy as np

lst = np.random.randint(-5, 10, 10)  # використав бібліотеку "numpy" для створення рандомного масиву
print(lst)


def max_num(lst_):
    m_count = lst_[0]
    for elem in lst_:
        if elem > m_count:
            m_count = elem
    return m_count


max_l = lambda lst_l: max_num(lst_l)

print(max(lst))  # - built-in функція

print(max_num(lst))  # - власна функція

print(max_l(lst))  # - анонімна функція
