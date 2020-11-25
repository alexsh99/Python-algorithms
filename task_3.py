x1 = float(input("Координата x1: "))
y1 = float(input("Координата y1: "))
x2 = float(input("Координата x2: "))
y2 = float(input("Координата y2: "))

if x1 == x2:
    print("прямая параллельна оси Х")
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f"уравнение прямой y = {k:.2f} * x + {b:.2f}")
