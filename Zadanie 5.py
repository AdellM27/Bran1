my_list = [7, 5, 3, 3, 2]
use = int(input("введите число"))

for el in range(len(my_list)):
    if my_list[el] == use:
        my_list.insert(el + 1, use)
        break
    elif my_list[0] < use:
        my_list.insert(0, use)
    elif my_list[-1] > use:
        my_list.append(use)
    elif my_list[el] > use and my_list[el + 1] < use:
        my_list.insert(el + 1, use)
print(my_list)
