WIDTH = 500
HEIGHT = 500
SPEED = 3
x = WIDTH / 2
y = HEIGHT / 2
x_add = 0
y_add = 0

PACMAN_WIDTH = 100
PACMAN_HEIGHT = 100
max_mouth_angle = 45
min_mouth_angle = 0
mouth_angle = 0
open_close = 5
rot_begin = 0
rot_end = 360

def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)
    fill(1.0, 1.0, 0.0)
    noStroke()

def draw():
    global x, y, mouth_angle, open_close
    background(0)

    if mouth_angle > max_mouth_angle:
        open_close = -5
    if mouth_angle < min_mouth_angle:
        open_close = 5

    mouth_angle = mouth_angle + open_close
    x = x + x_add
    y = y + y_add

    if x > WIDTH + PACMAN_WIDTH / 2:
        x = PACMAN_WIDTH / 2
    elif x > WIDTH - PACMAN_WIDTH / 2:
        pacman(x - WIDTH, y)
    if y > HEIGHT + PACMAN_HEIGHT / 2:
        y = PACMAN_HEIGHT / 2
    elif y > HEIGHT - PACMAN_HEIGHT / 2:
        pacman(x, y - HEIGHT)
    if x < -(PACMAN_WIDTH / 2):
        x = WIDTH - PACMAN_WIDTH / 2
    elif x < PACMAN_WIDTH / 2:
        pacman(x + WIDTH, y)
    if y < -(PACMAN_HEIGHT / 2):
        y = HEIGHT - PACMAN_HEIGHT / 2
    elif y < PACMAN_HEIGHT / 2:
        pacman(x, y + HEIGHT)
        
    pacman(x, y)


def pacman(x, y):
    arc(x, y, PACMAN_WIDTH, PACMAN_HEIGHT, radians(rot_begin + mouth_angle), radians(rot_end - mouth_angle))


def keyPressed():
    global x_add, y_add, rot_begin, rot_end
    if key == CODED:
        if keyCode == DOWN:
            rot_begin = 90
            rot_end = 450
            x_add = 0
            y_add = SPEED
        elif keyCode == UP:
            rot_begin = -90
            rot_end = 270
            x_add = 0
            y_add = -SPEED
        elif keyCode == LEFT:
            rot_begin = 180
            rot_end = 540
            x_add = -SPEED
            y_add = 0
        elif keyCode == RIGHT:
            rot_begin = 0
            rot_end = 360
            x_add = SPEED
            y_add = 0
