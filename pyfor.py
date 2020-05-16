for item in range(5, 10):
    print(item)

prices = [10, 20, 30]
total = 0

for price in prices:
    total += price
print(f"total :{total}")


for x in range(4):
    for y in range(3):
        print(f'({x},{y})')


numbers = [10, 3, 6, 2, 8, 4]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)
