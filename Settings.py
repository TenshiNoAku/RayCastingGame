import math

SIZE = width, height = 1200, 800
WALL = 100
FPS = 60
RENDER_DISTANCE = 600  # Дальность прорисовки луча(пиксели)
RAY_NUMBER = 100
FOV = math.pi / 3  # Угол обзора
HALF_FOV = FOV / 2
PROJ_COEFF = (RAY_NUMBER / (2 * math.tan(HALF_FOV))) * WALL * 3
SCALE = SIZE[0] // RAY_NUMBER
MAP_WALL = WALL // 5
MAP_POS = (0, SIZE[1] - SIZE[1] // 5)
DELTA_ANGLE = FOV / RAY_NUMBER  # Угол между лучами
PLAYER_SPEED = 1.5
COLOR_SKYBLUE = (135, 206, 235)
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_DARKGRAY = (105, 105, 105)
COLOR_DARKSLATEGRAY = (47, 79, 79)
