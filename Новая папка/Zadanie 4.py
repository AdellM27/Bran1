strin = input("введите предложение ")
worl = []
number = 1

for element in range(strin.count(' ') + 1):
    worl = strin.split()
    if len(str(worl)) <= 10:
        print(f" {number} {worl[element]}")
        number += 1
    else:
        print(f" {number} {worl[element][0:10]}")
        number += 1
