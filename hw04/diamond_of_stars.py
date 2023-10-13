import sys


def main(height):
    '''
    Draw diamond of stars with space and asterisk
    '''
    for i in range(height):
        space = (abs(2*i + 1 - height)//2)
        asterisk = min(2*i+1, (height-i)*2 -1)
        print(" "*space + "*"*asterisk)


main(int(sys.argv[1]))
