a = int(input("Сторона a: "))
b = int(input("Сторона b: "))
c = int(input("Сторона c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Треугольник равносторонний")
    elif (a == b) or (a == c) or (b == c):
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольник не собрать")
