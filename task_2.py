import timeit
import matplotlib.pyplot as plt


def sieve(n):
    if n == 1:
        return 2
    a = [0] * n * n
    for i in range(len(a)):
        a[i] = i
    a[1] = 0
    m = 2
    while m < len(a):
        if a[m] != 0:
            j = m * 2
            while j < len(a):
                a[j] = 0
                j = j + m
        m += 1
    a = sorted(list(set(a)))
    return a[n]


def prime(n):
    a = []
    r = []
    i = 2
    while True:
        a.append(i)
        f = True
        for m in a:
            if i % m == 0 and i != m:
                f = False
        if f:
            r.append(i)
        if len(r) > (n - 1):
            break
        i += 1
    return r[n - 1]


x = [g for g in range(1, 10)]
y = []

for z in x:
    y.append(timeit.timeit(f"sieve({z})", number=100, globals=globals()))

plt.title("Зависимость времени от номера числа")  # заголовок
plt.xlabel("номер простого числа")  # ось абсцисс
plt.ylabel("время исполнения 100 замеров")  # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x, y)
plt.show()
