import random

SIZE_M = 5
SIZE_N = 5
MIN_ITEM = -10
MAX_ITEM = 10
array = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)] for _ in range(SIZE_M)]
print(f"исходная матрица {array}")

for line in array:
    print(line)

# Создадим массив по количеству столбцов в матрице и копируем значения первой линии

min_col_el = array[0].copy()

for line in array:
    for i, item in enumerate(line):
        if item < min_col_el[i]:
            min_col_el[i] = item

max_in_min = min_col_el[0]

for m in min_col_el:
    if m > max_in_min:
        max_in_min = m

print(f"максимальный элемент среди минимальных элементов столбцов: {max_in_min}")
