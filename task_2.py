import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
even_array = []

print(f"исходный массив {array}")

for i, item in enumerate(array):
    if item % 2 == 0:
        even_array.append(i)

print(f"индексы четных элементов {even_array}")
