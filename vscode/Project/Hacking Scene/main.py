from random import randint, random, choice
import shutil
import sys
import time
from printy import printy  # pip install printy

mn_strm_len = 6
mx_strm_len = 14
chars = ["0", "1"]
density = 0.03
width = shutil.get_terminal_size()[0]-1
colors = ['c>', 'p>', 'b>', 'o>', 'r>', 'm>']
cols = [0] * width
while True:
    for i in range(width):
        if cols[i] == 0:
            if random() <= density:
                cols[i] = randint(mn_strm_len, mx_strm_len)
            if cols[i] > 0:
                printy(f"[{choice(colors)}]{choice(chars)}", end='')
                cols[i] -= 1
            else:
                print(' ', end='')
    print()
    sys.stdout.flush()
    time.sleep(0.1)
