import random

SIZE = 100
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"исходный массив {array}")

min_elem_pos, max_elem_pos = 0, 0  # Позиции минимального и максимального элемента

for i, item in enumerate(array):
    # Поиск позиции минимального элемента
    if array[min_elem_pos] > item:  # Если сравнение > то позиция первого найденого элемента, если >= то последнего
        min_elem_pos = i
    # Поиск позиции максимального элемента
    if array[max_elem_pos] < item:  # Если сравнение < то позиция первого найденого элемента, если <= то последнего
        max_elem_pos = i
# Для справки
print(f"Позиция первого минимального элемента: {min_elem_pos}")
print(f"Позиция первого максимального элемента: {max_elem_pos}")

array_for_sum = []
sum_number = 0

if min_elem_pos > max_elem_pos:
    array_for_sum = array[max_elem_pos + 1:min_elem_pos]
else:
    array_for_sum = array[min_elem_pos + 1:max_elem_pos]

if len(array_for_sum) > 0:
    print(f"Элменты для суммирования: {array_for_sum}")
    for val in array_for_sum:
        sum_number += val
    print(f"Сумма элементов между максимальным и минимальным элементом: {sum_number}")
else:
    print("Нет элементов для суммирования")
