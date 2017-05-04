##Sai Whiley May 2017 ##

##iteration and totalIter are required.

def progressBar(iteration, totalIter, prefix='', suffix ='', decimals = 1, length = 100, fill = '█'):

    percentage = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(totalIter)))
    progress = int(length * iteration // totalIter)
    bar = fill * progress + '-' * (length - progress)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percentage, suffix), end = '\r')
    if(iteration == totalIter):
        print()
    