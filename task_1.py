array_multiples = [0] * 8  # массив с посчетом кратности

for i in range(2, 100):  # перебираем диапозон от 2 до 99 включительно
    for n, m in enumerate(range(2, 10)):  # Перебираем диапозон от 2 до 9 включительно, но с индексом
        if i % m == 0:
            array_multiples[n] += 1

# Красивый вывод
print("В диапазоне натуральных чисел от 2 до 99")
for ind, item in enumerate(range(2, 10)):
    print(f"число {item} кратно {array_multiples[ind]} раз(а)")
