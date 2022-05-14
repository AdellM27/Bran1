new_dict = {"1": "zima", "2": "vesna", "3": "leto", "4": "osen"}
new_list1 = ["zima", "vesna", "leto", "osen"]

use = int(input("Введите месяц"))

if use == 1 or use == 2 or use == 12:
    print(new_list1[0])
elif use == 3 or use == 4 or use == 5:
    print(new_list1[1])
elif use == 6 or use == 7 or use == 8:
    print(new_list1[2])
elif use == 9 or use == 10 or use == 11:
    print(new_list1[3])
elif use > 12:
    print("Ошибка")
