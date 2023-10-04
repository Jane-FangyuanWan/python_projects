# draw a circle
import math


def main():
    radius = int(input("Enter a radius: "))

    for i in range(2 * radius):
        for j in range(2 * radius-1):
            # Calculate the distance from the center of the grid
            distance = math.sqrt((i - radius) ** 2 + (j - radius) ** 2)

            if distance >= radius:
                print(" ", end="")
                # Print "o" for positions inside the circle
            else:
                # Print a space for positions outside the circle
                # 'end=""' is used to print o without a new line charater or space so we can continue printing on the same line#
                print("o", end="")
        print()  # Move to the next row


main()
