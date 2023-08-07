def find_max(num):
    max_digit = 0
    num_str = str(abs(num))

    for digit in num_str:
        max_digit = max(max_digit, int(digit))

    return max_digit

while True:
    input_number = int(input("Enter integer number (0 to exit):"))
    if input_number == 0:
        print("Exit program")
        break

    max_digit = find_max(input_number)
    print(f"Max gidit of {input_number} = {max_digit}")

