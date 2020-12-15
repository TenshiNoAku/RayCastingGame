import math

SIZE = width, height = 1200, 800
WALL = 100
FPS = 60
RENDER_DISTANCE = 600  # Дальность прорисовки луча(пиксели)
RAY_NUMBER = 100
FOV = math.pi / 3  # Угол обзора
HALF_FOV = FOV / 2
DELTA_ANGLE = FOV * 57 / RAY_NUMBER  # Угол между лучами
PLAYER_SPEED = 1
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
