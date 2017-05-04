from time import sleep
from progressBar import *

items = list(range(0,57))
i=0
l = len(items)
progressBar(i, l, prefix = 'Running: ', length = 50)
for items in items:
    sleep(0.1)
    i+=1
    progressBar(i, l, prefix = "Running: ", length = 50)