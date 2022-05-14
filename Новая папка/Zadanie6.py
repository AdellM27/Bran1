products = []

n = int(input("введите число товаров"))

for i in range(1, n + 1):
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    unit = input('Введите единицу измерения товара: ')

    params = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'unit': unit
    }

    products.append((i, params))

print(products)


products1 = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

analitics = {}

for i, product in products1:
    for k, v in product.items():
        if analitics.get(k) == None:
            analitics[k] = []
        analitics[k].append(v)

for k in analitics.keys():
    analitics[k] = list(set(analitics[k]))

print(analitics)
