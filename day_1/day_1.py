import math

lines = open('data.txt').readlines()

def first_part():
    table_1 = []
    table_2 = []
    response = 0

    for line in lines:
        numbers = line.split()
        table_1.append(int(numbers[0]))
        table_2.append(int(numbers[1]))
    
    table_1.sort()
    table_2.sort()

    for (x, y) in zip(table_1, table_2):
        response += int(math.dist([x], [y]))

    print(response)

def second_part():
    table_1 = []
    table_2 = []
    response = 0

    for line in lines:
        numbers = line.split()
        table_1.append(int(numbers[0]))
        table_2.append(int(numbers[1]))

    for num in table_1:
        response += int(num * table_2.count(num))

    print(response)

first_part()
second_part()