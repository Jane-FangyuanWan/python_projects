# Fangyuan Wan
# Print out a rocket

import sys


def draw_nose_cone(width):
    """
    Print out the nose cone of the rocket
    """
    TWO = 2
    start = width % TWO
    for i in range(start, width, TWO):
        asterisk = "*" * i
        space = " "*((width-i)//TWO)
        nose_cone = space + asterisk
        print(nose_cone)


def draw_fuselage(width, length, striped=None):
    """
    Print out the fuselage of the rocket
    """
    TWO = 2
    if striped == "striped":
        for _ in range(length):
            for _ in range(width//TWO):
                striped_lines = "_" * width
                print(striped_lines)
            for _ in range(width-width//TWO):
                x_lines = "X" * width
                print(x_lines)
    else:
        for _ in range(width * length):
            fuselage = width * "X"
            print(fuselage)


def draw_tail(width):
    """
    Print out the tail of the rocket
    """
    ONE = 1
    TWO = 2
    for i in range((width)//TWO, width+ONE, TWO):
        space = " "*((width-i)//TWO)
        asterisk = "*" * i
        line = space + asterisk
        print(line)
    bottom_of_tail = "*" * width
    print(bottom_of_tail)


def main():
    """
    Draw a rocket
    """
    ONE = 1
    TWO = 2
    THREE = 3
    width = int(sys.argv[ONE])
    length = int(sys.argv[TWO])
    draw_nose_cone(width)
    if len(sys.argv[ONE:]) == THREE:
        striped = sys.argv[THREE]
        draw_fuselage(width, length, striped)
    else:
        draw_fuselage(width, length)
    draw_tail(width)


main()
