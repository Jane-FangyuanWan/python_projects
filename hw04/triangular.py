import sys


def main():
    '''
    Takes a number as an argument when the program is
    run and prints out the "triangular number"
    '''
    try:
        n = int(sys.argv[1])
        if n >= 0:
            triangular = cal_triangular(n)
            print(f"The triangular number of {n} is {triangular}")
        else:
            print("Please enter a non-negative interger.")
    except ValueError:
        print("Please enter a vaild integer.")


def cal_triangular(n):
    '''
    Calculate the "triangular number"
    '''
    return (n * (n+1)) // 2


main()
