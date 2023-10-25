# Fangyuan Wan
# Primary arithmetic

def integer_to_list(num):
    """
    Convert intergers to list
    """
    return [int(digit) for digit in str(num)]


def count_carries(num1, num2):
    """
    Add integers together
    """
    num1_digits = integer_to_list(num1)
    num2_digits = integer_to_list(num2)

    max_length = max(len(num1_digits), len(num2_digits))
    num1_digits = [0]*(max_length - len(num1_digits)) + num1_digits
    num2_digits = [0]*(max_length - len(num2_digits)) + num2_digits

    carry_count = 0
    carry = 0

    for i in range(max_length-1, -1, -1):
        digit_sum = num1_digits[i] + num2_digits[i] + carry
        if digit_sum >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0
    return carry_count


def main():
    """
    prompts the user for two positive integers
    of any length and adds them together.
    """
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 + num2
    carry_count = count_carries(num1, num2)

    print(f"{num1} + {num2} = {result}")
    print(f"Number of carries: {carry_count}")


if __name__ == "__main__":
    main()
