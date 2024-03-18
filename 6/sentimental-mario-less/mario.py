# TODO
# import cs50

from cs50 import get_int

# n = 0
# while n < 1 or n > 8:
# n = cs50.get_int("Height: ")
# for i in range(1, n+1, 1):

# pilnais pieraksts - 1 ... n
# for i in range(n):
# 0...n-1

while True:
    n = get_int("Height: ")
    if n > 0 and n < 9:
        break

for i in range(0, n, 1):
    for j in range(0, n, 1):
        if i + j < n - 1:
            print(" ", end="")
        else:
            print("#", end="")
    print()
