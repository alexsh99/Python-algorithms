import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f"исходный массив  {array}")

freq_dict = dict.fromkeys(array, 0)  # Создаем словарь с ключами из элементов массива и значением 0

# итерируем array и считаем кол-во
for item in array:
    freq_dict[item] += 1

max_freq_number = array[0]  # Пусть первым часто встречающимся числом будет первый элемент array

# Пробежим по словарю и найдем самый максимальный элемент
for item in freq_dict:
    if freq_dict[item] > freq_dict[max_freq_number]:
        max_freq_number = item  # Ключ элемента в словаре и будет самым частым числом в array

print(f"Число {max_freq_number} встречается чаще всего")
