a = int(input())

total = a
value = a

for i in range(a, 0, -1):
    output = ''
    for j in range(a, i - 1, -1):
        output += f'{j}'

    output += f'{j}' * (j - 1)
    print(output)