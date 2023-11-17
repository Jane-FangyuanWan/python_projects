from maze import Maze
from game_controller import GameController


def test_constructor():
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450,
             100, 300, g)
    assert m.LEFT_VERT == 150
    assert m.RIGHT_VERT == 450
    assert m.TOP_HORIZ == 100
    assert m.BOTTOM_HORIZ == 300
    assert m.WIDTH == 600
    assert m.HEIGHT == 400
    assert m.gc is g
    assert m.dots.dots_left() == ((m.dots.WIDTH//m.dots.SPACING + 1) * 2 +
                                  (m.dots.HEIGHT//m.dots.SPACING + 1) * 2)


def test_eat_dots():
    WIDTH = 600
    HEIGHT = 600
    LEFT_VERT = 150
    RIGHT_VERT = 450
    TOP_HORIZ = 150
    BOTTOM_HORIZ = 450
    game_controller = GameController(WIDTH, HEIGHT)

    # Initialize the Maze
    maze = Maze(WIDTH, HEIGHT, LEFT_VERT, RIGHT_VERT, TOP_HORIZ,
                BOTTOM_HORIZ, game_controller)

    # Assume Pac-Man's position near a dot in the top row
    pacman_x = maze.dots.top_row[0].x
    pacman_y = maze.dots.top_row[0].y

    # Get initial dot count
    initial_dot_count = maze.dots.dots_left()

    # Act: Pac-Man eats a dot
    maze.eat_dots(pacman_x, pacman_y)

    # Assert: Check if a dot was eaten
    assert maze.dots.dots_left() == initial_dot_count - 1
