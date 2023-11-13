WIDTH = 500
HEIGHT = 500
PACMAN_HEIGHT = 100
PACMAN_WIDTH = 100
SPEED = 3
x = WIDTH / 2
y = HEIGHT / 2
x_add = 0
y_add = 0
mouth_angle = 45

def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)
    fill(1.0, 1.0, 0.0)
    noStroke()

def draw():
    global x, y, mouth_angle
    background(0)
    x = x + x_add
    y = y + y_add
    update_mouth_angle()
    handle_edge_cases()
    pacman(x, y, mouth_angle)

def pacman(x, y, angle):
    arc(x, y, PACMAN_WIDTH, PACMAN_HEIGHT, radians(angle), radians(360 - angle))

def keyPressed():
    global x_add, y_add
    if key == CODED:
        if keyCode == DOWN:
            x_add = 0
            y_add = SPEED
        elif keyCode == UP:
            x_add = 0
            y_add = -SPEED
        elif keyCode == LEFT:
            x_add = -SPEED
            y_add = 0
        elif keyCode == RIGHT:
            x_add = SPEED
            y_add = 0

def update_mouth_angle():
    global mouth_angle
    if x_add > 0:
        mouth_angle = 45
    elif x_add < 0:
        mouth_angle = 225
    elif y_add > 0:
        mouth_angle = 315
    elif y_add < 0:
        mouth_angle = 135

def handle_edge_cases():
    global x, y
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
