import sys


def main():
    '''
    Takes a value and generates fibonacci numbers
    '''
    try:
        n = int(sys.argv[1])
        if n >= 0:
            fibonacci_numbers = cal_fibonacci_numbers(n)
            print(f"The first {n} fibonacci numbers are: {fibonacci_numbers} ")
    except ValueError:
        print("Please enter a vaild integer")


def cal_fibonacci_numbers(n):
    '''
    Calculate fibonacci numbers
    '''
    fibonacci_list = [0, 1]
    while len(fibonacci_list) < n:
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)
    return fibonacci_list


main()
