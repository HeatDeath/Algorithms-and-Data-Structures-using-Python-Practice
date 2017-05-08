'''
由于交换数量的减少，选择排序通常比冒泡排序执行得更快。
'''

def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0

        #使用location作为下标遍历alist的剩余项
        for location in range(1, fillslot + 1):

            #当alist中的当前项大于alist中的已知最大项的时候
            if alist[location] > alist[positionOfMax]:

                #将最大项的下标替换为当前项
                positionOfMax = location

        #当遍历结束后，将最大项放到剩余list的最后一项（交换剩余项的最后一项与最大项）
        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist)
print(alist)