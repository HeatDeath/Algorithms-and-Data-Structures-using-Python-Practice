import time
from random import randrange

alist = []

def find_min(alist):
    #假设alist中的第一个数字最小
    my_min = alist[0]
    #遍历alist
    for i in alist:
        #最小标记flag指示i是否为alist最小，初始为True
        flag = True
        #遍历alist
        for j in alist:
            #如果i>j(存在比i小的数)
            if i >j:
                #标记flag为false
                flag = False
        #当i为alist最小，my_min=i
        if flag:
            my_min = i
    return my_min

def findMin(alist):
    #初始化当前最小值minsofar=alist[0]
    minsofar = alist[0]
    #遍历alist
    for i in alist:
        #如果i小于minsofar
        if i < minsofar:
            minsofar = i
    return minsofar

#当list长度为100,000的时候，算法一等了1分多钟没算出来...
#当list长度为100,000*100的时候，算法二只要0.2s...
#当list长度为100,000*1000的时候，算法二python占用了3.2Gb内存，CPU占用30%，等了半分钟，也算不出来了...


listSize = 100000000
'''
alist = [randrange(10000000) for i in range(listSize)]
start = time.time()
print(find_min(alist))
end = time.time()
print('验证:%d'%min(alist))
print("listlength:{0},time:{1},O(n)=n^2".format(listSize,end-start))
print('---------------------------------------------------------------')
'''
alist = [randrange(10000000) for i in range(listSize)]
start = time.time()
print(findMin(alist))
end = time.time()
print('验证:%d'%min(alist))
print("listlength:%d,time:%.30f,O(n)=n"% (listSize,end-start))
print('-------------------ENDENDENDENDENDENDEND-------------------------')
