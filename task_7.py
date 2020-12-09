import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"исходный массив {array}")

# Будем считать что первое число и есть минимальное
first_min_number = array[0]
second_min_number = array[0]

for i in array:
    if i <= first_min_number:
        second_min_number, first_min_number = first_min_number, i
    elif i < second_min_number:
        second_min_number = i

print(f"Первое минимальное число: {first_min_number}\nвторое минимальное число: {second_min_number}")
