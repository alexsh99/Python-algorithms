import random

SIZE = 10
MIN_ITEM = -20
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"исходный массив  {array}")

max_negative_element_pos = None  # Объявляем позицию отрицательного элемента как None (ну не знаем мы её)

for i, item in enumerate(array):
    if item < 0 and max_negative_element_pos is None:  # Запоминаем позицию первого повашего отрицательного элемента
        max_negative_element_pos = i
    elif 0 > item > array[max_negative_element_pos]:  # А дальше ищем самый максимальный из отрицательных
        max_negative_element_pos = i

if max_negative_element_pos is None:
    print("В исходном массиве нет отрицательных элементов")
else:
    print(f"максимальный отрицательный элемент: {array[max_negative_element_pos]}")
    print(f"на позиции: {max_negative_element_pos}")
