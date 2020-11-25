# файл
# https://drive.google.com/file/d/1sGvsGy1hDJsBVwKLfxdac9S-PQhfyTds/view?usp=sharing
n = int(input("Введите трёхзначное число: "))
d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100

print(f"Сумма цифр числа {n} равна {d1 + d2 + d3}")
print(f"Произведение цифр числа {n} равно {d1 * d2 * d3}")
