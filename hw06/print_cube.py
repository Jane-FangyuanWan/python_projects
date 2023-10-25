# Fangyuan Wan
# Draw a cube

class Characters:
    """
    Create a class to store the symbols
    """
    PLUS = "+"
    HORIZONTAL = "-"
    VERTICAL = "|"
    DIAGONAL = "/"
    SPACE = " "


class DrawCube:
    """
    Manage the prompting and drawing of the cube.
    """

    def __init__(self):
        self.cube_size: int | None = None

    def get_cube_size(self):
        TWO = 2
        self.cube_size: int = int(input("Input cube size (multiple of 2): "))
        while self.cube_size % TWO != 0:
            self.cube_size = int(
                input("PLEASE Input cube size (multiple of 2): "))

    def draw_corner_and_horizontal(self):
        TWO = 2
        horizontal_characters: int = self.cube_size * TWO
        return (Characters.PLUS +
                Characters.HORIZONTAL * horizontal_characters +
                Characters.PLUS)

    def top_half_cube(self):
        TWO = 2
        ONE = 1
        height = int(self.cube_size / TWO + TWO)
        left_white_spaces: int = int(self.cube_size / TWO + ONE)
        mid_white_spaces: int = int(self.cube_size * TWO)
        first_line: int = 0
        for line in range(height):
            if line == first_line:
                print(Characters.SPACE * (left_white_spaces - line) +
                      self.draw_corner_and_horizontal())
            elif line == height - ONE:
                print(Characters.SPACE * (left_white_spaces - line) +
                      self.draw_corner_and_horizontal() +
                      Characters.SPACE * (line - ONE) +
                      Characters.VERTICAL)
            else:
                print(Characters.SPACE * (left_white_spaces - line) +
                      Characters.DIAGONAL +
                      Characters.SPACE * mid_white_spaces +
                      Characters.DIAGONAL +
                      Characters.SPACE * (line - ONE) +
                      Characters.VERTICAL)

    def bottom_half(self):
        """
        Draw the bottom half of the cube.
        """
        ONE = 1
        TWO = 2
        height: int = self.cube_size + ONE
        mid_white_spaces: int = self.cube_size * TWO
        right_white_spaces: int = int(self.cube_size / TWO)
        for line in range(height):
            if line == self.cube_size / TWO - ONE:
                print(Characters.VERTICAL +
                      Characters.SPACE * mid_white_spaces +
                      Characters.VERTICAL +
                      Characters.SPACE * right_white_spaces +
                      Characters.PLUS)
            elif line < self.cube_size / TWO - ONE:
                print(Characters.VERTICAL +
                      Characters.SPACE * mid_white_spaces +
                      Characters.VERTICAL +
                      Characters.SPACE * right_white_spaces +
                      Characters.VERTICAL)
            elif self.cube_size / TWO <= line < self.cube_size:
                print(Characters.VERTICAL +
                      Characters.SPACE * mid_white_spaces +
                      Characters.VERTICAL +
                      Characters.SPACE *
                      (self.cube_size - line - ONE) +
                      Characters.DIAGONAL)
            elif line == self.cube_size:
                print(self.draw_corner_and_horizontal())

    def draw_cube(self):
        """
        Call the three functions above to draw the cube.
        """
        self.get_cube_size()
        self.top_half_cube()
        self.bottom_half()


def main():
    """
    Draw the cube
    """
    draw_cube = DrawCube()
    draw_cube.draw_cube()


main()
