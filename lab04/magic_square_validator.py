def is_magic_square(magic_square):
    CORRECT_SUM = 15
    INPUT_NUMBERS = 3
    for i in range(INPUT_NUMBERS):
        if sum(magic_square[i]) != CORRECT_SUM:
            return False

        column_sum = sum(magic_square[j][i]for j in range(INPUT_NUMBERS))
        if column_sum != CORRECT_SUM:
            return False

    diagnoal_left = sum(magic_square[i][i]for i in range(INPUT_NUMBERS))
    diagnoal_rigt = sum(magic_square[i][INPUT_NUMBERS-1-i]
                        for i in range(INPUT_NUMBERS))

    if diagnoal_left != CORRECT_SUM or diagnoal_rigt != CORRECT_SUM:
        return False

    return True


def main():
    magic_square = []
    print("Enter a magic number")

    for _ in range(3):
        row = input()
    # convert the input row to a list of integers
        row = [int(char) for char in row]
        magic_square.append(row)

    if is_magic_square(magic_square):
        print("This is a magic square!")
    else:
        print("Not a magic square!")


main()
