import sys
x = sys.stdin.readline()
a = list(x)
c = 0
if ord(a[0]) + 2 <= ord('h'):
    if int(a[1]) - 1 >= 1:
        c += 1
    if int(a[1]) + 1 <= 8:
        c += 1
if ord(a[0]) - 2 >= ord('a'):
    if int(a[1]) - 1 >= 1:
        c += 1
    if int(a[1]) + 1 <= 8:
        c += 1
if int(a[1]) + 2 <= 8:
    if ord(a[0]) - 1 >= ord('a'):
        c += 1
    if ord(a[0]) + 1 <= ord('h'):
        c += 1
if int(a[1]) - 2 >= 1:
    if ord(a[0]) - 1 >= ord('a'):
        c += 1
    if ord(a[0]) + 1 <= ord('h'):
        c += 1
print(c)

#===================================================
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]) - int(ord('a'))) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)