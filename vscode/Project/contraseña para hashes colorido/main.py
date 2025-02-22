from hashlib import md5
import time
from printy import printy
import random

dict_list = open('./dict.txt', 'r').readline()
password = 'd4705b9f42c96eeb0b9fb53266013516'
colors = ['c', 'o', 'o>', 'p>', 'p', 'c>', 'm', 'm>',
          'b>', '<b', '<y', 'y>', 'n', 'n>', 'r', 'r>', 'g', 'w']

for k in dict_list:
    k = (k).replace('\n', '')
    hash = md5(bytes(k, 'utf-8')).hexdigest()
    cIndex = random.randint(0, (len(colors) - 1))
    printy(f'[{colors[cIndex]}]' + hash)
    time.sleep(0.02)
    if hash == password:
        printy(f'[o>]Your password is: {k}')
        break
