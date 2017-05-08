from timeit import Timer
import random

for i in range(10000,1000001,20000):
    t = Timer("x[random.randrange(%d)]"%i,"from __main__ import random,x")

    x=list(range(i))

    print("%10.4f"%t.timeit(number=1000))

