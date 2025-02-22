import time
from printy import printy

printy('[c]Entering in system...')
time.sleep(.5)

for i in range(101):
    printy('[n]System hack progress: @[n>]' + str(i) + '%', end='\r')
    time.sleep(.02)

printy('[p>]System hack progress: 100%')
time.sleep(0.5)
printy('[o>]System hacked')
time.sleep(0.5)
printy('----()')
printy('||||')
