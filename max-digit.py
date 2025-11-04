num = int(input("Enter an integer:"))
if num == 0:
    max_digit = 0
else:
    max_digit = -1
temp = num
while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
        temp = temp // 10
        print(f"Bigger digit: {max_digit}")