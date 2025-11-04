num = int(input("Enter an integer:"))
max_digit = 0
while num > 0:
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
        num = num // 10
        print(f"Bigger digit: {max_digit}")