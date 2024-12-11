n, m = map(int, input().split())

result = []
i = 1
while True:
    result.append(i)
    i = 1 + (i + m - 2) % n
    if i == 1:
        break

print("".join(map(str, result)))
