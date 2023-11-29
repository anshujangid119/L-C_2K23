def kaprekar_iterations(num):
    steps = 0
    while num != 6174:
        desc_num = sort_digits_descending(num)
        asc_num = sort_digits_ascending(num)
        num = desc_num - asc_num
        steps += 1
    return steps

def sort_digits_descending(num):
    digits = list(str(num))
    for i in range(len(digits)):
        for j in range(0, len(digits)-i-1):
            if digits[j] < digits[j+1]:
                digits[j], digits[j+1] = digits[j+1], digits[j]
    return int(''.join(digits))

def sort_digits_ascending(num):
    digits = list(str(num))
    for i in range(len(digits)):
        for j in range(0, len(digits)-i-1):
            if digits[j] > digits[j+1]:
                digits[j], digits[j+1] = digits[j+1], digits[j]
    return int(''.join(digits))

def is_valid_input(num_str):
    return 1000 <= int(num_str) <= 9999 and len(set(num_str)) >= 3 and num_str.count('0') <= 11

def get_number():
    try:
        number = int(input("Enter a 4-digit number: "))
        num_str = str(number)
        if not is_valid_input(num_str):
            print("Please enter a valid 4-digit number with at least 3 distinct digits and only one zero.")
            return None

        return number

    except ValueError:
        print("Invalid input. Please enter a valid 4-digit number.")
        return None

def main():
    number = get_number()
    if number is not None:
        # Calculate Kaprekar's iterations
        steps = kaprekar_iterations(number)
        largest_num = sort_digits_descending(number)
        smallest_num = sort_digits_ascending(number)
        print(f"\nReached Kaprekar's Constant (6174) in {steps} steps.")

if __name__ == "__main__":
    main()
