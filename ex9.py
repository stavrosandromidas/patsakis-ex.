#function gia na prosthetei ta pshfia tou aritmou
def sum_digits(num):
    s = num
    x = 0
    while s > 0:
        x = s % 10
        s = s // 10
    return x

number = int(input("ΔΩΣΕ ΕΝΑΝ ΑΡΙΘΜΟ: "))
number = number * 3
number += 1
number = sum_digits(number)
while not (0 < number <= 9):
    number = number * 3
    number += 1
    number = sum_digits(number)

print(number)



