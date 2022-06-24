"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
 преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
  и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, day_month_yaer):
        self.day_month_yaer = str(day_month_yaer)

    @classmethod
    def my_method(cls, day_month_yaer):
        time = []

        for i in day_month_yaer.split():
            if i != "_": time.append(i)
            return int(time[0]), int(time[1]), int(time[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Ok'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Date.my_method(self.day_month_yaer)}'


today = Date('22_02_2022')
print(Date.valid(11, 11, 2022))
print(Date.valid(11, 3, 2022))
print(Date.valid(1, 11, 2000))

"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
 вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
  ситуацию и не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        user_num_1 = int(input('Введите делимое: '))
        user_num_2 = int(input('Введите делитель: '))
        if user_num_2 == 0:
            raise OwnError("Делить на ноль нельзя!")
        else:
            res = user_num_1 / user_num_2
            return res
    except ValueError:
        return "Вы ввели не число"
    except OwnError as err:
        return err


print(div())

"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список 
только числами. Класс-исключение должен контролировать типы данных элементов списка.
"""


class MyError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input('Введите числа: '))
                    ex = input(f'добавляем "{user_val}" в список. Хотите продолжить? y/n: ').lower()
                    self.my_list.append(user_val)
                    if ex == 'n':
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                ex = input(f"Вы ввели не число! ").lower()
            else:
                self.check_value()


a = TypeCheck()
a.check_value()

"""
4.5.6:
"""


class OfficeEquipment:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def income(self):
        try:
            name = input(f'Введите наименование: ')
            price = int(input(f'Введите цену за ед: '))
            quantity = int(input(f'Введите количество: '))
            item = {'Модель устройства': name, 'Цена за ед': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Недопустимое значение!')


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


p = Printer('Hp', 2, 300)
s = Scanner('Canon', 54000, 10)
x = Xerox('Xerox', 7000, 15)
p.income()
s.income()
x.income()

"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку 
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные 
числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата. """


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


c_1 = ComplexNumber(4, -8)
c_2 = ComplexNumber(6, 11)
print(c_1 + c_2)
print(c_1 * c_2)
