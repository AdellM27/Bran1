pribl = int(input('Введите значение прибыли: '))
izdergki = int(input('Введите значение издержек: '))
cotrudniki = int(input('Ввдите количество работников: '))
if pribl > izdergki:
    print('Выручка больше издержек')
    clear_pribl = pribl - izdergki
rent = clear_pribl / pribl
print('Рентабельность {} выручки {}: {:.2f}'.format('нашей', 'составила', rent))
clear_for_person = float(clear_pribl / cotrudniki)
print('Прибыль фирмы в расчете на одного сотрудника: %s' % clear_for_person)
