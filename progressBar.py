

def progressBar(iteration, totalIter, prefix='', suffix ='', decimals = 1, length = 100, fill = '█'):

    percentage = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(totalIter)))
    progress = int(length * iteration // totalIter)
    bar = fill * progress + '-' * (length - progress)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percentage, suffix), end = '\r')
    if(iteration == totalIter):
        print()
    


from time import sleep

items = list(range(0,57))
i=0
l = len(items)
progressBar(i, l, prefix = 'Running: ', length = 50)
for items in items:
    sleep(0.1)
    i+=1
    progressBar(i, l, prefix = "Running: ", length = 50)