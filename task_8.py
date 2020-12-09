matrix = [[0] * 4 for i in range(5)]

for ind, row in enumerate(matrix):
    for i in range(len(row) - 1):
        matrix[ind][i] = int(input(f"Число: "))
        matrix[ind][len(row)-1] += matrix[ind][i]

print(matrix)
