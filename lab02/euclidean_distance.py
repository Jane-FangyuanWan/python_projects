import math
def main():
    X1 = int(input("Enter a numerical value for X1: "))
    X2 = int(input("Enter a numerical value for X2: "))
    Y1 = int(input("Enter a numerical value for Y1: "))
    Y2 = int(input("Enter a numerical value for Y2: "))

    distance = math.sqrt((X1 -X2) ** 2 + (Y1 - Y2) ** 2)

    print(f"Euclidean distance between the two points = {distance: .2f}")


main()