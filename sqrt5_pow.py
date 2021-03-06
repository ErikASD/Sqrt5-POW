import math
from time import time

START_TIME = time()

for _ in range(100000):
    SQRT_5 = math.sqrt(5)
RESET_TIME = time()
print(f'{SQRT_5=},{START_TIME-time()}')

for _ in range(100000):
    PERFECT = (1 + SQRT_5)/2
PERFECT_INVERSE = (1 - SQRT_5)/2
print(f'{PERFECT - PERFECT_INVERSE}, {RESET_TIME-time()}')


