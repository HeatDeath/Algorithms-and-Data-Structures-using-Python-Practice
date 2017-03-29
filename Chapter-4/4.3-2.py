def listsum(numlist):
    theSum = 0
    for i in numlist:
        theSum = theSum + i
    return theSum

print(listsum([x for x in range(1,11,2)]))