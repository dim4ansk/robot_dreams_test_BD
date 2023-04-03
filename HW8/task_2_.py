# ===============================================  TASK 2 =============================================

lst = [1, 2, 3, 'Hello', 22.5, 'i love', 10, 'python']


def up(elem):
    if type(elem) == str:
        elem = elem.upper()
    return elem


new_lst = list(map(up, lst))
print(new_lst)


# ===============================================  TASK 3 =============================================

result = list(filter(lambda x: type(x) == int, lst))

print(result)
