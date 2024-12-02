import math

lines = open('data.txt').readlines()

table_1 = []
table_2 = []

for line in lines:
    numbers = line.split()
    table_1.append(int(numbers[0]))
    table_2.append(int(numbers[1]))

table_1.sort()
table_2.sort()

def first_part():
    response = 0

    for (x, y) in zip(table_1, table_2):
        response += int(math.dist([x], [y]))

    print(response)

def second_part():
    response = 0

    for num in table_1:
        response += int(num * table_2.count(num))

    print(response)

first_part()
second_part()