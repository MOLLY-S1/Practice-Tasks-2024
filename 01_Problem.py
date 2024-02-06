num = int(input("Enter a four digit number:"))
length = len(str(num))

while True:

    if length == 3:
        num = f"0{num}"
        break

    elif length > 4:
        num = int(input("Enter a four digit number:"))
        length = len(str(num))

    elif length == 2:
        num = f"00{num}"
        break

    elif length == 1:
        num = f"000{num}"
        break


print(f"Your pin is {num}")
