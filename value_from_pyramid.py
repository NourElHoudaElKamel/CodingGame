def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()


def decide_number(i, j):
    num = 1
    if j > i - j:
        j = i - j
    for k in range(0, j):
        num = num * (i - k)
        num = num // (k + 1)
    return num

# set rows
rows = 7
#print_pascal_triangle(rows)
print(decide_number(67, 34))