class cls:
    i = 3
number = cls()

number.i = number.i + 1

print(number.i)


class ArryList:
    j = [0, 1]
    i = 0


arr_list = ArryList()
arr_list.i, arr_list.j[arr_list.i] = 1, 2
print(arr_list.j)
