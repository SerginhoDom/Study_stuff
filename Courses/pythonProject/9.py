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

print(len(set(map(lambda x: tuple(x), matrix))))
