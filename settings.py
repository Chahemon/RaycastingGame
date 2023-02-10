import math

# GAME SETTINGS
REAL_RES = 1140, 725
RES = WIDTH, HEIGHT = 900, 725
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60

PLAYER_POS = 5, 6
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.002
PLAYER_ROT_SPEED = 0.002

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS