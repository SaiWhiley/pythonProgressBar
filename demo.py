from time import sleep
from progressBar import *

items = list(range(0,100))
i=0
length = len(items)
progressBar(i, length, prefix = 'Running: ', length = 50)
for items in items:
    sleep(0.1)
    i+=1
    progressBar(i, length, prefix = "Running: ", length = 50)