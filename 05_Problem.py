numbers = [20, 36, 12, 24, 20, 48, 74, 353, 23, 98]

num = int(input("Enter Number to change:"))

if num in numbers:
    change = int(input(f"Enter Number to change {num} to:"))
    place = numbers.index(num)
    numbers[place] = change

print(numbers)

