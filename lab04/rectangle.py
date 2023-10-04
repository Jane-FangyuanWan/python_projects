# Drawing a rectangle
def draw_rectangle():
    edge_number = 2
    symbol = input("Please input symbol: ")
    width = int(input("Please input width: "))
    height = int(input("Please input height: "))

    if width < edge_number or edge_number < 2:
        print("Width and height must be at least 2.")
    else:
        print(symbol * width)

    for _ in range(height - 2):
        print(symbol + " " * (width - 2) + symbol)

    if height > 1:
        print(symbol * width)


draw_rectangle()
