import timeit
import random

for i in range(10000,1000001,20000):
    t = timeit.Timer("x.get(random.randrange(%d))"%i,"from __main__ import random,x")


    x={j:j+1 for j in range(i)}

    d_time = t.timeit(number=1000)

    print("%d,%10.4f "%(i,d_time))