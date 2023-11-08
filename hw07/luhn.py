# Fangyuan Wan
# Luhn's algorithm

def modify_digits(nums):
    """
    Determines whether or not the number
    is valid using Luhn’s algorithm.
    """
    digits = [int(digit) for digit in str(nums)]

    for i in range(len(digits)-2, -1, -2):
        doubled = digits[i] * 2
        if doubled >= 10:
            digits[i] = doubled//10 + doubled % 10
        else:
            digits[i] = doubled

    total = sum(digits)
    print(total)

    if total % 10 == 0:
        print(f"{nums} is vaild")
    else:
        print(f"{nums} is not vaild")


def main():
    """
    Asks for an account number and calls the function
    """
    nums = input("Enter an account number: ")

    modify_digits(nums)


main()
