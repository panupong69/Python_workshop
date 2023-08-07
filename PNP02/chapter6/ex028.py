def find_max_value(numbers):
    max_value = float('-inf')  # กำหนดค่าเริ่มต้นเป็นติดลบอนันต์ (negative infinity)
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

print(">>Program Find maximum Value<<\n")
num = int(input("Enter number of values (3-10): "))
num = max(3, min(10, num))

values = []
for i in range(num):
    value = int(input(f"Enter value Number #{i + 1}: "))
    values.append(value)

print(f"Your entered numbers: {', '.join(str(value) for value in values)}")
max_value = find_max_value(values)
print(f"Maximum value is {max_value}")

print("Exit Program")
