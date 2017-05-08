# -*- coding:utf-8 -*-
class binHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # 将 i 位置上的元素，上浮到正确的位置
    def floatUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i //= 2

    def insertHeap(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.floatUp(self.currentSize)

    def sinkDown(self, i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):
        if (2 * i + 1) > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] > self.heapList[i*2+1]:
                return i*2+1
            else:
                return i*2

    def delMin(self):
        reVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.sinkDown(1)
        return reVal

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.sinkDown(i)
            i -= 1

bh = binHeap()
bh.buildHeap([9, 5, 9, 6, 2, 3, 5])


print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
