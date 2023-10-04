# Draw a Christmas tree

def main():
    edge_number = 3
    width = int(input("Please input an odd value of 3 or greater: "))
    row = (width + 1)//2
    while width < edge_number or width % 2 == 0:
        width = int(input("Please input an odd value of 3 or greater: "))

    for i in range(row):
        if i == 0:
            print((width-1)//2 * " " + "*")
        elif i == row - 1:
            print("/"+"_"*(width-2) + "\\")
        else:
            spaces = (row - i-1) * " "
            slashes = "/" + (2*i-1) * " " + "\\"
            print(spaces + slashes)


main()
