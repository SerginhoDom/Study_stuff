def sum_blocks(matrix, k):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    result = []

    for i in range(0, rows, k):
        result_row = []
        for j in range(0, cols, k):
            block_sum = 0

            # Считаем сумму элементов в текущем блоке
            for m in range(k):
                for n in range(k):
                    if i + m < rows and j + n < cols:
                        block_sum += matrix[i + m][j + n]

            result_row.append(block_sum)

        result.append(result_row)

    return result


k = int(input().strip())

matrix = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        row = list(map(int, line.split()))
        matrix.append(row)
    except EOFError:
        break

result = sum_blocks(matrix, k)

for row in result:
    print(" ".join(map(str, row)))