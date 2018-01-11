import itertools


def nextTime(S):


    time = list(S)
    time.remove(':')
    ck1 = []
    ck2 = []
    
    print list(itertools.permutations(time))

    for x in list(itertools.permutations(time)):
        if x > (time) and x < [2,3,5,9]:
            ck1.append(x)
            print x
        elif x < (time):
            ck2.append(x)
    
    if ck1:
        print min(ck1)
    elif ck2:
        print min(ck2)
    else:
        print time

x = "11:59"
nextTime(x)
