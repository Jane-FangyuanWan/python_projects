# Fangyuan Wan
# Generate triangular number list

def triangular_number(num):
    """
    Calculate triangular numbers
    """
    ONE = 1
    TWO = 2
    num = int(num)
    return (num * (num + ONE)) // TWO


def main():
    """
    Calculate triangular numbers and adds the
    corresponding triangular number to a list
    """
    tri_num_list = []
    num = input("Enter a number, or enter 'done': ")
    while num != "done":
        tri_number = triangular_number(num)
        print(f"The triangular number for {num} is {tri_number}")
        tri_num_list.append(tri_number)
        num = input("Enter another number, or enter 'done': ")
    print(tri_num_list)


main()
