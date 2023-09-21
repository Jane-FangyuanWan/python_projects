import math

def main():
    angle = int(input("Enter an angle: "))
    cosine = math.cos(angle)
    sine = math.sin(angle)

    print(f"The cosine of {angle} is: {cosine:.2f}")
    print(f"The sine of {angle} is: {sine:.2f}")

main()
