import timeit
import random
import cProfile

MIN_ITEM = -100
MAX_ITEM = 100


def tow_min_1(lst):
    """
    Функция нахождния двух минимальных элементов в массиве
    из домашнего задание урока 3, 7 задача
    :param lst: list
    :return: tuple
    """
    if lst[0] < lst[1]:
        first_min_number, second_min_number = lst[0], lst[1]
    else:
        first_min_number, second_min_number = lst[1], lst[0]
    for i in range(2, len(lst)):
        if lst[i] <= first_min_number:
            second_min_number, first_min_number = first_min_number, lst[i]
        elif lst[i] < second_min_number:
            second_min_number = lst[i]
    return first_min_number, second_min_number


def tow_min_2(lst):
    """
    Функция нахождния двух минимальных элементов в массиве
    методом удаления из списка
    :param lst: list
    :return: tuple
    """
    first_min_number = min(lst)
    lst.remove(first_min_number)
    second_min_number = min(lst)
    return first_min_number, second_min_number


def tow_min_3(lst):
    """
    Функция нахождния двух минимальных элементов в массиве
    методом сортировки
    :param lst: list
    :return: tuple
    """
    lst = sorted(lst)
    return lst[0], lst[1]


# Будем проверять замеры производительности на разной длине массива
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(10)]
print(timeit.timeit(f"tow_min_1({array})", number=1000, globals=globals()))  # 0.0018097000000000252
print(timeit.timeit(f"tow_min_2({array})", number=1000, globals=globals()))  # 0.0012039000000000355
print(timeit.timeit(f"tow_min_3({array})", number=1000, globals=globals()))  # 0.0005682999999999661
print()
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(100)]
print(timeit.timeit(f"tow_min_1({array})", number=1000, globals=globals()))  # 0.013424299999999945
print(timeit.timeit(f"tow_min_2({array})", number=1000, globals=globals()))  # 0.007589599999999974
print(timeit.timeit(f"tow_min_3({array})", number=1000, globals=globals()))  # 0.003936700000000015
print()
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(500)]
print(timeit.timeit(f"tow_min_1({array})", number=1000, globals=globals()))  # 0.08210430000000002
print(timeit.timeit(f"tow_min_2({array})", number=1000, globals=globals()))  # 0.03801520000000003
print(timeit.timeit(f"tow_min_3({array})", number=1000, globals=globals()))  # 0.043664499999999995
print()
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(1000)]
print(timeit.timeit(f"tow_min_1({array})", number=1000, globals=globals()))  # 0.1656033
print(timeit.timeit(f"tow_min_2({array})", number=1000, globals=globals()))  # 0.061386800000000075
print(timeit.timeit(f"tow_min_3({array})", number=1000, globals=globals()))  # 0.10255869999999989
print()
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(10000)]
print(timeit.timeit(f"tow_min_1({array})", number=1000, globals=globals()))  # 1.7036109000000002
print(timeit.timeit(f"tow_min_2({array})", number=1000, globals=globals()))  # 0.5922765999999999
print(timeit.timeit(f"tow_min_3({array})", number=1000, globals=globals()))  # 1.2698109000000004
print()

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(100000)]
cProfile.run(f'tow_min_1({array})')
cProfile.run(f'tow_min_2({array})')
cProfile.run(f'tow_min_3({array})')


#          5 function calls in 0.246 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.018    0.018 <string>:1(<module>)
#         1    0.017    0.017    0.017    0.017 task_1.py:10(tow_min_1)
#         1    0.228    0.228    0.246    0.246 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          7 function calls in 0.236 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#         1    0.000    0.000    0.005    0.005 task_1.py:29(tow_min_2)
#         1    0.231    0.231    0.236    0.236 {built-in method builtins.exec}
#         2    0.005    0.003    0.005    0.003 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
#
#
#          5 function calls in 0.249 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.014    0.014 <string>:1(<module>)
#         1    0.000    0.000    0.013    0.013 task_1.py:42(tow_min_3)
#         1    0.235    0.235    0.249    0.249 {built-in method builtins.exec}
#         1    0.013    0.013    0.013    0.013 {built-in method builtins.sorted}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0

# Перва функция на основе прогонки всего массива конечно же работает медленее чем остальные две
# А вот результат второй и третий функции очень удивил, время исполнения третий функции на основе сортровки
# увеличеватся с ростом длинны массива, хотя на коротких массивах она показывает более быстрый результат
